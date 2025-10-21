## Definicion de un  diccionario 
registro = {
  "Nombre": "jorge",
  "Edad": 20,
  "compra": "GTAV"
}
print(registro)

##Formato key value

registro = dict([
      ('Nombre', 'Sara'),
      ('Edad', 25),
      ('compra', "GTAV"),
])
print(registro)

## GET 

print(registro.get('Nombre'))
# o
print(registro['Nombre'])

## Iteracion de un diccionario

for x in registro:
    print(registro[x])


for x,y in registro.items:
    print(x,y)

## Anidacion de diccionarios

anidado1 = {"a": 1, "b": 2}
anidado2 = {"a": 1, "b": 2}
d = {
  "anidado1" : anidado1,
  "anidado2" : anidado2
}
print(d)

##Metodos utiles

#Clear 
d = {'a': 1, 'b': 2}
d.clear()
print(d)

#get

d = {'a': 1, 'b': 2}
print(d.get('a')) #1
print(d.get('z', 'No encontrado'))

#Items

d = {'a': 1, 'b': 2}
it = d.items()
print(it)             
print(list(it))       
print(list(it)[0][0]) 

#Update 

d1 = {'a': 1, 'b': 2}
d2 = {'a': 0, 'd': 400}
d1.update(d2)
print(d1)
#{'a': 0, 'b': 2, 'd': 400}