import urllib

from multidimensional_urlencode import urlencode


def test_basic():
    """Verify that urlencode works with four levels."""
    d = {"a": {"b": {"c": "d"}}}
    expected = urllib.quote("a[b][c]=d", safe="=/&")
    assert urlencode(d) == expected


def test_two():
    """Verify that urlencode works with two params."""
    d = {'a': 'b', 'c': {'d': 'e'}}
    expected = urllib.quote("a=b&c[d]=e", safe="=/&")
    assert urlencode(d) == expected


def test_with_list_value():
    """Verify that urlencode works with list value."""
    d = {'a': {"b": [1, 2, 3]}}
    expected = urllib.quote("a[b]=1&a[b]=2&a[b]=3", safe="=/&")
    assert urlencode(d) == expected
