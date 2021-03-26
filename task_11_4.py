class ComplexValue:
    def __init__(self,re,im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplexValue(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexValue(self.re * other.re - self.im * other.im, self.re * other.im + self.im*other.re)

    def __str__(self):
        return f"(Real:{self.re}, Imagine:{self.im})"

a = ComplexValue(1,2)
b = ComplexValue(2,1)
c = 1 + 2j
d = 2 + 1j
print(f"Sum complex values {a} and {b} is {a+b}")
print(f"Control {c+d}")
print(f"Mul complex values {a} and {b} is {a*b}")
print(f"Control {c*d}")

