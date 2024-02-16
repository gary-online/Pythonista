"""
>>> triangle(4, 3)
6.0
>>> rectangle(4, 3)
12
>>> square(5)
25
"""
def triangle(height, base):
    return 0.5 * height * base

def rectangle(length, breadth):
    return length * breadth

def square(side):
    return side**2