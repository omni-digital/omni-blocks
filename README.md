# Omni Blocks
![](https://badge.fury.io/py/omni_blocks.svg)
![](https://travis-ci.org/omni-digital/omni-blocks.svg?branch=master)
![](https://codecov.io/gh/omni-digital/omni-blocks/branch/master/graph/badge.svg)


A collection of common implementations for use with wagtail's block framework.

## Quickstart

### Install Omni Blocks:

```bash
pip install omni_blocks
```

### Add it to your `INSTALLED_APPS`:

```python
    INSTALLED_APPS = [
        ...
        'wagtail.contrib.table_block',
        'omni_blocks',
        ...
    ]
```

## Blocks

### HBlock
A block for adding headings, the tag is defined when the HBlock is instantiated and is a required. This block is not limited to the "h" element and can be used for any text-based content.

```python
from omni_blocks import HBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    h1 = HBlock(tags='h1')
    h2 = HBlock(tags='h2')
    h3 = HBlock(tags='h3')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]
```

### JumpHBlock
A block that adds navigation locally within the page. The block requires a tag is defined, like `HBlock` this tag can take the form of any text-based HTML element. This block *must* be used in tandem with the `has_jumplist` & `get_jumplist` template tags.

```python
from omni_blocks import JumpHBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""

     jump_h2 = JumpHBlock(tags='h2')
     jump_h3 = JumpHBlock(tags='h3')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]

```

### PullQuoteBlock
A block for adding pull quotes within a page's content. The block is rendered in an HTML template located at `block/pull_quote_block.html`.  This template can be overridden by either parsing the kwarg template with the new template's location as the value or adding your own template into your local project, the local template's location *must* match the location of the template within `omni-blocks`.

```python
from omni_blocks import PullQuoteBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    pull_quote = PullQuoteBlock()
    custom_pull_quote = PullQuoteBlock(template='path/to/custom/template.html')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]

```

### QuoteBlock
A block for adding quotes within a page's content. The block is rendered in an HTML template located at `block/quote_block.html`.  This template can be overridden by either parsing the kwarg template with the new template's location as the value or adding your own template into your local project, the local template's location *must* match the location of the template within `omni-blocks`.

```python
from omni_blocks import QuoteBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    quote = QuoteBlock()
    custom_quote = QuoteBlock(template='path/to/custom/template.html')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]

```

### PageChooserTemplateBlock
A modified version of the core wagtail `PageChooserBlock`, that renders the link in a HTML template allowing custom styles to be added into the link's markup. The HTML template located at `block/page_chooser_block.html`.  This template can be overridden by either parsing the kwarg template with the new template's location as the value or adding your own template into your local project, the local template's location *must* match the location of the template within `omni-blocks`.

```python
from omni_blocks import PageChooserTemplateBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    related_page = PageChooserTemplateBlock()
    custom_related_page = PageChooserTemplateBlock(template='/path/to/custom/template.html')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]

```

### ImageGridBlock
A block that can contain multiple wagtail image objects, these images are rendered into a HTML template in an unordered list. The HTML template located at `block/image_grid_block.html`.  This template can be overridden by either parsing the kwarg template with the new template's location as the value or adding your own template into your local project, the local template's location *must* match the location of the template within `omni-blocks`.

```python
from omni_blocks import ImageGridBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    image_grid = ImageGridBlock()
    custom_image_grid = ImageGridBlock(template='/path/to/custom/template.html')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]
```

### LinkedImageBlock
A block that contains a wagtail image object and a link, the link can either be a page object or a URL. The blocks content is rendered into a HTML template allowing custom style to be applied. The HTML template located at `block/image_grid_block.html`.  This template can be overridden by either parsing the kwarg template with the new template's location as the value or adding your own template into your local project, the local template's location *must* match the location of the template within `omni-blocks`.

```python
from omni_blocks import LinkedImageBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    linked_image = LinkedImageBlock()
    custom_linked_image = LinkedImageBlock(template='/path/to/custom/template.html')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]
```

### LinkedImageGridBlock
A block that can contain multiple `LinkedImageBlocks`, these images are rendered into a HTML template in an unordered list. The HTML template located at `block/linked_image_grid_block.html`.  This template can be overridden by either parsing the kwarg template with the new template's location as the value or adding your own template into your local project, the local template's location *must* match the location of the template within `omni-blocks`.

```python
from omni_blocks import LinkedImageGridBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    linked_image = LinkedImageGridBlock()
    custom_linked_image = LinkedImageGridBlock(template='/path/to/custom/template.html')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]
```

### BasicCardGridBlock
A block that can contain multiple `BasicCardBlock`s, these card blocks are rendered into a HTML template in an unordered list. The HTML template located at `block/basic_card_grid_block.html`.  This template can be overridden by either parsing the kwarg template with the new template's location as the value or adding your own template into your local project, the local template's location *must* match the location of the template within `omni-blocks`.

```python
from omni_blocks import BasicCardGridBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    card_grid = BasicCardGridBlock()
    custom_card_grid = BasicCardGridBlock(template='/path/to/custom/template.html')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]
```

### FlowListBlock
The `FlowListBlock` is designed to display ordered data in a linear fashion. The `FlowListBlock` can contain multiple `FlowBlock` instances, the content is rendered into a HTML template in an unordered list. The HTML template located at `block/flow_list_block.html`. This template can be overridden by either parsing the kwarg template with the new template's location as the value or adding your own template into your local project, the local template's location *must* match the location of the template within `omni-blocks`.

```python
from omni_blocks import FlowListBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    flow_list = FlowListBlock()
    custom_flow_list = FlowListBlock(template='/path/to/custom/template.html')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]
```

### ULBlock
The `ULBlock` is a block implementation of an unordered list, this block can only contain text-based content. The `ULBlock` is rendered in python and does *not* have a HTML template.

```python
from omni_blocks import ULBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    unordered_list = ULBlock()
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]
```

### OLBlock
The `OLBlock` is a block implementation of an ordered list, this block can only contain text-based content. The `ULBlock` is rendered in python and does *not* have a HTML template.

```python
from omni_blocks import OLBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    ordered_list = OLBlock()
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]
```

### LinkBlock
The `LinkBlock` is a block implementation of an anchor tag. The `LinkBlock` can contain either a page instance or a URL, the content is rendered into a HTML template. The HTML template located at `block/link_block.html`. This template can be overridden by either parsing the kwarg template with the new template's location as the value or adding your own template into your local project, the local template's location *must* match the location of the template within `omni-blocks`.

```python
from omni_blocks import LinkBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    link = LinkBlock()
    custom_link = LinkBlock(template='path/to/custom/template.html')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]
```

### TitledLinkBlock
The `TitledLinkBlock` is an implementation of  `LinkBlock`. The `TitledLinkBlock` adds a title that is wrapped by an anchor. The HTML template located at `block/titled_link_block.html`. This template can be overridden by either parsing the kwarg template with the new template's location as the value or adding your own template into your local project, the local template's location *must* match the location of the template within `omni-blocks`.

```python
from omni_blocks import TiltedLinkBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    titled_link = TitledLinkBlock()
    custom_titled_link = TitledLinkBlock(template='path/to/custom/template.html')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]
```

### BasicCardBlock
The `BasicCardBlock` is a block implementation of the [Google material card](https://material.io/design/components/cards.html). The `BasicCardBlock` *must* contain a title it can additionally contain an image, link, and description. The HTML template located at `block/basic_card_block.html`. This template can be overridden by either parsing the kwarg template with the new template's location as the value or adding your own template into your local project, the local template's location *must* match the location of the template within `omni-blocks`.

```python
from omni_blocks import BasicCardBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    card = BasicCardBlock()
    custom_card = BasicCardBlock(template='path/to/custom/template.html')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]
```

### ButtonBlock
The `ButtonBlock` is a block implementation of `TitledLinkBlock`. The HTML template located at `block/basic_card_block.html`. This template can be overridden by either parsing the kwarg template with the new template's location as the value or adding your own template into your local project, the local template's location *must* match the location of the template within `omni-blocks`.

```python
from omni_blocks import ButtonBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    button = ButtonBlock()
    custom_button = ButtonBlock(template='path/to/custom/template.html')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]
```

### GoogleMapBlock
The `GoogleMapBlock` is a block implementation of an embed google map. The HTML template located at `block/google_map_block.html`. This template can be overridden by either parsing the kwarg template with the new template's location as the value or adding your own template into your local project, the local template's location *must* match the location of the template within `omni-blocks`.

```python
from omni_blocks import GoogleMapBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    google_map = GoogleMapBlock()
    custom_map = GoogleMapBlock(template='path/to/custom/template.html')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]
```

### TwoColumnBlock
The `TwoColumnBlock` is designed to display content in two distinct columns (left & right). Each column can display either an image or a text item, the HTML template is located at `blocks/two_column_block.html`. This template can be overridden by either parsing the kwarg template with the new template's location as the value or adding your own template into your local project, the local template's location *must* match the location of the template within `omni-blocks`.

```python
from omni_blocks import TwoColumnBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.model import Page
from wagtail.wagtailsearch.index import SearchField

...


class MyPageStreamBlock(StreamBlock):
    """A implementation of wagtail.StreamBlock for the `MyPage` model."""
    ...
    two_column = TwoColumnBlock()
    custom_two_column = TwoColumnBlock(template='path/to/custom/template.html')
    ...


class MyPage(Page)
    """My Page model."""

    body = StreamField(
        MyPageStreamBlock(required=False),
        blank=True,
        null=True,
        help_text='The main content of my page.'
    )

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    search_fields = Page.search_fields + [SearchField('body')]
```

## Running the tests.

```python
    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox
```

## Supported Versions

### Wagtail

* 1.11
* 1.12 LTS

### Django

* 1.10
* 1.11 LTS

# By [Omni Digital](omni-digital.co.uk)
