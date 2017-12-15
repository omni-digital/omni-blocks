from __future__ import unicode_literals

from django.utils.safestring import mark_safe
from django.utils.text import slugify
from wagtail.wagtailcore.blocks import BlockQuoteBlock, CharBlock


class HBlock(CharBlock):
    """A block for displaying headings."""
    def __init__(self, tag, icon='title', classname='title', *args, **kwargs):
        self.tag = tag
        super(HBlock, self).__init__(
            icon=icon,
            classname=classname,
            *args,
            **kwargs
        )

    def render(self, value, context=None):
        """
        Renders the block contents and returns them as a safe string.

        :param value: The value from the database to render
        :return: Safe String - Rendered block content
        """
        return mark_safe('<{tag}>{contents}</{tag}>'.format(
            tag=self.tag,
            contents=self.render_basic(value, context=context)
        ))


class JumpHBlock(CharBlock):
    """Special type of heading for adding jumplinks to a page."""
    ANCHOR_PREFIX = 'heading'

    def __init__(self, tag, icon='title', classname='title', *args, **kwargs):
        """Load the tag into self."""
        self.tag = tag
        super(JumpHBlock, self).__init__(
            icon=icon,
            classname=classname,
            *args,
            **kwargs
        )

    @staticmethod
    def make_jump_link(value):
        """Create a jumpable link."""
        return '{0}-{1}'.format(JumpHBlock.ANCHOR_PREFIX, slugify(value))

    def get_context(self, value, parent_context=None):
        """Add the tag and anchor into our context."""
        context = super(JumpHBlock, self).get_context(
            value,
            parent_context=parent_context,
        )
        context['tag'] = self.tag
        context['anchor'] = self.make_jump_link(value)
        return context

    class Meta:
        template = 'blocks/jump_h_block.html'
        name = 'Jump H2'


class PullQuoteBlock(CharBlock):
    """ Blockquote with additional css class """

    class Meta(object):
        """Wagtail properties."""
        icon = 'openquote'
        label = 'Pull Quote'
        template = 'blocks/pull_quote_block.html'


class QuoteBlock(BlockQuoteBlock):
    """ BlockQuote with external template """

    class Meta(object):
        """Wagtail properties."""
        icon = 'openquote'
        label = 'Quote'
        template = 'blocks/quote_block.html'
