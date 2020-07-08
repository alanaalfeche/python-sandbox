class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    def __str__(self):
        # overides previous implementation of converting object to string
        return f"{self.num}/{self.den}"

    def __add__(self, frac2):
        num = self.num*frac2.den + frac2.num*self.den 
        den = self.den*frac2.den
        
        return Fraction(num,den)

    def __eq__(self, frac2):
        frac1 = self.num*self.den
        frac2 = frac2.num*frac2.den

        return frac1 == frac2

frac1 = Fraction(2,3)
frac2 = Fraction(3,5)
fsum = frac1.__add__(frac2)
feq = frac1.__eq__(frac2)
print(feq)