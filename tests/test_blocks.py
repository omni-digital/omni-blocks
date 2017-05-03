from django.test import TestCase
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks.field_block import RawHTMLBlock
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
            'basic_card',
            'block_quote',
            'google_map',
            'h1',
            'h2',
            'h3',
            'h4',
            'image',
            'image_grid',
            'linked_image_grid',
            'ordered_list',
            'paragraph',
            'pull_quote',
            'raw_html',
            'related_page',
            'table',
            'two_column',
            'unordered_list',
        ]
        self.assertEqual(list(self.children.keys()), expected)

    def test_basic_card(self):
        """Test BodyStreamBlock.basic_card has the expected parent."""
        block = self.children.get('basic_card')

        self.assertIsInstance(block, internal_blocks.BasicCardBlock)

    def test_block_quote(self):
        """Test BodyStreamBlock.block_quote has the expected parent."""
        block = self.children.get('block_quote')

        self.assertIsInstance(block, blocks.BlockQuoteBlock)

    def test_google_map(self):
        """Test BodyStreamBlock.google_map has the expected parent."""
        block = self.children.get('google_map')

        self.assertIsInstance(block, internal_blocks.GoogleMapBlock)

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

    def test_ordered_list(self):
        """Test BodyStreamBlock.ordered_list has the expected parent."""
        block = self.children.get('ordered_list')

        self.assertIsInstance(block, internal_blocks.OLBlock)

    def test_paragraph(self):
        """Test BodyStreamBlock.paragraph has the expected parent."""
        block = self.children.get('paragraph')

        self.assertIsInstance(block, blocks.RichTextBlock)

    def test_pull_quote(self):
        """Test BodyStreamBlock.pull_quote has the expected parent."""
        block = self.children.get('pull_quote')

        self.assertIsInstance(block, internal_blocks.PullQuoteBlock)

    def test_raw_html(self):
        """Test BodyStreamBlock.raw_html has the expected parent."""
        block = self.children.get('raw_html')

        self.assertIsInstance(block, RawHTMLBlock)

    def test_related_page(self):
        """Test BodyStreamBlock.related_page has the expected parent."""
        block = self.children.get('related_page')

        self.assertIsInstance(block, blocks.PageChooserBlock)

    def test_table(self):
        """Test BodyStreamBlock.table has the expected parent."""
        block = self.children.get('table')

        self.assertIsInstance(block, TableBlock)

    def test_two_column(self):
        """Test BodyStreamBlock.two_column has the expected parent."""
        block = self.children.get('two_column')

        self.assertIsInstance(block, internal_blocks.TwoColumnBlock)

    def test_unordered_list(self):
        """Test BodyStreamBlock.unordered_list has the expected parent."""
        block = self.children.get('unordered_list')

        self.assertIsInstance(block, internal_blocks.ULBlock)


class TestHBlock(TestCase):
    """Tests for the HBlock."""
    def test_parent_class(self):
        """Test HBlock is a subclass of CharBlock."""
        self.assertTrue(issubclass(internal_blocks.HBlock, blocks.CharBlock))

    def test_render(self):
        """Test HBlock.render renders as expected."""
        block = internal_blocks.HBlock('h2')
        expected = '<h2>some text</h2>'
        result = block.render('some text')

        self.assertEqual(result, expected)
