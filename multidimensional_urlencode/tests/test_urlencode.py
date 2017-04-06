try:
    from urllib.parse import quote, unquote
except ImportError:
    from urllib import quote, unquote


import pytest

from multidimensional_urlencode import urlencode


def test_basic():
    """Verify that urlencode works with four levels."""
    d = {"a": {"b": {"c": "d"}}}
    expected = quote("a[b][c]=d", safe="=/&")
    assert urlencode(d) == expected


def test_key_types():
    """Verify that urlencode works with key type 'int'."""
    d = {1: {2: {3: 4}}}
    expected = quote("1[2][3]=4", safe="=/&")
    assert urlencode(d) == expected


def test_two():
    """Verify that urlencode works with two params."""
    d = {'a': 'b', 'c': {'d': 'e'}}
    expected = quote("a=b&c[d]=e", safe="=/&")
    assert '&'.join(urlencode(d).split('&')) == expected


def test_with_list_value():
    """Verify that urlencode works with list value."""
    d = {'a': {"b": [1, 2, 3]}}
    expected = "a[b][]=1&a[b][]=2&a[b][]=3"
    assert unquote(urlencode(d)) == expected


def test_with_non_dict():
    """Verify that we raise an exception when passing a non-dict."""
    with pytest.raises(TypeError):
        urlencode("e")
