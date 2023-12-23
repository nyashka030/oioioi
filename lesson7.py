my_list = [1, 2, 3, 4]
for i in my_list:
    print(i)

# iterator = iter(my_list)
# print(iterator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))  # StopIteration
# for i in iterator:
#    print(i)
# for i in iterator:
#     print(i)

class Counter:

    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i


count = Counter(5)
print(count.__next__())
print(next(count))
print(iter(count))
print(next(count))

for elem in count:
    print(elem)


def raise_to(number):
    i = 0
    while True:
        result = number ** i
        yield result
        if result > 100 ** 20:
            return
        i += 1

r = raise_to(12345)
print(r)
for _ in r:
    print(_)





def checker(*ex_types):
    def checker(func):
        def wrap(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except (ex_types) as err:
                print(f'We have problems: {err}')
            else:
                print(f'No problems. \n Result - {result}')

        return wrap


@checker(ZeroDivisionError, TypeError, SyntaxError)
def calculate(expression):
    return eval(expression)

checker('2/0')