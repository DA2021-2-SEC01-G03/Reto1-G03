

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


def loadArtists(catalog):
    
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)


def loadArtworks(catalog):
    
    tagsfile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)



# Funciones de ordenamiento

def sortArtistsBeginDate(catalog):
    model.sortArtistsBeginDate(catalog)

def sortArtworksDateAquired(catalog):
    model.sortArtworksDateAquired(catalog)    


# Funciones de consulta sobre el catálogo

def artistsByDates(catalog,date1,date2):
    return model.artistsByDates(catalog,date1,date2)

def artworksByDates(catalog,date1,date2):
    return model.artworksByDates(catalog,date1,date2)
