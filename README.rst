===============================
ctx
===============================

.. image:: https://badge.fury.io/py/ctx.png
    :target: http://badge.fury.io/py/ctx

.. image:: https://travis-ci.org/figlief/ctx.png?branch=master
        :target: https://travis-ci.org/figlief/ctx

.. image:: https://pypip.in/d/ctx/badge.png
        :target: https://pypi.python.org/pypi/ctx


A minimal but opinionated dict/object combo (like Bunch).

Features
=========

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

