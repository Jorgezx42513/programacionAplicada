import math
class OperacionesBasicas:
   
    def __init__(self):
        self.val=0
        self.val2=0
        self.r=0
    
    def getVal(self):
        return self.val
    
    def setVal(self, valor):
        self.val=valor

    def getVal2(self):
        return self.val2
    
    def setVal2(self, valor):
        self.val2=valor

    def getR(self):
        return self.r
    
    def setR(self, valor):
        self.r=valor
    
    def sumar(self,a,b):
        self.r = a + b

    def resta(self, a, b):
        self.r = a - b

    def multiplicar(self,a,b):
        self.r = a * b

    def divisor(self, a, b):
        self.r = a/b

    def exponencial(self, a, b):
        self.r = pow(a, b)

    def raiz(self, a):
        self.r = math.sqrt(a)


    

