import math


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if a == 0:
        raise ZeroDivisionError("Division by zero")
    else:
        return b/a

def logarithm(a,b):
    if b <= 0 or a <= 0 or a == 1:
        raise ValueError(f"{b} less than 0 or {a} is 1 or {a} is less than 0")
    else:
        return math.log(a,b)

def exponential(a,b):
    return a**b


