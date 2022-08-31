# -*- coding: utf-8 -*-
"""
Time:2022/8/29 13:10
Author:CAOZHENG
File:decorator.py
"""

import functools
import time

"""
 @value_dispatch
def get_direction(direction):
    return 'Direction not defined'

@get_direction.register('x')
def test(direction):
            
argparse.ArgumentParser
"""


def value_dispatch(func):
    """
    装饰器：代替 if else
    """
    registry = {}

    @functools.wraps(func)
    def wrapper(arg0, *args, **kwargs):
        try:
            delegate = registry[arg0]
        except KeyError:
            pass
        else:
            return delegate(arg0, *args, **kwargs)

        return func(arg0, *args, **kwargs)

    def register(value):
        def wrap(func):
            if value in registry:
                raise ValueError(
                    f'@value_dispatch: there is already a handler '
                    f'registered for {value!r}'
                )
            registry[value] = func
            return func

        return wrap

    wrapper.register = register
    return wrapper


def filter_error(func):
    """
    装饰器：在函数执行前添加时间戳

    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        try:
            print("------------------%s------------------" % time.strftime("%Y-%m-%d %H:%M:%S"))
            func(*args, **kwargs)
        except Exception:
            pass

    return wrapper

