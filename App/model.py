from DISClib.DataStructures.arraylist import getElement
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
               'artworks': None,
               'ConstituentIDs': None}

    catalog['artists'] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=compareArtistName)
    catalog['artworks'] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=compareArworks)
    catalog['ConstituentIDs'] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=compareIDs)

    return catalog


# Funciones para agregar informacion al catalogo

def addConstituentID(catalog, id, artwork=None, nationality=''):
    IDs = catalog['ConstituentIDs']
    posID = lt.isPresent(IDs, id)
    if posID > 0:
        C_ID = lt.getElement(IDs, posID)
    else:
        C_ID = newConstituentID(id, nationality)
        lt.addLast(IDs, C_ID)
        C_ID = lt.lastElement(IDs, C_ID) 
    if artwork is not None:
        lt.addLast(C_ID['artworks'], artwork)


def addArtist(catalog, artistinfo):
    """
    Adiciona un artista al catálogo y agrega su ID
    """
    lt.addLast(catalog['artists'], artistinfo)
    addConstituentID(catalog, artistinfo['ConstituentID'], artistinfo['Nationality'])


def addArtwork(catalog, artwork):
    """
    Adiciona una obra al catálogo y la asocia a los IDs de sus artistas.
    """
    lt.addLast(catalog['artworks'], artwork)
    artists_id = artwork['ConstituentID'].replace('[', '').replace(']', '')
    artists_id = artists_id.split(', ')

    for id in artists_id:
        addConstituentID(catalog, id.strip(), artwork)



# Funciones para creación de datos

def newConstituentID(id, nationality):
    """
    Crea una nueva estructura para modelar las obras de un artista
    """
    ID = {'ID': "", 'artworks': None, 'nationality': ""}
    ID['ID'] = id
    ID['artworks'] = lt.newList(datastructure='ARRAY_LIST')
    ID['nationality'] = nationality
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


def busquedaBinaria3(catalog, element):
    """
    Retorna la posición de un elemento en una lista organizada.
    Esta función encuentra el ID de un artista.
    En caso de no existir, retorna la última posición encontrada.
    """
    low = 0
    high = lt.size(catalog) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        cmp = lt.getElement(catalog, mid)
        if int(cmp['ID']) < element:
            low = mid + 1
        elif int(cmp['ID']) > element:
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


def getArtistID(catalog, artistname):
    artists = catalog['artists']
    pos = lt.isPresent(artists, artistname)
    if pos > 0:
        artist = lt.getElement(artists, pos)
        return int(artist['ConstituentID'])
    return None


def getTechniques(catalog, artist):
    """
    Retorna las técnicas empleadas por un artista
    """
    IDs = catalog['ConstituentIDs']
    id = getArtistID(catalog, artist)
    if id is not None:
        pos = busquedaBinaria3(IDs, id)
        artworks = lt.getElement(catalog, pos)['artworks']
        techniques = {}
        count = lt.size(artworks)
        for artwork in artworks:
            technique = artwork['Medium']
            if technique == '':
                pass
            elif technique not in techniques.keys():
                techniques[technique] = 1
            else:
                techniques[technique] += 1
        return count, techniques
    return None


def getArtworksByTechnique(catalog, artist, technique):
    """
    Retorna las obras de un artista con una técnica determinada.
    """
    IDs = catalog['ConstituentIDs']
    id = getArtistID(catalog, artist)
    if id is not None:
        pos = busquedaBinaria3(IDs, id)
        artworks = lt.getElement(catalog, pos)['artworks']
        array = lt.newList(datastructure='ARRAY_LIST')
        for artwork in artworks:
            if artworks['Medium']==technique:
                lt.addLast(array, artwork)
        return array
    return None


def getTOP1(catalog, top1):
    """
    Retorna un arrayList con las obras de la nacionalidad
    mas recurrente en el MoMA.
    """
    IDs = catalog['ConstituentIDs']
    arrayList = lt.newList(datastructure='ARRAY_LIST')

    for artist in lt.iterator(IDs):
        nacionalidad = artist['nationality']
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
    IDs = catalog['ConstituentIDs']

    for artist in lt.iterator(IDs):
        size = lt.size(artist['artworks'])
        nacionalidad = artist['nationality']
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


def cmpIDs(id1, id2):
    return int(id1['ID']) < int(id2['ID'])


def compareIDs(id1, id2):
    if int(id1['ID']) ==  int(id2['ID']):
        return 0
    else:
        return -1

def compareArtistName(artistname, artist):
    if (artistname.lower() in artist['DisplayName'].lower):
        return 0
    else:
        return -1


def compareArworks(artwork1, artwork2):
    if int(artwork1['ObjectID']) == int(artwork2['ObjectID']):
        return 0
    else:
        return -1




# Funciones de ordenamiento


def sortArtists(catalog):
    mg.sort(catalog['artists'], cmpArtists)


def sortArtWorks(catalog):
    mg.sort(catalog['artworks'], cmpArtworks)


def sortIDs(catalog):
    mg.sort(catalog['ConstituentIDs'], cmpIDs)
