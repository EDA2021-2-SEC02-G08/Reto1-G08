"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from datetime import date
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import quicksort as qk
assert cf

"""
Se define la estructura de un catálogo de obras y artisitas. El catálogo
tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog(datastructure):
    """
    Inicializa el catálogo de obras y artistas. Crea una lista vacia para
    guardar todos los artistas y crea una lista vacia para las obras.
    """
    catalog = {'artists': None,
               'id': None,
               'artworks': None}

    catalog['artists'] = lt.newList(datastructure)
    catalog['id'] = lt.newList(datastructure)
    catalog['artworks'] = lt.newList(datastructure)

    return catalog


# Funciones para agregar informacion al catalogo


def addArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)


def addArtwork(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)


def createID(catalog, artwork):
    artwork_id = artwork['ObjectID']
    artists_id = artwork['ConstituentID'].replace('[', '').replace(']', '')
    lista = []

    if ',' in artists_id:
        lista = artists_id.split(', ')
        for artist in lista:
            id = artwork_id + '-' + artist
            lt.addLast(catalog['id'], id)
    else:
        id = artwork_id + '-' + artists_id
        lt.addLast(catalog['id'], id)


# Funciones utilizadas para comparar elementos dentro de una lista


def cmpArtwork(artwork1, artwork2):
    """
    Devuelve True si el 'DateAcquired' de artwork1
    es menor que el de artwork2.
    Args: 
        artwork1: información de la primera obra con su valor 'DateAcquired'.
        artwork2: información de la segunda obra con su valor 'DateAcquired'.
    """
    if artwork1['DateAcquired'] == '' or artwork2['DateAcquired'] == '':
        return False
    else:
        artwork1 = date.fromisoformat(artwork1['DateAcquired'])
        artwork2 = date.fromisoformat(artwork2['DateAcquired'])
        return artwork1 < artwork2
        

# Funciones de ordenamiento


def sortArtworks(catalog, sort, size):
    sub_list = lt.subList(catalog['artworks'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()

    if 'insertion' in sort.lower():
        sorted_list = ins.sort(sub_list, cmpArtwork)
    elif 'shell' in sort.lower():
        sorted_list = sa.sort(sub_list, cmpArtwork)
    elif 'merge' in sort.lower():
        sorted_list = mg.sort(sub_list, cmpArtwork)
    elif 'quick' in sort.lower():
        sorted_list = qk.sort(sub_list, cmpArtwork)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return elapsed_time_mseg, sorted_list
