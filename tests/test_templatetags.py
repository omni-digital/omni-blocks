from __future__ import unicode_literals

from mock import Mock

from django.test import TestCase
from wagtail_factories import PageFactory

from omni_blocks.blocks.text_blocks import JumpHBlock
from omni_blocks.templatetags.omni_blocks_tags import has_jumplist, get_jumplist


class TestHasJumplist(TestCase):
    def setUp(self):
        self.page = PageFactory.create(title="Page", parent=None)

    def test_jumplist_does_not_exists(self):
        """has_jumplist should return `False` if no JumpHBlock exists."""
        self.assertFalse(has_jumplist(self.page, "body"))

    def test_jumplist_exists(self):
        """Ensure has_jumplist returns `True` when a JumpHBlock exists."""
        field = Mock(block=JumpHBlock(tag="h2"))
        self.page.body = [field]

        self.assertTrue(has_jumplist(self.page, "body"))


class TestGetJumplist(TestCase):
    def setUp(self):
        self.page = PageFactory.create(title="Page", parent=None)

    def test_no_jumplist_exists(self):
        """Ensure get_jumplist returns an empty list if no JumpHBlock exists."""
        result = get_jumplist(self.page, "body")
        self.assertEqual(len(result), 0)

    def test_jumplist_exists(self):
        """Ensure get_jumplist returns the JumpHBlocks."""
        field = Mock(block=JumpHBlock(tag="h2"))
        self.page.body = [field, field, field]
        result = get_jumplist(self.page, "body")

        self.assertEqual(len(result), 3)
