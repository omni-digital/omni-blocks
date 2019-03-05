from __future__ import unicode_literals

from collections import namedtuple

from django import template

from omni_blocks.blocks.text_blocks import JumpHBlock


register = template.Library()


Anchor = namedtuple("Anchor", ["value", "href"])


@register.simple_tag
def has_jumplist(calling_page, field):
    """
    Determine if one or more JumpHBlocks exist within a streamfield.

    :param page: The Page object that contains a streamfield.
    :param field: A streamfield that may contain one or more JumpHBlock.
    :return: Boolean - Returns `True` if JumpHBlock is within the field.
    """
    body = getattr(calling_page, field, [])
    return any(isinstance(item.block, JumpHBlock) for item in body)


@register.simple_tag
def get_jumplist(calling_page, field):
    """
    Gets all JumpHBlocks from a given streamfield and loads them into an array.
    Used in base.html to render a jumplist for navigation around the page.

    :param page: The Page object that contains a streamfield.
    :param field: A streamfield that may contain one or more JumpHBlock.
    :return: List - Returns a list of JumpHBlock instances.
    """
    anchors = []
    body = getattr(calling_page, field, [])
    for item in body:
        if isinstance(item.block, JumpHBlock):
            anchors.append(
                Anchor(
                    value=item.value,
                    href="#{}".format(JumpHBlock.make_jump_link(item.value)),
                )
            )
    return anchors
