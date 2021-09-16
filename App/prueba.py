import config as cf
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.ADT import list as lt
assert cf
from datetime import date

lista = lt.newList('ARRAY_LIST')

lista_auxiliar = ['1990-06-03', '2000-06-04', '1996-06-04']

for element in lista_auxiliar:
    lt.addLast(lista, element)


print(lista)


def cmpfunction(element1, element2):
    return date.fromisoformat(element1) < date.fromisoformat(element2)


ins.sort(lista, cmpfunction)


print(lista)
