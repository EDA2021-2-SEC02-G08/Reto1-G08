import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del cátalogo


def initCatalog():
    """
    Llama la función de inicialización del catálogo del model
    """
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos


def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)


def loadArtists(catalog):
    """
    Carga los artistas del archivo.
    """
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-20pct.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)


def loadArtworks(catalog):
    """
    Carga las obras del archivo.
    """
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-20pct.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)


# Funciones de ordenamiento


def sortArtists(catalog):
    """
    Ordena los artistas por año de nacimiento
    """
    return model.sortArtists(catalog)


def sortArtworks(catalog):
    """
    Ordena las obras de arte por año de adquisición
    """
    return model.sortArtWorks(catalog)


# Funciones de consulta sobre el catálogo


def getArtists(catalog, inicio, fin):
    """
    Retorna los artistas según su año de nacimiento.
    """
    return model.getArtists(catalog, inicio, fin)


def getArtWorks(catalog, inicio, fin):
    """
    Retorna las obras según su fecha de adquisición.
    """
    return model.getArtWorks(catalog, inicio, fin)


def getTOP(catalog):
    """
    Retorna el TOP de nacionalidades por obra.
    """
    return model.getTOP(catalog)


def getRequirement5(catalog, department):
    """
    Retorna el requerimiento 5 del reto.
    """
    return model.getRequirement5(catalog, department)
