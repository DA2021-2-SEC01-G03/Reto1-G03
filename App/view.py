
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

def initCatalog():

    return controller.initCatalog()


def loadData(catalog):
    
    controller.loadData(catalog)

def artistsByDates():
    date01 = int(input('Primer año (YYYY) '))
    date02 = int(input('Último año (YYYY) '))
    controller.sortArtistsBeginDate(catalog)
    list = controller.artistsByDates(catalog,date01,date02)[0]
    print("There are " + str(controller.artistsByDates(catalog,date01,date02)[1]) + " artists born between " + str(date01) + " and " + str(date02))

    return print(list)


def artworksByDateAquired():
    date01 = int(input('Fecha inicial (AAAAMMDD) '))
    date02 = int(input('Fecha final  (AAAAMMDD) '))
    controller.sortArtworksDateAquired(catalog)
    list = controller.artworksByDates(catalog,date01,date02)[0]
    print("There are " + str(controller.artistsByDates(catalog,date01,date02)[1]) + " artists born between " + str(date01) + " and " + str(date02))

    return print(list)



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
        artistsByDates()

    elif int(inputs[0]) == 3:
        artworksByDateAquired()    

    else:
        sys.exit(0)
        

