# var = ""
# var.join("24")
# print(dir(var))
#
# for method in dir(var):
#     print(method)
#
# print(hasattr(var, "find"))
#
# def first_func():
#     pass
# print(callable(var), callable(first_func))
#
# class Class1():
#     pass
#
# class Class2(Class1):
#     pass
#
# print(issubclass(Class2, Class1))
# print(issubclass(Class1, Class2))
#
import inspect
import random
from inspect import getmodule

print(inspect.ismodule(random))
print(inspect.isclass(random))
print(getmodule(random))

class Human:
    def __init__(self, age, height, name="John"):
        self.age = age
        self.height = height
        self.name = name
        self.secondname = "Wich"

import sys
print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)
print(sys.modules)
