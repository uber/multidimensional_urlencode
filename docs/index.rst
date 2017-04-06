.. multidimensional_urlencode documentation master file, created by
   sphinx-quickstart on Tue Sep 10 09:55:53 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to multidimensional_urlencode's documentation!
======================================================

Contents:

.. toctree::
   :maxdepth: 2


Quick Start
===========

multidimensional_urlencode lets you url encode a multidimensional dict:

.. code-block:: python

    >>> try:
    ...     from urllib.parse import unquote
    ... except:
    ...     from urllib import unquote
    >>> from multidimensional_urlencode import urlencode
    >>> e = urlencode({"a": {"b": {"c": [1, 2, 3], "d": "e"}}})
    >>> unquote(e)
    'a[b][c][]=1&a[b][c][]=2&a[b][c][]=3&a[b][d]=e'

Development
===========

Install requirements::

    $ pip install -r requirements-dev.txt

Run tests::

    $ py.test
    $ # or
    $ tox


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
