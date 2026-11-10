import math

def add(a,b):
    return a + b

def subtract(a, b):
    return a-b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("a can not me 0")
    return b/a

def logarithm(a, b):
    if  <= 0:
        raise ValueError("log argument must be positive")
    elif a < 0 or a == 1:
        raise ValueError("log base cant equal one or be negative")
    return math.log(a,b)


def exp(a, b):
    return a**b


