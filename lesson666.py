
"""
try:
    <code with possible error>
except <Error or tuple of errors>:
    <code executed is case of error>
else:    - optional
    <code executed in case of no errors>
finally: - optional
    <code executed whether is an error>


except NameError:
except (ValueError, NameError):


try:
    <code with possible error>
except NameError:
    <code executed is case of error>
except ValueError:
    <code executed is case of error>
"""


try:
    print(10/0)
except ZeroDivisionError:
    print('we have an errors')

try:
    print(10/2)
except ZeroDivisionError:
    print('we have an errors')
else:
    print('WE HAVE NO ERRORS')
finally:
    print('Code is a loh, Code that exactly runs')

print('=============================')

try:
    print(10/0)
except ZeroDivisionError:
    print('we have an errors')
else:
    print('WE HAVE NO ERRORS')
finally:
    print('Code is a loh, Code that exactly runs')


def checker(value):
    if not isinstance(value, str):
        raise TypeError(
            f'Sorry, we can not work with {type(value)}, we need str'
        )
    else:
        print(value)

x = "10"
checker(x)


class BiuldError(Exception):

    def __str__(self):
        return 'Not enough materials. We cannot build the house'


def check_materials(value, limit=300):

    if value > limit:
        return 'enough materials'
    else:
        raise BiuldError

our_materials = 301
check_materials(our_materials)


import warnings

warnings.simplefilter('ignore', SyntaxWarning)
warnings.simplefilter('always', ImportWarning)

warnings.warn('NO code here', SyntaxWarning)
try:
    warnings.warn('NO module here', ImportWarning)
except:
    print('Error was processed')

warnings.warn('No module here', ImportWarning)

