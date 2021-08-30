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


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar el nacimiento de los artistas en un rango de tiempo")
    print("3- Consultar la fecha de adquisición de las obras en un rango de tiempo")
    print("4- Consultar las obras de un artista por técnica")
    print("5- Consultar las obras por la nacionalidad de sus artistas")
    print("6- Consultar el costo de transportar todas las obras de un departamento del MoMA")
    print("0- Salir")


catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        numArtists = lt.size(catalog['artists'])
        numArtworks = lt.size(catalog['artworks'])
        print('Artistas cargados: ' + str(numArtists))
        print('Obras cargadas: ' + str(numArtworks))
        print('Últimos tres artistas: ' + '\n' + 
              str(lt.getElement(catalog['artists'], numArtists-2)) + '\n' +
              str(lt.getElement(catalog['artists'], numArtists-1)) + '\n' +
              str(lt.lastElement(catalog['artists'])))
        print('Últimas tres obras: ' + '\n' + 
              str(lt.getElement(catalog['artworks'], numArtworks-2)) + '\n' +
              str(lt.getElement(catalog['artworks'], numArtworks-1)) + '\n' +
              str(lt.lastElement(catalog['artworks'])))

    elif int(inputs[0]) == 2:
        pass

    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass

    else:
        sys.exit(0)
sys.exit(0)
