##Declaracion tupla 

tupla = (1,2,3,4,5)
print(tupla)
print(type(tupla))

## Operaciones 

tuplaAnin = 1,2,('a','b'),4
print(tuplaAnin)
print(tuplaAnin[2][0])

## convertir lista atupla 

lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla)) #<class 'tuple'>
print(tupla) 

## iteracion con ducle for

tupla = [1, 2, 3]
for t in tupla:
    print(t) #1, 2, 3

## Metodos

l = [1, 1, 1, 3, 5]
print(l.count(1)) #3

l = [7, 7, 7, 3, 5]
print(l.index(7, 2)) #2