===
ctx
===

ctx - A minimal but opinionated dict/object combo (like Bunch).

.. image:: https://travis-ci.org/figlief/ctx.png?branch=master
        :target: https://travis-ci.org/figlief/ctx

.. contents::
   :backlinks: none

Requirements
------------
The ctx module should work with  all versions of Python.

Features
--------

The ctx module provides the `Ctx` class which is a subclass of
the python 'dict' object.

    Ctx modifies 'dict' in the following ways:

        1  The dictionary items can be read or set using attribute
        access notation.

            'ctx.a' is identical to 'ctx["a"]' and
            'ctx.a = 5' is identical to 'ctx["a"] = 5'

        2  The objects attributes can be read using item access notation.

            'ctx["__doc__"]' is identical to 'ctx.__doc__'

        3  The objects attributes can not be set under any circumstances.

        4  The dictionary can not have a key with the same name as an
        objects attribute.


    'ctx.name' and 'ctx["name"]' are resolved using the following three steps.

        a)  if the object has an attribute 'name' then return the attribute.

        b)  if the dictionary has a key 'name' then return the value
        associated with the key.

        c)  raise LookupError.


    'ctx.name = 5' and 'ctx["name"] = 5'

        a) If name is an attribute of the class then raise AttributeError.

        b) set the dictionary item as usual.


Installation
------------
You can install this package using pip with the following command. ::

    pip install ctx


Support
-------
To report any bugs, or ask any question, please visit ::

    https://github.com/figlief/ctx/issues.


Resources
---------
Here is a list of useful links about this project.

- `Latest release on PyPI <https://pypi.python.org/pypi/ctx>`_
- `Source code on GitHub <https://github.com/figlief/ctx>`_
- `Issue tracker on GitHub <https://github.com/figlief/ctx/issues>`_
- `Changelog on GitHub <https://github.com/figlief/ctx/blob/master/History.rst>`


