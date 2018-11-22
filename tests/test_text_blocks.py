from django.test import TestCase
from wagtail.core.blocks import CharBlock, BlockQuoteBlock

from omni_blocks.blocks.text_blocks import HBlock, JumpHBlock, PullQuoteBlock, QuoteBlock


class TestHBlock(TestCase):
    """Tests for the HBlock."""
    def test_parent_class(self):
        """Test HBlock is a subclass of CharBlock."""
        self.assertTrue(issubclass(HBlock, CharBlock))

    def test_render(self):
        """Test HBlock.render renders as expected."""
        block = HBlock('h2')
        expected = '<h2>some text</h2>'
        result = block.render('some text', context={})

        self.assertEqual(result, expected)


class TestJumpHBlock(TestCase):
    """Test the JumpHBlock block."""
    block = JumpHBlock

    def test_make_jump_link(self):
        """Make Jump Link should return a slugified url."""
        self.assertEqual(
            'heading-my-cool-link',
            self.block.make_jump_link('My Cool Link')
        )

    def test_block_renders(self):
        """Ensure the block renders."""
        block = self.block(tag='h2')
        rendered = block.render('My Heading')
        self.assertIn('<h2 id="heading-my-heading">', rendered)
        self.assertIn('My Heading', rendered)


class TestPullQuoteBlock(TestCase):
    """Tests for the PullQuoteBlock."""
    def test_parent_class(self):
        """Test PullQuoteBlock is a subclass of CharBlock."""
        self.assertTrue(issubclass(PullQuoteBlock, CharBlock))

    def test_render(self):
        """Test PullQuoteBlock.render renders as expected."""
        block = PullQuoteBlock()
        rendered = block.render('My quote')
        self.assertIn('<p class="pullquote__quote">', rendered)
        self.assertIn('My quote', rendered)


class TestQuoteBlock(TestCase):
    """Tests for the QuoteBlock."""
    def test_parent_class(self):
        """Test QuoteBlock is a subclass of BlockQuoteBlock."""
        self.assertTrue(issubclass(QuoteBlock, BlockQuoteBlock))

    def test_render(self):
        """Test QuoteBlock.render renders as expected."""
        block = QuoteBlock()
        rendered = block.render('My quote')
        self.assertIn('<p class="blockquote__quote">', rendered)
        self.assertIn('My quote', rendered)
