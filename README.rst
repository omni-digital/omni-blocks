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
