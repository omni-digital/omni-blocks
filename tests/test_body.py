from __future__ import unicode_literals

from django.test import TestCase
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock

from omni_blocks import blocks as internal_blocks


class TestBodyStreamBlock(TestCase):
    """Tests for the BodyStreamBlock."""

    def setUp(self):
        self.block = internal_blocks.BodyStreamBlock
        self.children = self.block().child_blocks

    def test_parent_class(self):
        """Test BodyStreamBlock is a subclass of StreamBlock."""
        self.assertTrue(issubclass(self.block, blocks.StreamBlock))

    def test_attributes(self):
        """Test BodyStreamBlock's attributes are correct."""
        expected = [
            # Chooser blocks
            'related_page',

            # Image blocks
            'image',
            'image_grid',
            'linked_image_grid',

            # List blocks
            'basic_card_grid',
            'flow_list',
            'ordered_list',
            'unordered_list',

            # Struct blocks
            'button',
            'google_map',
            'two_column',

            # Text blocks
            'h1',
            'h2',
            'h3',
            'h4',
            'jump_h2',
            'paragraph',
            'pull_quote',
            'quote',

            # Wagtail blocks
            'table',
        ]
        self.assertEqual(list(self.children.keys()), expected)

    def test_related_page(self):
        """Test BodyStreamBlock.related_page has the expected parent."""
        block = self.children.get('related_page')

        self.assertIsInstance(block, internal_blocks.PageChooserTemplateBlock)

    def test_image(self):
        """Test BodyStreamBlock.image has the expected parent."""
        block = self.children.get('image')

        self.assertIsInstance(block, ImageChooserBlock)

    def test_image_grid(self):
        """Test BodyStreamBlock.image_grid has the expected parent."""
        block = self.children.get('image_grid')

        self.assertIsInstance(block, internal_blocks.ImageGridBlock)

    def test_linked_image_grid(self):
        """Test BodyStreamBlock.linked_image_grid has the expected parent."""
        block = self.children.get('linked_image_grid')

        self.assertIsInstance(block, internal_blocks.LinkedImageGridBlock)

    def test_basic_card_grid(self):
        """Test BodyStreamBlock.basic_card_grid has the expected parent."""
        block = self.children.get('basic_card_grid')

        self.assertIsInstance(block, internal_blocks.BasicCardGridBlock)

    def test_flow_list(self):
        """Test BodyStreamBlock.flow_list has the expected parent."""
        block = self.children.get('flow_list')

        self.assertIsInstance(block, internal_blocks.FlowListBlock)

    def test_ordered_list(self):
        """Test BodyStreamBlock.ordered_list has the expected parent."""
        block = self.children.get('ordered_list')

        self.assertIsInstance(block, internal_blocks.OLBlock)

    def test_unordered_list(self):
        """Test BodyStreamBlock.unordered_list has the expected parent."""
        block = self.children.get('unordered_list')

        self.assertIsInstance(block, internal_blocks.ULBlock)

    def test_button_block(self):
        """Test BodyStreamBlock.button_block has the expected parent."""
        block = self.children.get('button')

        self.assertIsInstance(block, internal_blocks.ButtonBlock)

    def test_google_map(self):
        """Test BodyStreamBlock.google_map has the expected parent."""
        block = self.children.get('google_map')

        self.assertIsInstance(block, internal_blocks.GoogleMapBlock)

    def test_two_column(self):
        """Test BodyStreamBlock.two_column has the expected parent."""
        block = self.children.get('two_column')

        self.assertIsInstance(block, internal_blocks.TwoColumnBlock)

    def test_h1(self):
        """Test BodyStreamBlock.h1 has the expected parent."""
        block = self.children.get('h1')

        self.assertIsInstance(block, internal_blocks.HBlock)

    def test_h2(self):
        """Test BodyStreamBlock.h2 has the expected parent."""
        block = self.children.get('h2')

        self.assertIsInstance(block, internal_blocks.HBlock)

    def test_h3(self):
        """Test BodyStreamBlock.h3 has the expected parent."""
        block = self.children.get('h3')

        self.assertIsInstance(block, internal_blocks.HBlock)

    def test_h4(self):
        """Test BodyStreamBlock.h4 has the expected parent."""
        block = self.children.get('h4')

        self.assertIsInstance(block, internal_blocks.HBlock)

    def test_jump_h2(self):
        """Test BodyStreamBlock.jump_h2 has the expected parent."""
        block = self.children.get('jump_h2')

        self.assertIsInstance(block, internal_blocks.JumpHBlock)

    def test_paragraph(self):
        """Test BodyStreamBlock.paragraph has the expected parent."""
        block = self.children.get('paragraph')

        self.assertIsInstance(block, blocks.RichTextBlock)

    def test_pull_quote(self):
        """Test BodyStreamBlock.pull_quote has the expected parent."""
        block = self.children.get('pull_quote')

        self.assertIsInstance(block, internal_blocks.PullQuoteBlock)

    def test_quote(self):
        """Test BodyStreamBlock.quote has the expected parent."""
        block = self.children.get('quote')

        self.assertIsInstance(block, internal_blocks.QuoteBlock)

    def test_table(self):
        """Test BodyStreamBlock.table has the expected parent."""
        block = self.children.get('table')

        self.assertIsInstance(block, TableBlock)
