from __future__ import unicode_literals

from django.utils.html import format_html, format_html_join
from wagtail.wagtailcore.blocks import CharBlock
from wagtail.wagtailcore.blocks.list_block import ListBlock

from omni_blocks.blocks.struct_blocks import BasicCardBlock, FlowBlock


class BasicCardGridBlock(ListBlock):
    """Block for displaying a grid of cards."""

    def __init__(self, **kwargs):
        """
        Instantiates an ImageChooserBlock instance,
        then passes it to the super class for list rendering.

        :param kwargs: Default keyword args
        :type kwargs: {}
        """
        child_block = BasicCardBlock(required=True)
        super(BasicCardGridBlock, self).__init__(child_block, **kwargs)

    class Meta(object):
        """Wagtail properties."""
        icon = 'form'
        label = 'Basic Card Grid'
        template = 'blocks/basic_card_grid_block.html'


class FlowListBlock(ListBlock):
    """Block for displaying lists of data points."""
    def __init__(self, **kwargs):
        """
        Instantiates FlowBlock instance, then passes it to the super
        class for list rendering.

        :param kwargs: Default keyword args
        :type kwargs: {}
        """
        child_block = FlowBlock(required=True)
        super(FlowListBlock, self).__init__(child_block, **kwargs)

    class Meta(object):
        """Wagtail properties."""
        icon = 'list-ul'
        label = 'Flow List'
        template = 'blocks/flow_list_block.html'


class ULBlock(ListBlock):
    """Block for displaying an unordered of rich text."""
    def __init__(self, **kwargs):
        """
        Instantiates an RichTextBlock instance,
        then passes it to the super class for list rendering.

        :param kwargs: Default keyword args
        :type kwargs: {}
        """
        child_block = CharBlock(required=True)
        super(ULBlock, self).__init__(child_block, **kwargs)

    class Meta(object):
        """Wagtail properties."""
        icon = 'list-ul'
        label = 'Unordered List'


class OLBlock(ULBlock):
    """Block for displaying an ordered of rich text."""
    class Meta(object):
        """Wagtail properties."""
        icon = 'list-ol'
        label = 'Ordered List'

    def render_basic(self, value, context=None):
        child_list = []
        for child_value in value:
            child_list.append((self.child_block.render(child_value, context=context),))

        children = format_html_join('\n', '<li>{0}</li>', child_list)
        return format_html("<ol>{0}</ol>", children)
