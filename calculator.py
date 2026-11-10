import math

def add(a,b):
    return a+b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("a can not be 0")
    return b/a

def log(a, b):
    if b <= 0:
        raise ValueError("log argument must be positive")
    elif a < 0 or a == 1:
        raise ValueError("log base cant equal one or be negative")
    return math.log(a,b)


def exp(a, b):
    return a**b


