
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

def initCatalog():

    return controller.initCatalog()


def loadData(catalog):
    
    controller.loadData(catalog)


# Artists ByDates


def artistsByDates():
    controller.sortArtistsBeginDate(catalog)
    list = controller.artistsByDates(catalog,date01,date02)[0]

    sizeList = lt.size(list)
 
    if sizeList:
      first3 = lt.subList(list,1,3)
      last3 = lt.subList(list,sizeList-3,3) 
      print("There are " + str(controller.artistsByDates(catalog,date01,date02)[1]) + " artists born between " + str(date01) + " and " + str(date02))
      print("")
      print("The first and last 3 artists in the range are...")  
      for artist in lt.iterator(first3):
        
             print('Name: ' + artist['DisplayName'] + '  Begin date: ' +
                  artist['BeginDate'] + ' End date: ' + artist['EndDate'] +
                  ' Nacionality: ' + artist['Nationality'] + ' Gender: ' + artist['Gender'])

      print("")            

      for artist in lt.iterator(last3):
        
             print('Name: ' + artist['DisplayName'] + '  Begin date: ' +
                  artist['BeginDate'] + ' End date: ' + artist['EndDate'] +
                  ' Nacionality: ' + artist['Nationality'] + ' Gender: ' + artist['Gender'])  
      
                  
    else:
        print("No se encontraron artistas")                        
           

#Artworks By Date Acquired


def artworksByDateAquired():
    controller.sortArtworksDateAquired(catalog)
    list = controller.artworksByDates(catalog,date01,date02)[0]
    count = controller.artworksByDates(catalog,date01,date02)[1]
    
    sizeList = lt.size(list)
 
    if sizeList:
      first3 = lt.subList(list,1,3)
      last3 = lt.subList(list,sizeList-3,3) 
      print("The MoMA acquired " + str(count) + " unique pieces between " + str(date01) + " and " + str(date02))
      print("")
      print("The first and last 3 artworks in the range are...")  
      print("")
      for artwork in lt.iterator(first3):
        
             print('ObjectID: ' + artwork['ObjectID'] + ',  Title: ' +
                  artwork['Title'] + ', ArtistsNames: ' + str(artwork['ArtistsNames']) +
                  ', Medium: ' + artwork['Medium'] + ', Dimensions: ' + artwork['Dimensions']
                  + ', Date: ' + artwork['Date'] + ', DateAcquired: ' + artwork['DateAcquired'] +
                  ', URL: ' + artwork['URL'])
      print("")            

      for artwork in lt.iterator(last3):
        
             print('ObjectID: ' + artwork['ObjectID'] + ',  Title: ' +
                  artwork['Title'] + ', ArtistsNames: ' + str(artwork['ArtistsNames']) +
                  ', Medium: ' + artwork['Medium'] + ', Dimensions: ' + artwork['Dimensions']
                  + ', Date: ' + artwork['Date'] + ', DateAcquired: ' + artwork['DateAcquired'] +
                  ', URL: ' + artwork['URL'])  
      
                  
    else:
        print("No se encontraron artistas") 





#Menu


def printMenu():
    print("Bienvenido")
    print("1- Cargar información de artistas u obras")
    print("2- Listar cronológicamente artistas nacidos dentro de un rango de años")
    print("3- Listar cronológicamente las obras por fecha de adquisición")
    print("0- Salir")

catalog = None

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        


    elif int(inputs[0]) == 2:
        date01 = int(input('Primer año (YYYY) '))
        date02 = int(input('Último año (YYYY) '))
        artistsByDates()

    elif int(inputs[0]) == 3:
        date01 = int(input('Fecha inicial (AAAAMMDD) '))
        date02 = int(input('Fecha final  (AAAAMMDD) '))
        artworksByDateAquired()        

    else:
        sys.exit(0)
        

