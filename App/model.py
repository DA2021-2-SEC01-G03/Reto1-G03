
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

# Construccion de modelos

def newCatalog():
   
    catalog = {'artists': None,
               'artworks': None,
               }

    catalog['artists'] = lt.newList('SINGLE_LINKED')
    catalog['artworks'] = lt.newList('SINGLE_LINKED')
   
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):

    lt.addLast(catalog['artists'], artist)


def addArtwork(catalog, artwork):

    lt.addLast(catalog['artworks'], artwork)



# Funciones para creacion de datos

# Funciones de consulta



# Funciones utilizadas para comparar elementos dentro de una lista
def compareauthors(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1



def compareratings(artist1, artist2):
    return (float(artist1['BeginDate']) > float(artist2['BeginDate']))    

def comparetagnames(name, tag):
    if (name == tag['name']):
        return 0
    elif (name > tag['name']):
        return 1
    return -1    

# Funciones de ordenamiento

def sortArtistsBeginDate(catalog):
    sa.sort(catalog['artists'], compareratings)