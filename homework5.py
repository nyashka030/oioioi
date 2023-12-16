
import colorama

def my_func():
    pass

class Human:
    pass

class Worker:
    pass
x = my_func
nick = Human

print("Atreb..:")
for attr_name in dir(colorama):
    print(f" - {attr_name}")

print("\nMetodick:")
for attr_name in dir(colorama):
    attr = getattr(colorama, attr_name)
    if callable(attr):
        print(f" - {attr_name}")

print(colorama.__name__)
print(my_func.__name__)
print(x.__name__)
print(Human.__name__)
print(nick.__name__)
print(__name__)

print(type(colorama))

for method in dir():
    print(method)
print(list(dir()))

l = list
print(hasattr(l, 'append'))
print(hasattr(l, 'split'))
print(getattr(l, 'split', None))
print(getattr(l, 'append'))

print(callable(my_func))
print(callable(l))

print(issubclass(Human, Worker))
print(issubclass(Worker, Human))

print(isinstance('Hello', str))
print(isinstance('Hello', int))

import inspect

print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
print(inspect.isfunction(colorama))

print(inspect.getmodule(colorama))
print(inspect.getmodule(list))

import  sys

print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)
for mn, mp in sys.modules.items():
    print(mn, mp)

print(dir(__builtins__))

