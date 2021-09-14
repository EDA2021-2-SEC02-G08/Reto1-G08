"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


default_limit = 1000
sys.setrecursionlimit(default_limit * 10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


def printArtist(artist):
    pass


def printArtWorkData(artwork):
    pass


def printMenu():
    print("Bienvenido")
    print("1- Consultar los artistas segun su año de nacimiento")
    print("2- Consultar las obras segun su fecha de adquisicion")
    print("3- Consultar las obras de un artista por tecnica")
    print("4- Consultar las obras por la nacionalidad de sus artistas")
    print("5- Consultar el costo de transportar las obras")
    print("0- Salir")


catalog = None


"""
Menu principal
"""


while True:
    printMenu()
    catalog = initCatalog()
    loadData(catalog)
    print('\nCargando información de los archivos...')
    print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
    print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
    inputs = input('\nSeleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        inicio = int(input('Ingrese el año inicial: '))
        fin = int(input('Ingrese el año final: '))
        controller.sortArtists(catalog)
        result = controller.getArtists(catalog, inicio, fin)
        print(result)

    elif int(inputs[0]) == 2:
        inicio = str(input('Ingrese la fecha inicial (AAAA-MM-DD): '))
        fin = str(input('Ingrese la fecha final (AAAA-MM-DD): '))
        sorted_list = controller.sortArtworks(catalog)
        print(sorted_list[0])
        result = controller.getArtWorks(sorted_list[1], inicio, fin)

    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass 

    else:
        sys.exit(0)

sys.exit(0)