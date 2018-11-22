from django.test import TestCase
from wagtail.core.blocks import PageChooserBlock
from wagtail_factories import PageFactory, SiteFactory

from omni_blocks.blocks.chooser_blocks import PageChooserTemplateBlock


class TestPageChooserTemplateBlock(TestCase):
    """Tests for the PageChooserTemplateBlock."""
    def setUp(self):
        self.block = PageChooserTemplateBlock()

    def test_parent_class(self):
        """PageChooserTemplateBlock should inherit from PageChooserBlock."""
        self.assertIsInstance(self.block, PageChooserBlock)

    def test_renders(self):
        """Ensure PageChooserTemplateBlock renders correctly."""
        page = PageFactory.create(parent=None, title='foo')
        SiteFactory.create(root_page=page)
        with self.assertTemplateUsed(
            template_name='blocks/page_chooser_block.html'
        ):
            response = self.block.render_basic(page)

        self.assertIn(page.title, response)
        self.assertIn(page.url, response)

    def test_renders_blank(self):
        """Ensure PageChooserTemplateBlock renders blank string when no page exists."""
        response = self.block.render_basic('')

        self.assertEqual(response, '')
