

import config as cf
import model
import csv


# Inicialización del Catálogo de libros
def initCatalog():
    
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos
def loadData(catalog):
    
    loadArtists(catalog)
    loadArtworks(catalog)
    sortArtistsBeginDate(catalog)


def loadArtists(catalog):
    
    booksfile = cf.data_dir + 'MoMA/Artists-utf8-5pct.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)


def loadArtworks(catalog):
    
    tagsfile = cf.data_dir + 'MoMA/Artworks-utf8-5pct.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)



# Funciones de ordenamiento

def sortArtistsBeginDate(catalog):
    model.sortArtistsBeginDate(catalog)
# Funciones de consulta sobre el catálogo
