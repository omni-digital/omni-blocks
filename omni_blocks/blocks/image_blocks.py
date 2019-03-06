from __future__ import unicode_literals

from wagtail.core.blocks import StructBlock
from wagtail.core.blocks.list_block import ListBlock
from wagtail.images.blocks import ImageChooserBlock

from omni_blocks.blocks.struct_blocks import LinkBlock


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

        icon = "image"
        label = "Image Grid"
        template = "blocks/image_grid_block.html"


class LinkedImageBlock(StructBlock):
    """Image block wrapped by a href link."""

    image = ImageChooserBlock(required=True)
    link = LinkBlock(required=True)

    class Meta(object):
        """Wagtail properties."""

        template = "blocks/linked_image_block.html"


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

        icon = "image"
        label = "Linked Image Grid"
        template = "blocks/linked_image_grid_block.html"
