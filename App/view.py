
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

def initCatalog():

    return controller.initCatalog()


def loadData(catalog):
    
    controller.loadData(catalog)


def printMenu():
    print("Bienvenido")
    print("1- Cargar información de artistas u obras")
    print("2- Listar cronológicamente artistas dentro de un rango de años")

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
        int(input('Primer año (YYYY) '))
        int(input('Último año (YYYY) '))

        

    else:
        sys.exit(0)
        

