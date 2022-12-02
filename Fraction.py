def pgcd(a:int, b:int):
    for i in range(min(a,b),1,-1):
        if a % i == 0 and b % i == 0 :
            return i

class Fraction:
    All = []
    def __init__(self, a:int, b:int) -> object:
        assert b != 0, f"{self.__b} DEM must be not Zero ..!"
        self.__a = a
        self.__b = b
        Fraction.All.append(self)

    def __str__(self) -> str:
        # return "%d / %d "%(self.A, self.B) 
        if self.A == 0 or self.B == 1:
            return f"{self.A}"
        return f"{self.A}/{self.B}"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.A},{self.B})"

    def get_A(self):
        return self.__a

    def set_A(self,newA):
        self.__a=newA
    A=property(get_A,set_A)

    def get_B(self):
        return self.__b

    def set_B(self,newB):
        assert newB != 0, f"{self.B} DEM must be not Zero ..!"
        self.__b=newB
    B=property(get_B,set_B)

    def MultiplayByCoef(self, coef:int):
        return f"{(coef * self.A)}/{self.B}"

    def MultiplayByFrac(self, frac):
        return f"{self.A * frac.A}/{self.B * frac.B}"

    def AddFrac(self, frac):
        if self.B == frac.B:
            return f"{self.A + frac.A}/{self.B}"
        else:
            return f"{(self.A * frac.B) + (self.B * frac.A)}/{self.B * frac.B}"

    def SubFrac(self, frac):
        if self.B == frac.B:
            return f"{self.A - frac.A}/{self.B}"
        else:
            return f"{(self.A * frac.B) - (self.B * frac.A)}/{self.B * frac.B}"

    def reversFrac(self):
        return Fraction(self.B, self.A)

    def DivisByFrac(self, frac):
        return self.MultiplayByFrac(frac.reversFrac())

    def RedFrac(self):
        return f"{self.A // pgcd(self.A, self.B)}/{self.B // pgcd(self.A, self.B)}"
    
    def CmpareFrac(self, frac , comp=max):
        sub = self.SubFrac(frac)
        if comp == max:
            # if self.B == frac.B:
            #     if self.A > frac.A:
            #         return f"{self.A}/{self.B}"
            #     return f"{frac.A}/{self.B}"
            if int(sub[:sub.index('/')]) > 0:
                return f"{self.A}/{self.B}"
            return f"{frac.A}/{frac.B}"

        if comp == min:
            if int(sub[:sub.index('/')]) < 0:
                return f"{self.A}/{self.B}"
            return f"{frac.A}/{frac.B}"

        if comp == 'equal':
            if int(sub[:sub.index('/')]) ==  0: return True
            return False
                
        

f = Fraction(-20,38)     
f1 = Fraction(4,18)     
f2 = Fraction(7,3)
f3 = Fraction(7,3)
print(f3.CmpareFrac(f2, comp='equal')) 
# t = '23456789/455678UI9'
# print(t[:t.index('/')])
# print(t[t.index('/')+1:])