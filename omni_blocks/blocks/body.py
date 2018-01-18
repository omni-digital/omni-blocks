from __future__ import unicode_literals

from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock

from omni_blocks.blocks.image_blocks import ImageGridBlock, LinkedImageGridBlock
from omni_blocks.blocks import list_blocks
from omni_blocks.blocks.chooser_blocks import PageChooserTemplateBlock
from omni_blocks.blocks.struct_blocks import ButtonBlock, GoogleMapBlock, TwoColumnBlock
from omni_blocks.blocks.text_blocks import HBlock, JumpHBlock, PullQuoteBlock, QuoteBlock


class BodyStreamBlock(blocks.StreamBlock):
    """Stream block for the body field on all pages."""
    # Chooser blocks
    related_page = PageChooserTemplateBlock()

    # Image blocks
    image = ImageChooserBlock()
    image_grid = ImageGridBlock()
    linked_image_grid = LinkedImageGridBlock()

    # List blocks
    basic_card_grid = list_blocks.BasicCardGridBlock()
    flow_list = list_blocks.FlowListBlock()
    ordered_list = list_blocks.OLBlock()
    unordered_list = list_blocks.ULBlock()

    # Struct blocks
    button = ButtonBlock()
    google_map = GoogleMapBlock()
    two_column = TwoColumnBlock()

    # Text blocks
    h1 = HBlock(tag='h1')
    h2 = HBlock(tag='h2')
    h3 = HBlock(tag='h3')
    h4 = HBlock(tag='h4')
    jump_h2 = JumpHBlock(tag='h2')
    paragraph = blocks.RichTextBlock()
    pull_quote = PullQuoteBlock()
    quote = QuoteBlock()

    # Wagtail blocks
    table = TableBlock()
