import config as cf
from itertools import islice
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
               'id': {},
               'artworks': None}

    catalog['artists'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['artworks'] = lt.newList(datastructure='ARRAY_LIST')

    return catalog


# Funciones para agregar informacion al catalogo


def addArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)


def addArtwork(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    artists_id = artwork['ConstituentID'].replace('[', '').replace(']', '')

    if ',' in artists_id:
        lista = artists_id.split(', ')
        for artist_id in lista:
            addID(catalog, artist_id, artwork)
    else:
        addID(catalog, artists_id, artwork)


def addID(catalog, artist_id, artwork):
    id = catalog['id']

    if artist_id not in id.keys():
        for artist in lt.iterator(catalog['artists']):
            if artist['ConstituentID'] == artist_id:
                nacionalidad = artist['Nationality']
                id[artist_id] = createID(nacionalidad)
                break
        lt.addLast(id[artist_id]['artworks'], artwork)
    else:
        lt.addLast(id[artist_id]['artworks'], artwork)


# Funciones para creacion de datos


def createID(nacionalidad):
    id = {'nacionalidad': '', 'artworks': None}
    id['nacionalidad'] = nacionalidad
    id['artworks'] = lt.newList(datastructure='ARRAY_LIST')

    return id


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


# Funciones auxiliares


def take(n, iterable):
    "Return first n items of the iterable as a list"

    return list(islice(iterable, n))


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


def getTOP1(catalog, top1):
    """
    Retorna un arrayList con las obras de la nacionalidad
    mas recurrente en el MoMA.
    """
    id = catalog['id']
    arrayList = lt.newList(datastructure='ARRAY_LIST')

    for artist in id.values():
        nacionalidad = artist['nacionalidad']
        if nacionalidad == top1:
            for artwork in lt.iterator(artist['artworks']):
                lt.addLast(arrayList, artwork)

    return arrayList


def getTOP(catalog):
    """
    Retorna el TOP 10 de nacionalidades por obras.
    Retorna un arrayList con todas las obras de la
    nacionalidad más recurrente en el MoMA.
    """
    auxiliar = {}
    id = catalog['id']

    for artist in id.values():
        size = lt.size(artist['artworks'])
        nacionalidad = artist['nacionalidad']
        if nacionalidad == '' or nacionalidad == 'Nationality unknown':
            pass
        else:
            if nacionalidad not in auxiliar.keys():
                auxiliar[nacionalidad] = size
            else:
                auxiliar[nacionalidad] += size

    auxiliar_sorted = dict(sorted(auxiliar.items(), key=lambda item: item[1],
                           reverse=True))
    top10 = take(10, auxiliar_sorted.items())
    top1 = top10[0][0]
    arrayList = getTOP1(catalog, top1)

    return top10, arrayList


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


# Funciones de ordenamiento


def sortArtists(catalog):
    mg.sort(catalog['artists'], cmpArtists)


def sortArtWorks(catalog):
    mg.sort(catalog['artworks'], cmpArtworks)
