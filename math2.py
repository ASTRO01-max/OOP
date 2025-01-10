class Math:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    
    def plus(self):
        return self.a+self.b
    
    def minus(self):
        return self.a-self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def to_divide(self):
        return self.a // self.b
    
    def square(self, x):
        return x ** 2
    
    def cube(self, x):
        return x**3
    
    def modulus(self):
        return self.a % self.b

    def be_interestBearing(self):
        return self.a / self.b
    
    def minimum(self):
        if self.a < self.b:
            return self.a
        else:
            return self.b
    
    def maximum(self):
        if self.a > self.b:
            return self.a
        else:
            return self.b

math_obj = Math(20, 5)
print(math_obj.plus())
print(math_obj.minus())
print(math_obj.multiplication())
print(math_obj.square(5))
print( math_obj.cube(3))
print(math_obj.modulus())
print(math_obj.be_interestBearing())
print(math_obj.minimum())
print(math_obj.maximum())
