from django.test import TestCase
from wagtail.wagtailimages.tests.utils import Image, get_test_image_file

from omni_blocks.blocks.image_blocks import LinkedImageBlock


class TestLinkedImageBlock(TestCase):
    def setUp(self):
        self.image = Image.objects.create(
            title="Test image",
            file=get_test_image_file(),
        )

    def test_image_link(self):
        """Ensure that the image link renders correctly"""
        block = LinkedImageBlock()
        value = block.to_python({
            'image': self.image.pk,
            'link': {'external_url': 'https://omni-digital.co.uk'},
        })
        self.assertIn(
            '<a href="https://omni-digital.co.uk"><img alt="Test image"',
            block.render(value)
        )
