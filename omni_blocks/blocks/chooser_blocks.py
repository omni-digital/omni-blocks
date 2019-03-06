from __future__ import unicode_literals

from django.template.loader import render_to_string
from wagtail.core.blocks import PageChooserBlock


class PageChooserTemplateBlock(PageChooserBlock):
    """Page chooser block that renders from a template."""

    template = "blocks/page_chooser_block.html"

    def render_basic(self, value, context=None):
        """Override render_basic to use provided template."""
        if value:
            return render_to_string(self.template, {"page": value})
        else:
            return ""
