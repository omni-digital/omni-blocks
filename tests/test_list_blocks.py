from django.test import TestCase
from wagtail.wagtailcore.blocks import CharBlock, RichTextBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from omni_blocks.blocks.list_blocks import OLBlock, ULBlock
from omni_blocks.blocks.struct_blocks import FlowBlock, LinkBlock


class TestULBlock(TestCase):
    """Tests for the ULBlock."""
    def test_render_basic(self):
        """ Test block rendering """
        block = ULBlock()
        self.assertEqual(
            '<ul class=\"written_content_list\"><li>1</li>\n<li>2</li>\n<li>3</li>\n<li>4</li></ul>',
            block.render_basic(('1', '2', '3', '4'))
        )


class TestOLBlock(TestCase):
    """Tests for the OLBlock."""
    def test_parent_class(self):
        """Test OLBlock is a subclass of ULBlock."""
        self.assertTrue(issubclass(OLBlock, ULBlock))

    def test_render_basic(self):
        """ Test block rendering """
        block = OLBlock()
        self.assertEqual(
            '<ol class=\"written_content_list\"><li>1</li>\n<li>2</li>\n<li>3</li>\n<li>4</li></ol>',
            block.render_basic(('1', '2', '3', '4'))
        )


class TestFlowBlock(TestCase):
    block = FlowBlock()

    def test_meta_title(self):
        """Ensure FlowBlock.meta_title is the expected block type."""
        child_block = self.block.child_blocks['meta_title']

        self.assertIsInstance(child_block, CharBlock)
        self.assertTrue(child_block.required)

    def test_title(self):
        """Ensure FlowBlock.title is the expected block type."""
        child_block = self.block.child_blocks['title']

        self.assertIsInstance(child_block, CharBlock)
        self.assertFalse(child_block.required)

    def test_body(self):
        """Ensure FlowBlock.body is the expected block type."""
        child_block = self.block.child_blocks['body']

        self.assertIsInstance(child_block, RichTextBlock)
        self.assertFalse(child_block.required)

    def test_image(self):
        """Ensure FlowBlock.image is the expected block type."""
        child_block = self.block.child_blocks['image']

        self.assertIsInstance(child_block, ImageChooserBlock)
        self.assertFalse(child_block.required)

    def test_link(self):
        """Ensure FlowBlock.link is the expected block type."""
        child_block = self.block.child_blocks['link']

        self.assertIsInstance(child_block, LinkBlock)
        self.assertFalse(child_block.required)

    def test_renders(self):
        """Ensure FlowBlock renders as expected."""
        value = self.block.to_python({
            'meta_title': 'Meta Title',
            'title': 'Main Title',
            'body': 'This is the body.',
            'link': {'external_url': 'https://omni-digital.co.uk'},
        })
        response = self.block.render(value)

        self.assertIn('Meta Title', response)
        self.assertIn('Main Title', response)
        self.assertIn('This is the body.', response)
        self.assertIn('https://omni-digital.co.uk', response)
