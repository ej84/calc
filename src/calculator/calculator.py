import math
class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self,a,b):
        result = a + b
        return result

    def divide(self,a,b):
        result = a / b
        return result

    def multiply(self, a, b):
        result = a * b
        return result

    def subtraction(self,a,b):
        result = a - b
        return result

    def sqrt(self,a):
        result = math.sqrt(a)
        return result

    def square(self,a):
        result = a**2
        return result