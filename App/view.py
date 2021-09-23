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


# Funciones auxiliares


def artistInfo(artists):
    i = 1
    while i <= 3:
        artist = lt.getElement(artists, i)
        print('Nombre: ' + artist['DisplayName'] +
              '. Nacimiento: ' + artist['BeginDate'] +
              '. Fallecimiento: ' + artist['EndDate'] +
              '. Nacionalidad: ' + artist['Nationality'] +
              '. Genero: ' + artist['Gender'])
        i += 1

    i = -2
    while i <= 0:
        artist = lt.getElement(artists, i)
        print('Nombre: ' + artist['DisplayName'] +
              '. Nacimiento: ' + artist['BeginDate'] +
              '. Fallecimiento: ' + artist['EndDate'] +
              '. Nacionalidad: ' + artist['Nationality'] +
              '. Genero: ' + artist['Gender'])
        i += 1


def artworkInfo(artworks):
    i = 1
    while i <= 3:
        artwork = lt.getElement(artworks, i)
        print('Titulo: ' + artwork['Title'] +
              '. Fecha: ' + artwork['Date'] +
              '. Medio: ' + artwork['Medium'] +
              '. Dimensiones: ' + artwork['Dimensions'])
        i += 1

    i = -2
    while i <= 0:
        artwork = lt.getElement(artworks, i)
        print('Titulo: ' + artwork['Title'] +
              '. Fecha: ' + artwork['Date'] +
              '. Medio: ' + artwork['Medium'] +
              '. Dimensiones: ' + artwork['Dimensions'])
        i += 1


def countPurchase(artworks):
    count = 0
    for artwork in lt.iterator(artworks):
        if 'purchase' in artwork['CreditLine'].lower():
            count += 1

    return count


def countArtists(artworks):
    auxiliar = {}
    count = 0
    for artwork in lt.iterator(artworks):
        artists_id = artwork['ConstituentID'].replace('[', '').replace(']', '')

        if ',' in artists_id:
            lista = artists_id.split(', ')
            for artist in lista:
                veces = auxiliar.get(artist, 0)
                if veces == 0:
                    auxiliar[artist] = 1
                    count += 1
        else:
            veces = auxiliar.get(artists_id, 0)
            if veces == 0:
                auxiliar[artists_id] = 1
                count += 1

    return count


# Funciones imprimir


def printBeginDate(result):
    size = lt.size(result)
    print('\nHay ' + str(size) + ' artistas nacidos en este rango de tiempo.')
    print('\nLos primeros y últimos tres artistas son:')
    artistInfo(result)


def printDateAcquired(result):
    size = lt.size(result)
    print('\nEl MoMA adquirió ' + str(size) + ' obras en este rango')
    purchase = str(countPurchase(result))
    artists = str(countArtists(result))
    print('Con ' + artists + ' artistas distintos y ' +
          purchase + ' de estas obras compradas.')
    print('\nLas primeras y últimas obras de arte son:')
    artworkInfo(result)


def printNationality(result):
    top10 = result[0]
    top1 = result[1]
    print('\nEl TOP 10 de nacionalidad en el MoMA es:')

    for top in top10:
        print(top)

    print('\nEl TOP de nacionalidad en el MoMA es: ' + str(top10[0][0]) +
          ' con ' + str(top10[0][1]) + ' obras de arte.')
    print('\nLos primeros y ultimo tres en la lista de obras ' +
          str(top10[0][0]) + ' son:')
    artworkInfo(top1)


def printTechniques(result1):
    print('Las obras con esta técnica son:')
    for artwork in lt.iterator(result1):
        print('Título: ' + artwork['Title'] + ' Fecha: ' + artwork['Date'] + 
              ' Medio: ' + artwork['Medium'] + ' Dimensiones: ' + artwork['Dimensions'])



def printMenu():
    print("\nBienvenido")
    print('0- Cargar Datos')
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
    inputs = int(input('\nSeleccione una opción para continuar\n'))
    if inputs == 0:
        print('\nCargando información de los archivos...')
        catalog = initCatalog()
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
    elif inputs == 1:
        inicio = int(input('Ingrese el año inicial: '))
        fin = int(input('Ingrese el año final: '))
        controller.sortArtists(catalog)
        result = controller.getArtists(catalog, inicio, fin)
        printBeginDate(result)

    elif inputs == 2:
        inicio = str(input('Ingrese la fecha inicial (AAAA-MM-DD): '))
        fin = str(input('Ingrese la fecha final (AAAA-MM-DD): '))
        controller.sortArtworks(catalog)
        result = controller.getArtWorks(catalog, inicio, fin)
        printDateAcquired(result)

    elif inputs == 3:
        artista = str(input('Ingrese el artista a examinar: '))
        controller.sortIDs(catalog)
        num, techs, artworks, top_tech, n_top = controller.getArtistTechniques(catalog, artista)
        num_techs = len(techs)
        print('\n' + artista + 'tiene ' + str(num) + 
              ' piezas a su nombre en el museo.')
        print('Hay un total de ' + str(num_techs) + ' técnicas a su nombre.')
        print('La técnica más utilizada por este/esta artista es ' + top_tech 
              + ' con un total de ' + str(n_top) + ' obras con esta técnica.')
        printTechniques(artworks)


    elif inputs == 4:
        result = controller.getTOP(catalog)
        printNationality(result)

    elif inputs == 5:
        department = str(input('Ingrese el departamento del MoMA: '))
        result = controller.getRequirement5(catalog, department)
        print(result[0])
        print(result[1])
    else:
        sys.exit(0)

sys.exit(0)
