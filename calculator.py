class Calculator():

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return 'undefined'
        else:
            return a / b
    
    def power(self, a, b):
        return a ** b
    
    def factorial(self, a):
        if a == 0:
            return 1
        elif a<0:
            return a * self.factorial(a+1)
        else:
            return a * self.factorial(a-1)
        
        