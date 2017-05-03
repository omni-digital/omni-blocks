from django.core.exceptions import ValidationError
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks.field_block import RawHTMLBlock, URLBlock
from wagtail.wagtailcore.blocks.list_block import ListBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class ColumnBlock(blocks.StructBlock):
    """ """
    image = ImageChooserBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)

    def clean(self, value):
        cleaned_data = super(ColumnBlock, self).clean(value)
        errors = {}
        if cleaned_data['image'] and cleaned_data['paragraph']:
            msg = 'Please use either image or paragraph, not both'
            errors['image'] = errors['paragraph'] = ValidationError(msg)

        if not cleaned_data['image'] and not cleaned_data['paragraph']:
            msg = 'Please add either an image or a paragraph.'
            errors['image'] = errors['paragraph'] = ValidationError(msg)

        if errors:
            raise ValidationError(msg, params=errors)

        return cleaned_data


class TwoColumnBlock(blocks.StructBlock):
    """Two column block."""
    left_column = ColumnBlock(required=True)
    right_column = ColumnBlock(required=True)

    class Meta(object):
        """Wagtail properties."""
        icon = 'form'
        label = 'Two Column'
        template = 'blocks/two_column_block.html'


class GoogleMapBlock(blocks.StructBlock):
    """Block for embedding a google map."""
    longitude = blocks.CharBlock(required=True, max_length=255)
    latitude = blocks.CharBlock(required=True, max_length=255)
    zoom_level = blocks.CharBlock(default=14, required=True, max_length=3)

    class Meta(object):
        """
        Wagtail properties
        """
        template = 'blocks/google_map_block.html'
        icon = 'site'
        label = 'Google Map'


class HBlock(blocks.CharBlock):
    """A block for displaying headings."""
    def __init__(self, tag, icon='title', classname='title', *args, **kwargs):
        self.tag = tag
        super(HBlock, self).__init__(
            icon=icon,
            classname=classname,
            *args,
            **kwargs
        )

    def render(self, value):
        """
        Renders the block contents and returns them as a safe string.

        :param value: The value from the database to render
        :return: Safe String - Rendered block content
        """
        return mark_safe('<{tag}>{contents}</{tag}>'.format(
            tag=self.tag,
            contents=self.render_basic(value)
        ))


class LinkBlock(blocks.StructBlock):
    """"""
    external_url = URLBlock(required=False)
    internal_url = blocks.PageChooserBlock(
        icon='doc-empty-inverse',
        required=False,
    )

    def clean(self, value):
        cleaned_data = super(LinkBlock, self).clean(value)
        errors = {}
        if cleaned_data['external_url'] and cleaned_data['internal_url']:
            msg = 'Please select either internal URL or extrenal URL, not both.'
            errors['external_url'] = errors['internal_url'] = ValidationError(msg)

        if not cleaned_data['external_url'] and not cleaned_data['internal_url']:
            msg = 'Please select an internal URL or add an extrenal URL.'
            errors['external_url'] = errors['internal_url'] = ValidationError(msg)

        if errors:
            raise ValidationError(msg, params=errors)

        return cleaned_data

    class Meta(object):
        """Wagtail properties."""
        template = 'blocks/link_block.html'


class TitledLinkBlock(blocks.StructBlock):
    """"""
    title = blocks.CharBlock(required=True)
    link = LinkBlock(required=True)

    class Meta(object):
        """Wagtail properties."""
        icon = ''
        label = 'Link'
        template = 'blocks/titled_link_block.html'


class BasicCardBlock(blocks.StructBlock):
    """A basic material card block."""
    title = HBlock(tag='h2')
    image = ImageChooserBlock(required=False)
    link = TitledLinkBlock(required=False)
    description = blocks.RichTextBlock(required=False)

    class Meta(object):
        """Wagtail properties."""
        template = 'blocks/basic_card_block.html'
        icon = 'form'
        label = 'Basic card'


class ImageGridBlock(ListBlock):
    """Block for displaying a grid of images."""
    def __init__(self, **kwargs):
        """
        Instantiates an ImageChooserBlock instance,
        then passes it to the super class for list rendering.

        :param kwargs: Default keyword args
        :type kwargs: {}
        """
        child_block = ImageChooserBlock(required=True)
        super(ImageGridBlock, self).__init__(child_block, **kwargs)

    class Meta(object):
        """Wagtail properties."""
        icon = 'image'
        label = 'Image Grid'


class LinkedImageBlock(blocks.StructBlock):
    """"""
    image = ImageChooserBlock(required=True)
    link = LinkBlock(required=True)

    class Meta(object):
        """Wagtail properties."""
        template = 'blocks/linked_image_block.html'


class LinkedImageGridBlock(ListBlock):
    """Block for displaying a grid of linked images."""
    def __init__(self, **kwargs):
        """
        Instantiates an LinkedImageBlock instances,
        then passes them to the super class for list rendering.

        :param kwargs: Default keyword args
        :type kwargs: {}
        """
        child_block = LinkedImageBlock(required=True)
        super(LinkedImageGridBlock, self).__init__(child_block, **kwargs)

    class Meta(object):
        """Wagtail properties."""
        icon = 'image'
        label = 'Linked Image Grid'


class ULBlock(ListBlock):
    """Block for displaying an unordered of rich text."""
    def __init__(self, **kwargs):
        """
        Instantiates an RichTextBlock instance,
        then passes it to the super class for list rendering.

        :param kwargs: Default keyword args
        :type kwargs: {}
        """
        child_block = blocks.CharBlock(required=True)
        super(ULBlock, self).__init__(child_block, **kwargs)

    class Meta(object):
        """Wagtail properties."""
        icon = 'list-ul'
        label = 'Unordered List'


class OLBlock(ULBlock):
    """Block for displaying an ordered of rich text."""
    def render_basic(self, value, context=None):
        children = format_html_join(
            '\n', '<li>{0}</li>',
            [(self.child_block.render(
                child_value,
                context=context
            ),) for child_value in value]
        )
        return format_html("<ol>{0}</ol>", children)

    class Meta(object):
        """Wagtail properties."""
        icon = 'list-ol'
        label = 'Ordered List'


class PullQuoteBlock(blocks.CharBlock):
    """ """
    def render(self, value):
        """
        Renders the block contents and returns them as a safe string.

        :param value: The value from the database to render
        :return: Safe String - Rendered block content
        """
        return mark_safe(
            '<aside class="{pq}"><{bq}><p>{contents}</p></{bq}></aside>'.format(
                pq='pquote',
                bq='blockquote',
                contents=self.render_basic(value),
            )
        )

    class Meta(object):
        """Wagtail properties."""
        icon = 'openquote'
        label = 'Pull Quote'


class BodyStreamBlock(blocks.StreamBlock):
    """Stream block for the body field on all pages."""
    basic_card = BasicCardBlock()
    block_quote = blocks.BlockQuoteBlock()
    google_map = GoogleMapBlock()
    h1 = HBlock(tag='h1')
    h2 = HBlock(tag='h2')
    h3 = HBlock(tag='h3')
    h4 = HBlock(tag='h4')
    image = ImageChooserBlock()
    image_grid = ImageGridBlock()
    linked_image_grid = LinkedImageGridBlock()
    ordered_list = OLBlock()
    paragraph = blocks.RichTextBlock()
    pull_quote = PullQuoteBlock()
    raw_html = RawHTMLBlock()
    related_page = blocks.PageChooserBlock(icon='doc-empty-inverse')
    table = TableBlock()
    two_column = TwoColumnBlock()
    unordered_list = ULBlock()
