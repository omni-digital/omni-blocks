from __future__ import unicode_literals

from django.utils.safestring import mark_safe
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
