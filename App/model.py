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
from DISClib.ADT import list as lt
assert cf


"""
Se define la estructura de un catálogo de obras y artisitas. El catálogo
tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


# Construccion de modelos


def newCatalog():
    """
    Inicializa el catálogo de obras y artistas. Crea una lista vacia para
    guardar todos los artistas y crea una lista vacia para las obras.
    """
    catalog = {'artists': None,
               'id': None,
               'artworks': None}

    catalog['artists'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['id'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['artworks'] = lt.newList(datastructure='ARRAY_LIST')

    return catalog


# Funciones para agregar informacion al catalogo


def addArtist(catalog, artist):
    data_artist = newArtist(artist)
    lt.addLast(catalog['artists'], data_artist)


def addArtwork(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)


# Funciones para creacion de datos

def newArtist(artist):
    """
    Crea una nueva estructura para modelar los datos de cada artista
    """
    data_artist = {'id': None, 
                   'name': None, 
                   'nationality': None, 
                   'beginDate': None}
    
    data_artist['id'] = artist['ConstituentID']
    data_artist['name'] = artist['DisplayName']
    data_artist['nationality'] = artist['Nationality']
    data_artist['beginDate'] = artist['BeginDate']

    return data_artist


def create_addID(catalog, artwork):
    """
    Crea un nuevo id en el que se relaciona el id del artwork y el del artist.
    Este nuevo id se adiciona a la lista id del catálogo.
    """
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


# Funciones de consulta


# Funciones utilizadas para comparar elementos dentro de una lista


# Funciones de ordenamiento


def sortArtists(catalog):
    pass


def sortArtWorks(catalog):
    pass
