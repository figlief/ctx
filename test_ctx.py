import pytest
from ctx import Ctx


def test_init():
    p = {}
    q = {}

    x = Ctx(a=p, b=q)
    assert x['a'] is p
    assert x.a is p
    assert x['b'] is q
    assert x.b is q


def test_item():
    p = {}
    x = Ctx()
    x['a'] = p
    assert x.a is p
    assert x['a'] is p


def test_attr():

    p = {}
    x = Ctx()
    x.a = p
    assert x.a is p
    assert x['a'] is p


def test_init_copy():
    p = {}
    q = {}

    x = Ctx(a=p, b=q)
    y = x.copy()
    assert x is not y
    assert y['a'] is p
    assert y.a is p
    assert y['b'] is q
    assert y.b is q


if __name__ == '__main__':
    pytest.main()
