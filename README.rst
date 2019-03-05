=============================
Omni Blocks
=============================

.. image:: https://badge.fury.io/py/omni_blocks.svg
    :target: https://badge.fury.io/py/omni_blocks

.. image:: https://travis-ci.org/omni-digital/omni-blocks.svg?branch=master
    :target: https://travis-ci.org/omni-digital/omni-blocks

.. image:: https://codecov.io/gh/omni-digital/omni-blocks/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/omni-digital/omni-blocks

A useful collection of wagtail blocks.

Quickstart
----------

Install Omni Blocks::

    pip install omni_blocks

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'wagtail.contrib.table_block',
        'omni_blocks',
        ...
    )

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Supported Versions
------------------

omni-blocks 3.x
~~~~~~~~~~~~~~~

Python: 3.6

Django: 2.0, 2.1

Wagtail: 2.1, 2.2, 2.3, 2.4


omni-blocks 2.0.4
~~~~~~~~~~~~~~~~~

Python: 2.7, 3.4, 3.5, 3.6

Django:1.10, 1.11

Wagtail: 1.11, 1.12
