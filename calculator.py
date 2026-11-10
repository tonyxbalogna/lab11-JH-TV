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
    try:
        return b / a
    except ZeroDivisionError:
        return 'Division by zero'

def logarithm(a, b):
    try:
        return math.log(b,a)
    except ValueError:
        return 'a or b is negative or b is one'



def exp(a, b):
    return a**b


