#Este ejercicio vale una desima para el total del corte
while True:
    numero = int(input("ingrese un numero:"))
    if numero > 1 :
        if numero == 2:
            print("El numero es primo.")
        else:
            if numero % 2 != 0:
                n = numero - 1 
                while n > 1:
                    if numero % n == 0:
                        print("El numero no primo.")
                    n = n-1
                    break
                print("El numero es primo.")
            else:
                print("el numero no es primo. ")
    else:
        print("El numero no es primo.")