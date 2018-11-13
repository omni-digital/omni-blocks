from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks.field_block import URLBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from omni_blocks.blocks.text_blocks import HBlock


class LinkBlock(blocks.StructBlock):
    """Block for adding links.

    If required is set to false, we assume that a link does not need to be present.
    """
    external_url = URLBlock(required=False)
    internal_url = blocks.PageChooserBlock(icon='doc-empty-inverse', required=False)

    both_urls_error = _('Please select either internal URL or external URL; not both.')
    no_urls_error = _('Please select an internal URL or add an external URL.')

    def __init__(self, **kwargs):
        """Override init to retrieve required value.

        StructBlock does not have a "required" value in WagtailCore.
        """
        required = kwargs.pop('required', True)
        super(LinkBlock, self).__init__(**kwargs)
        self._required = required

    @property
    def required(self):
        """Override base block required function to return our custom kwarg.

        The StructBlock class in wagtail has no logic for what is "required",
        as such we must override the method in the base Block class.

        https://github.com/wagtail/wagtail/blob/master/wagtail/core/blocks/base.py#L315
        """
        return self._required

    def clean(self, value):
        cleaned_data = super(LinkBlock, self).clean(value)
        errors = {}
        if cleaned_data.get('external_url') and cleaned_data.get('internal_url'):
            msg = self.both_urls_error
            errors['external_url'] = errors['internal_url'] = ValidationError(msg)

        if self.required:
            if not cleaned_data.get('external_url') and not cleaned_data.get('internal_url'):
                msg = self.no_urls_error
                errors['external_url'] = errors['internal_url'] = ValidationError(msg)

        if errors:
            raise ValidationError(msg, params=errors)

        return cleaned_data

    def render(self, value, context=None):
        """Override the render to get around the above dunder string issue."""
        rendered = super(LinkBlock, self).render(value, context=context)
        return rendered.strip()

    class Meta:
        """Wagtail properties."""
        label = 'Link'
        template = 'blocks/link_block.html'


class TitledLinkBlock(blocks.StructBlock):
    """Link block with a title."""
    title = blocks.CharBlock(required=True)
    link = LinkBlock(required=True)

    class Meta(object):
        """Wagtail properties."""
        icon = ''
        label = 'Link'
        template = 'blocks/titled_link_block.html'


class BasicCardBlock(blocks.StructBlock):
    """A basic card block."""
    title = HBlock(tag='h2')
    image = ImageChooserBlock(required=False)
    link = LinkBlock(required=False)
    description = blocks.TextBlock(required=False)

    class Meta(object):
        """Wagtail properties."""
        template = 'blocks/basic_card_block.html'
        icon = 'form'
        label = 'Basic card'


class ColumnBlock(blocks.StructBlock):
    """Block that can either contain text or an image."""
    image = ImageChooserBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)

    both_fields_error = _('Please add either an image or a paragraph.')
    no_data_error = _('Please use either image or paragraph; not both')

    def clean(self, value):
        cleaned_data = super(ColumnBlock, self).clean(value)
        errors = {}
        if cleaned_data.get('image') and cleaned_data.get('paragraph'):
            msg = self.both_fields_error
            errors['image'] = errors['paragraph'] = ValidationError(msg)

        if not cleaned_data.get('image') and not cleaned_data.get('paragraph'):
            msg = self.no_data_error
            errors['image'] = errors['paragraph'] = ValidationError(msg)

        if errors:
            raise ValidationError(msg, params=errors)

        return cleaned_data


class ButtonBlock(TitledLinkBlock):
    class Meta(object):
        """Wagtail properties."""
        icon = 'placeholder'
        label = 'Button Block'
        template = 'blocks/button_block.html'


class FlowBlock(blocks.StructBlock):
    """Block for displaying flow or timeline data."""
    meta_title = blocks.CharBlock(required=True)
    title = blocks.CharBlock(required=False)
    body = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock(required=False)
    link = LinkBlock(required=False)


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


class TwoColumnBlock(blocks.StructBlock):
    """Two column block."""
    left_column = ColumnBlock(required=True)
    right_column = ColumnBlock(required=True)

    class Meta(object):
        """Wagtail properties."""
        icon = 'form'
        label = 'Two Column'
        template = 'blocks/two_column_block.html'
