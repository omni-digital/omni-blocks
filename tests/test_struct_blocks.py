from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils.crypto import get_random_string
from wagtail.core.blocks import StructBlock
from wagtail.images.tests.utils import Image, get_test_image_file
from wagtail_factories import PageFactory, SiteFactory

from omni_blocks.blocks import struct_blocks


class TestButtonBlock(TestCase):
    def test_renders(self):
        """Ensure that the block renders as expected."""
        block = struct_blocks.ButtonBlock()
        value = block.to_python(
            {"title": "Omni Digital", "link": {"external_url": "https://omni-digital.co.uk"}}
        )
        self.assertIn('<div class="button_block">', block.render(value))
        self.assertIn(
            '<a class="button__anchor" href="https://omni-digital.co.uk">Omni Digital</a>',
            block.render(value),
        )


class TestColumnBlock(TestCase):
    """Tests for the internal_blocks.ColumnBlock."""

    def setUp(self):
        self.block = struct_blocks.ColumnBlock
        self.image = Image.objects.create(title="Test image", file=get_test_image_file())

    def test_parent_class(self):
        """Test ColumnBlock is a subclass of StructBlock."""
        self.assertTrue(issubclass(self.block, StructBlock))

    def test_validation_image_and_paragraph(self):
        """Test ColumnBlock.clean() validates data as expected."""
        block = self.block()
        data = {"image": self.image.pk, "paragraph": get_random_string()}
        with self.assertRaises(ValidationError) as context:
            block.clean(block.to_python(data))
        self.assertIn(block.both_fields_error, context.exception.messages)

    def test_validation_not_image_and_not_paragraph(self):
        """Test ColumnBlock.clean() validates data as expected."""
        block = self.block()
        with self.assertRaises(ValidationError) as context:
            block.clean(block.value_from_datadict({}, {}, ""))
        self.assertIn(block.no_data_error, context.exception.messages)

    def test_validation_data(self):
        """Test ColumnBlock.clean() validates data as expected."""
        block = self.block()
        key = "paragraph"
        val = get_random_string()
        data = block.clean(block.to_python({key: val}))
        self.assertIn(val, str(data[key]))


class TestLinkBlock(TestCase):
    def setUp(self):
        self.block = struct_blocks.LinkBlock()
        root = PageFactory.create(title="home", parent=None)
        self.site = SiteFactory.create(root_page=root)
        self.page = PageFactory.create(title="Omni Digital", parent=root)

    def test_external_url_renders(self):
        """Ensure the block renders in isolation."""
        value = self.block.to_python({"external_url": "https://omni-digital.co.uk"})
        content = self.block.render(value)

        self.assertEqual("https://omni-digital.co.uk", content)

    def test_internal_url_renders(self):
        """Ensure that the internal_url renders as expected."""
        value = self.block.render({"internal_url": self.page})

        self.assertEqual(value, "{}/omni-digital/".format(self.site.root_url))

    def test_data_validation_external_and_internal_url(self):
        """Ensure that the data is validated as expected."""
        with self.assertRaises(ValidationError) as context:
            self.block.clean(
                {"external_url": "https://omni-digital.co.uk", "internal_url": self.page.pk}
            )

        self.assertIn(self.block.both_urls_error, context.exception.messages)

    def test_data_validation_no_urls(self):
        """Ensure that the data is validated as expected."""
        with self.assertRaises(ValidationError) as context:
            self.block.clean({"external_url": None, "internal_url": None})

        self.assertIn(self.block.no_urls_error, context.exception.messages)

    def test_data_validation_link_not_required(self):
        """Ensure that if the block is not required, we don't raise validation errors."""
        unrequired_block = struct_blocks.LinkBlock(required=False)
        try:
            unrequired_block.clean({"external_url": None, "internal_url": None})
        except ValidationError:
            self.fail("LinkBlock clean raised exception when not required and links are empty.")

    def test_data_validation(self):
        """Ensure that the data is validated as expected."""
        key = "external_url"
        value = "https://omni-digital.co.uk"
        data = self.block.clean({key: value})

        self.assertIn(value, str(data[key]))


class TestTitledLinkBlock(TestCase):
    def test_renders(self):
        """Ensure that the block renders as expected."""
        block = struct_blocks.TitledLinkBlock()
        value = block.to_python(
            {"title": "Omni Digital", "link": {"external_url": "https://omni-digital.co.uk"}}
        )
        self.assertIn(
            '<a class="titled_link" href="https://omni-digital.co.uk">Omni Digital</a>',
            block.render(value),
        )
