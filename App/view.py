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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def initCatalog(datastructure):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(datastructure)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


def printMenu():
    print("Bienvenido")
    print("1- Seleccionar la estructura de datos")
    print("2- Ordenar las obras de arte por fecha de adquisición")
    print("0- Salir")


catalog = None


"""
Menu principal
"""


while True:
    printMenu()
    inputs = input('\nSeleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        datastructure = str(input('Seleccione la estructura de datos (ARRAY_LIST / LINKED_LIST): '))
        catalog = initCatalog(datastructure)
        loadData(catalog)
        print('\nCargando información de los archivos...')
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
    elif int(inputs[0]) == 2:
        size = int(input('Indique tamaño de la muestra: '))
        sort = str(input('Indique el algoritmo de ordenamiento iterativo: '))
        result = controller.sortArtworks(catalog, size, sort)
        print('Para la muestra de', size, 'elementos, el tiempo (mseg) es:', result)

sys.exit(0)