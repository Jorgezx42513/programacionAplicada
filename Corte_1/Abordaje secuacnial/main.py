import operacionesAlgebraicas

obj = operacionesAlgebraicas.OperacionesBasicas()

obj.setVal(float(input("ingrese un numero a:")))

obj.setVal2(float(input("ingrese un numero b:")))



obj.sumar(obj.getVal(),obj.getVal2())
print("suma a + b =" + str(obj.getR()))

obj.resta(obj.getVal(),obj.getVal2())
print("resta a - b=" + str(obj.getR()))

obj.resta(obj.getVal2(),obj.getVal())
print("resta b - a =" + str(obj.getR()))

obj.multiplicar(obj.getVal(),obj.getVal2())
print("multiplicacion 1 * b =" + str(obj.getR()))

obj.divisor(obj.getVal(),obj.getVal2())
print("division a/b=" + str(obj.getR()))

obj.divisor(obj.getVal2(),obj.getVal())
print("divicion b/a=" + str(obj.getR()))

obj.exponencial(obj.getVal(),obj.getVal2())
print("exponencial aˆb=" + str(obj.getR()))

obj.raiz(obj.getVal())
print(" raiz de a " + str(obj.getR()))

obj.raiz(obj.getVal2())
print("raiz de b " + str(obj.getR()))