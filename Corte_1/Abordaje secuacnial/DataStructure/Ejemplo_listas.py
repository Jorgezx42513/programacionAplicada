# Ejemplo listas con python 

#lista comun

juegolistComun = ["Isacc +rebirt", 2.00, 2023]

print("-----------------------------------------------")
print("lista comun")

print("el juego se llama:"+ juegolistComun[0])
#Al poner a poscion -2 me devuelve la penultima posicion 
print("Tiene un precio de:"+ str(juegolistComun[-2]))
#Al poner la posicion -1 me devuelve la ultima posicion 
print("Salio en el:"+ str(juegolistComun[-1]))
print("-----------------------------------------------")

#lista anidada

juego = [["isacc +rebirth",2.9,2021]]
print("-----------------------------------------------")
print("Lista anidada")

print("el juego se llama:"+ juego[0][0])
#Al poner a poscion -2 me devuelve la penultima posicion 
print("Tiene un precio de:"+ str(juego[0][-2]))
#Al poner la posicion -1 me devuelve la ultima posicion 
print("Salio en el:"+ str(juego[0][-1]))
print("-----------------------------------------------")


# ingresar un elemento a la lista anidad
nombre = input("ingrese el combre del juego:")
precio = input("ingrese el precio del juego:")
salida = input("ingrese cuando salio:")
juego.append([nombre,precio,salida])
print("-----------------------------------------------")
print("Lista anidada con nuevo registro")
counter = 0

while counter < len(juego):
    print("el juego se llama:"+ juego[counter][0])
    #Al poner a poscion -2 me devuelve la penultima posicion 
    print("Tiene un precio de:"+ str(juego[counter][-2]))
    #Al poner la posicion -1 me devuelve la ultima posicion 
    print("Salio en el:"+ str(juego[counter][-1]))
    counter = counter + 1
    print("-----------------------------------------------")







