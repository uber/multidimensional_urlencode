from unittest import TestCase

from multidimensional_urlencode import urlencode


class TestUrlEncode(TestCase):

    def test_basic(self):
        """Verify that urlencode works with four levels."""
        d = {"a": {"b": {"c": "d"}}}
        expected = "a[b][c]=d"
        self.assertEqual(urlencode(d), expected)

    def test_two(self):
        """Verify that urlencode works with two params."""
        d = {'a': 'b', 'c': {'d': 'e'}}
        expected = "a=b&c[d]=e"
        self.assertEqual(urlencode(d), expected)
