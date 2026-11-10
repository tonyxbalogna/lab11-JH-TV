import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        return 'a is negative'

def hypotenuse(a,b):
    try:
        return math.hypot(a,b)
    except ValueError:
        return 'a or b is negative'

def add(a,b):
    return a + b

def subtract(a, b):
    return a-b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("a cannot be 0")
    return b/a

def logarithm(a, b):
    if a <= 0:
        raise ValueError("log argument must be positive")
    elif b < 0 or b == 1:
        raise ValueError("log base cant equal one or be negative")
    return math.log(b,a)


def exp(a, b):
    return a**b