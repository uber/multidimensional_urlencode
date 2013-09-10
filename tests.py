import urllib
from unittest import TestCase

from multidimensional_urlencode import urlencode


class TestUrlEncode(TestCase):

    def test_basic(self):
        """Verify that urlencode works with four levels."""
        d = {"a": {"b": {"c": "d"}}}
        expected = urllib.quote("a[b][c]=d", safe="=/&")
        self.assertEqual(urlencode(d), expected)

    def test_two(self):
        """Verify that urlencode works with two params."""
        d = {'a': 'b', 'c': {'d': 'e'}}
        expected = urllib.quote("a=b&c[d]=e", safe="=/&")
        self.assertEqual(urlencode(d), expected)

    def test_with_list_value(self):
        """Verify that urlencode works with list value."""
        d = {'a': {"b": [1, 2, 3]}}
        expected = urllib.quote("a[b]=1&a[b]=2&a[b]=3", safe="=/&")
        self.assertEqual(urlencode(d), expected)
