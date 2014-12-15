# -*- coding: utf-8 -*-

__author__ = 'Robert Ledger'
__email__ = 'figlief@figlief.com'
__version__ = '0.1.0'

class Ctx(dict):
    """
    A minimal but opinionated dict/object combo (like Bunch).

    Setting an attribute is the same as setting an item.

    So 'ctx.a = 5' is the same as 'ctx["a"] = 5'.

    Getting an attribute is the sameas getting an item.

    So 'x = ctx.a' is the same as 'x = ctx["a"]'

    When getting a value, attributes have priority over dictionary items.

    So 'ctx.copy and ctx["copy'] both return the 'copy' method for the class.

    When setting a value, attrnbutes again have priority.

    But Ctx does not allow attributesto be set.

    So 'ctx.copy = 5' and 'ctx["copy"] = 5' both result in an AttributeError with a message  saying that attrbute copy is read only.

    """

    def copy(self):
        return self.__class__(self)

    def __getattr__(self, k):

        try:
            return object.__getattribute__(self, k)
        except AttributeError:
            return dict.__getitem__(self, k)

    __getitem__ = __getattr__

    def __setattr__(self, k, v):

        try:
            (object.__getattribute__(self, k))
        except AttributeError:
            dict.__setitem__(self, k, v)
            return

        raise AttributeError('Attribute "%s" is read only' % k)

    __setitem__ = __setattr__

    def __repr__(self):
        return "%s(%s)" % (
            self.__class__.__name__,
            dict.__repr__(self)
        )
