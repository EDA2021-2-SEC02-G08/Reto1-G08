import config as cf
from datetime import date
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as mg
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
               'artworks': None}

    catalog['artists'] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=compareartists)
    catalog['artworks'] = lt.newList(datastructure='ARRAY_LIST')

    return catalog


# Funciones para agregar informacion al catalogo


def addArtist(catalog, artistinfo, artwork=None):
    """
    Adiciona un artista a lista de artistas, donde a su vez se guardan 
    """
    artists = catalog['artists']
    posartist = lt.isPresent(artists, artistinfo)
    if posartist > 0:
        artist = lt.getElement(artists, artistinfo)
    else:
        artist = newArtist(artistinfo)
        lt.addLast(artists, artist)
    if artwork is not None:
        lt.addLast(artist['artworks'], artwork)



def addArtwork(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)


# Funciones para creación de datos

def newArtist(info):
    """
    Crea una nueva estructura para modelar lasobras de un artista
    """
    artist = {'info': "", 'artworks': None}
    artist['info'] = info
    artist['artworks'] = lt.newList('ARRAY_LIST')
    return artist



# Algoritmos de busqueda


def busquedaBinaria(catalog, element):
    """
    Retorna la posición de un elemento en una lista organizada.
    Esta función encuentra el año de nacimiento del artista.
    En caso de no existir, retorna la última posición encontrada.
    """
    low = 0
    high = lt.size(catalog) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        cmp = lt.getElement(catalog, mid)
        if int(cmp['BeginDate']) < element:
            low = mid + 1
        elif int(cmp['BeginDate']) > element:
            high = mid - 1
        else:
            return mid

    return mid


def busquedaBinaria2(catalog, element):
    """
    Retorna la posición de un elemento en una lista organizada.
    Esta función encuentra la fecha de compra de una obra de arte.
    En caso de no existir, retorna la última posición encontrada.
    """
    low = 0
    high = lt.size(catalog) - 1
    mid = 0
    element = date.fromisoformat(element)

    while low <= high:
        mid = (high + low) // 2
        cmp = lt.getElement(catalog, mid)
        if date.fromisoformat(cmp['DateAcquired']) < element:
            low = mid + 1
        elif date.fromisoformat(cmp['DateAcquired']) > element:
            high = mid - 1
        else:
            return mid

    return mid



# Funciones de consulta


def getArtists(catalog, inicio, fin):
    """
    Retorna un arrayList con los artistas
    en un rango de tiempo.
    """
    artists = catalog['artists']
    pos_inicio = busquedaBinaria(artists, inicio)
    pos_fin = busquedaBinaria(artists, fin)
    arrayList = lt.newList(datastructure='ARRAY_LIST')

    for pos in range(pos_inicio, pos_fin + 1):
        artist = lt.getElement(artists, pos)
        lt.addLast(arrayList, artist)

    return arrayList


def getArtWorks(catalog, inicio, fin):
    """
    Retorna un arrayList con las obras de arte
    en un rango de tiempo.
    """
    artworks = catalog['artworks']
    pos_inicio = busquedaBinaria2(artworks, inicio)
    pos_fin = busquedaBinaria2(artworks, fin)
    arrayList = lt.newList(datastructure='ARRAY_LIST')

    for pos in range(pos_inicio, pos_fin + 1):
        artwork = lt.getElement(artworks, pos)
        lt.addLast(arrayList, artwork)

    return arrayList


# Funciones utilizadas para comparar elementos dentro de una lista


def cmpArtists(artist1, artist2):
    """
    Retorna True si el 'BeginDate' de artist1
    es menor que el de artist2.
    """
    return int(artist1['BeginDate']) < int(artist2['BeginDate'])


def cmpArtworks(artwork1, artwork2):
    """
    Retorna True si el 'DateAcquired' de artwork1
    es menor que el de artwork2.
    """
    if artwork1['DateAcquired'] == '' or artwork2['DateAcquired'] == '':
        return False
    else:
        artwork1 = date.fromisoformat(artwork1['DateAcquired'])
        artwork2 = date.fromisoformat(artwork2['DateAcquired'])
        return artwork1 < artwork2


# Funciones de comparación

def compareartists(artist1, artist2):
    if int(artist1['info']['ConstituentID']) ==  int(artist2['info']['ConstituentID']):
        return 0
    else:
        return -1


# Funciones de ordenamiento


def sortArtists(catalog):
    mg.sort(catalog['artists'], cmpArtists)


def sortArtWorks(catalog):
    mg.sort(catalog['artworks'], cmpArtworks)
