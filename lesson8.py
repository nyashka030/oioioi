

# if 2 + 2 == 4:
#   print('yeah')

# assert 2 + 2 == 5, 'it is wrong'


# """
# >>> 2 + 57
# 54
# >>> 2 + 2
# 5
# """

# if __name__ == '__main__':
#   import doctest
#    doctest.testmod()

def checker(value):

    try:
        value = int(value)
    except (ValueError, TypeError):
         value = 0

    return value





def adder(*args, **kwargs):
    res = 0
    for _ in args:
        if isinstance(_, int) or (_, bool) or isinstance(_, float):
            res += _
        else:
            res += checker(value=_)
            continue
    for _ in kwargs.values():
        if isinstance(_, int) or isinstance(_, bool) or isinstance(_, float):
            res += _
        else:
            res += checker(value=_)

    return res