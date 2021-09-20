
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

# Construccion de modelos

def newCatalog():
   
    catalog = {'artists': None,
               'artworks': None,
               }

    catalog['artists'] = lt.newList('ARRAY_LIST')
    catalog['artworks'] = lt.newList('ARRAY_LIST')
   
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):

    lt.addLast(catalog['artists'], artist)


def addArtwork(catalog, artwork):

    lt.addLast(catalog['artworks'], artwork)



# Funciones para creacion de datos

# Funciones de consulta

def artistsByDates(catalog, date1:int, date2:int):

    list = lt.newList()
    artists = catalog['artists']
    i = 1
    tam = lt.size(artists)
    count = 1
    while i < tam:
      dict = lt.getElement(artists, i)
      if (int(dict['BeginDate']) >= date1) and (int(dict['BeginDate']) <= date2):
          lt.addLast(list, dict)
          count += 1
      i += 1
    return (list,count)


def artworksByDates(catalog, date1, date2):
    list = lt.newList()
    artworks = catalog['artworks']
    artists = catalog['artists']
    i = 1
    tam = lt.size(artworks)
    count = 0
    while i < tam:
      dict = lt.getElement(artworks, i) 
      DateInt = becomeDateAquiredToInt(dict['DateAcquired'])
      if DateInt > date1 and DateInt < date2:
         constituentslistByArtwork = []
         constituents = dict['ConstituentID'] 
         lt.addLast(list, dict)
         count += 1
         for artist in lt.iterator(artists):
            if artist['ConstituentID'] in constituents:
                constituentslistByArtwork.append(artist['DisplayName'])
         dict['ArtistsNames'] = constituentslistByArtwork    
      i += 1           

    return (list,count)               





# Funciones utilizadas para comparar elementos dentro de una lista

def compareBeginDates(artist1, artist2):
    return int(artist1['BeginDate']) < int(artist2['BeginDate'])

def compareDatesAquired(artwork1, artwork2):
    date1 = artwork1['DateAcquired']
    date2 = artwork2['DateAcquired']

    intDate1 = becomeDateAquiredToInt(date1)
    intDate2 = becomeDateAquiredToInt(date2)

    return intDate1 < intDate2
    
    

# Funciones de ordenamiento

def sortArtistsBeginDate(catalog):
    sa.sort(catalog['artists'], compareBeginDates)

def sortArtworksDateAquired(catalog):
    ms.sort(catalog['artworks'], compareDatesAquired)

#Auxiliar functions

def becomeDateAquiredToInt(Date):
    if Date == '':
        DateInt = 0
    else:
        year = str(Date[0]) + str(Date[1]) +str(Date[2]) + str(Date[3])
        month = str(Date[5]) + str(Date[6]) 
        day = str(Date[8]) + str(Date[9])    
         
        DateInt = int(year+month+day) 
        

    return DateInt
