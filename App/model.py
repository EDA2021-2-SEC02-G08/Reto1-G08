﻿"""
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
    data_artwork = newArtWork(artwork)
    lt.addLast(catalog['artworks'], data_artwork)


def addID(catalog, artwork):
    artwork_id = artwork['ObjectID']
    artists_id = artwork['ConstituentID'].replace('[', '').replace(']', '')

    if ',' in artists_id:
        lista = artists_id.split(', ')
        for artist in lista:
            id = artwork_id + '-' + artist
            lt.addLast(catalog['id'], id)
    else:
        id = artwork_id + '-' + artists_id
        lt.addLast(catalog['id'], id)


# Funciones para creacion de datos


def newArtist(artist):
    """
    Crea una nueva estructura para modelar los datos relevantes de cada artista
    """
    data_artist = {'id': None, 
                   'name': None, 
                   'nationality': None, 
                   'gender': None,
                   'beginDate': None}
    
    data_artist['id'] = artist['ConstituentID']
    data_artist['name'] = artist['DisplayName']
    data_artist['nationality'] = artist['Nationality']
    data_artist['gender'] = artist['Gender']
    data_artist['beginDate'] = artist['BeginDate']

    return data_artist


def newArtWork(artwork):
    """
    Crea una nueva estructura para modelar los datos relevantes de cada obra
    """
    data_artWork = {'id': artwork['ObjectID'], 
                   'title': artwork['Title'],
                   'date': artwork['Date'], 
                   'medium': artwork['Medium'],
                   'dimensions': artwork['Dimensions'], 
                   'creditLine': artwork['CreditLine'],
                   'department': artwork['Department'],
                   'dateAcquired': artwork['DateAcquired'],
                   'weight (kg)': artwork['Weight (kg)'],
                   'circumference (cm)': artwork['Circumference (cm)'],
                   'depth (cm)': artwork['Depth (cm)'],
                   'diameter (cm)': artwork['Diameter (cm)'],
                   'height (cm)': artwork['Height (cm)'],
                   'lenght (cm)': artwork['Length (cm)'],
                   'width (cm)': artwork['Width (cm)']}

    return data_artWork


# Funciones de consulta

def getArtists(catalog, año_inicial, año_final):
    lista = lt.newList(datastructure='ARRAY_LIST')

    for artist in lt.iterator(catalog['artists']):
        if artist['beginDate'] in range(año_inicial, año_final + 1):
            lt.addLast(lista, artist)

    return lista
    

def getArtWork(catalog, fecha_inicial, fecha_final):
    pass


# Funciones utilizadas para comparar elementos dentro de una lista


def compareArtists(artist1, artist2):
    return (int(artist1['beginDate']) > int(artist2['beginDate']))


# Funciones de ordenamiento


def sortArtists(catalog):
    pass


def sortArtWorks(catalog):
    pass
