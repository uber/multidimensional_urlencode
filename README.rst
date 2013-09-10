multidimensional_urlencode
==========================

Python library to urlencode a multidimensional dict

Quick Start
===========

multidimensional_urlencode lets you url encode a multidimensional dict:

.. code-block:: python

    >>> import urllib
    >>> from multidimensional_urlencode import urlencode
    >>> e = urlencode({"a": {"b": {"c": [1, 2, 3], "d": "e"}}})
    >>> urllib.unquote(e)
    'a[b][d]=e&a[b][c]=1&a[b][c]=2&a[b][c]=3'

Documentation
=============
