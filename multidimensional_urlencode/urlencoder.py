try:
    from urllib.parse import urlencode as urllib_urlencode
except ImportError:
    from urllib import urlencode as urllib_urlencode

from collections import OrderedDict


def flatten(d, encode_list_key=False):
    """Return a dict as a list of lists.

    >>> flatten({"a": "b"})
    [['a', 'b']]
    >>> flatten({"a": [1, 2, 3]})
    [['a', [1, 2, 3]]]
    >>> flatten({"a": {"b": "c"}})
    [['a', 'b', 'c']]
    >>> flatten({"a": {"b": {"c": "e"}}})
    [['a', 'b', 'c', 'e']]
    >>> flatten({"a": {"b": "c", "d": "e"}})
    [['a', 'b', 'c'], ['a', 'd', 'e']]
    >>> flatten({"a": {"b": "c", "d": "e"}, "b": {"c": "d"}})
    [['a', 'b', 'c'], ['a', 'd', 'e'], ['b', 'c', 'd']]
    """

    if isinstance(d, dict) or (encode_list_key and isinstance(d, list)):
        returned = []

        if isinstance(d, list) and encode_list_key:
            inner = [(x, d[x]) for x in range(len(d))]
        else:
            inner = sorted(d.items())

        for key, value in inner:
            # Each key, value is treated as a row.
            nested = flatten(value, encode_list_key)
            for nest in nested:
                current_row = [key]
                current_row.extend(nest)
                returned.append(current_row)

        return returned
    else:
        return [[d]]


def parametrize(params):
    """Return list of params as params.

    >>> parametrize(['a'])
    'a'
    >>> parametrize(['a', 'b'])
    'a[b]'
    >>> parametrize(['a', 'b', 'c'])
    'a[b][c]'

    """
    returned = str(params[0])
    returned += "".join("[" + str(p) + "]" for p in params[1:])
    return returned


def urlencode(params, encode_list_key=False, array_braces=True):
    """Urlencode a multidimensional dict.

    >>> try:
    ...     from urllib.parse import quote, unquote
    ... except ImportError:
    ...     from urllib import quote, unquote
    ...
    >>> unquote(urlencode({'a': {"b": [1, 2, 3]}}))
    'a[b][]=1&a[b][]=2&a[b][]=3'
    >>> unquote(urlencode({'a': {"b": [1, 2, 3]}}, array_braces=False))
    'a[b]=1&a[b]=2&a[b]=3'
    >>> unquote(urlencode({'a': {"b": [1, 2, 3]}}, encode_list_key=True))
    'a[b][0]=1&a[b][1]=2&a[b][2]=3'

    """

    # Not doing duck typing here. Will make debugging easier.
    if not isinstance(params, dict):
        raise TypeError("Only dicts are supported.")

    params = flatten(params, encode_list_key)

    url_params = OrderedDict()
    for param in params:
        value = param.pop()

        name = parametrize(param)
        if isinstance(value, (list, tuple)) and array_braces:
            name += "[]"

        url_params[name] = value

    return urllib_urlencode(url_params, doseq=True)
