import sys

result = []

class CustomError(Exception):
    pass

class AnotherError(Exception):
    pass

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a should be greater than or equal to b")
        if b == 0:
            raise ZeroDivisionError("b should not be zero")
        if b > 100:
            raise IndexError("b should be less than or equal to 100")

        if isinstance(a, str):
            raise CustomError("a should be an integer, not a string")

        if a % 2 == 0:
            raise AnotherError("a should be an odd number")

        return a / b
    except (ValueError, ZeroDivisionError, IndexError, CustomError, AnotherError) as e:
        print(f"Error: {e} for a={a}, b={b}")
        sys.exit(1)


data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4, 9: 3}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, ZeroDivisionError, IndexError, CustomError, AnotherError):
        pass

print(result)
sys.exit(0)