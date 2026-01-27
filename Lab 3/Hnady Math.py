#handy library of mathemaitical functions
#Name: Paul Bagara
#Date: January 27, 2026

def midpoint(num1, num2):
    """Calculate the mid point between two numbers."""
    mid = (num1 + num2) / 2
    return mid
def sqrt(number):
    "Calculate the square root of a number"
    if number < 0:
        return None
    return number ** 0.5


def exponent(base, exp):
    """Calculate the exponent of a base raised to exp."""
    return base ** exp

def rounded_result(value, precision=2):
    """Return value rounded to the given precision."""
    return round(value, precision)

