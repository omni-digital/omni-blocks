from __future__ import unicode_literals

from django.utils.safestring import mark_safe
from django.utils.text import slugify
from wagtail.core.blocks import BlockQuoteBlock, CharBlock


class HBlock(CharBlock):
    """A block for displaying headings, with ID for use in anchors."""
    def __init__(
        self,
        tag,
        icon='title',
        classname='title',
        slugified_id=False,
        *args,
        **kwargs,
    ):
        self.tag = tag
        self.slugified_id = slugified_id
        super(HBlock, self).__init__(
            icon=icon,
            classname=classname,
            *args,
            **kwargs,
        )

    def get_context(self, value, parent_context=None):
        """Add the tag, content, and slugified ID into our context."""
        context = super(HBlock, self).get_context(
            value,
            parent_context=parent_context,
        )
        context['tag'] = self.tag
        if self.slugified_id:
            context['slugified_id'] = slugify(value)
        return context

    class Meta:
        template = 'blocks/heading.html'



class JumpHBlock(CharBlock):
    """Special type of heading for adding jumplinks to a page."""

    ANCHOR_PREFIX = "heading"

    def __init__(self, tag, icon="title", classname="title", *args, **kwargs):
        """Load the tag into self."""
        self.tag = tag
        super(JumpHBlock, self).__init__(icon=icon, classname=classname, *args, **kwargs)

    @staticmethod
    def make_jump_link(value):
        """Create a jumpable link."""
        return "{0}-{1}".format(JumpHBlock.ANCHOR_PREFIX, slugify(value))

    def get_context(self, value, parent_context=None):
        """Add the tag and anchor into our context."""
        context = super(JumpHBlock, self).get_context(value, parent_context=parent_context)
        context["tag"] = self.tag
        context["anchor"] = self.make_jump_link(value)
        return context

    class Meta:
        template = "blocks/jump_h_block.html"
        name = "Jump H2"


class PullQuoteBlock(CharBlock):
    """ Blockquote with additional css class """

    class Meta(object):
        """Wagtail properties."""

        icon = "openquote"
        help_text = "A repeated section of text from this page's main flow of content."
        label = "Pull Quote"
        template = "blocks/pull_quote_block.html"


class QuoteBlock(BlockQuoteBlock):
    """ BlockQuote with external template """

    class Meta(object):
        """Wagtail properties."""

        icon = "openquote"
        help_text = "A quote from a person which is in this page's main flow of content."
        label = "Quote"
        template = "blocks/quote_block.html"
