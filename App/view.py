
from typing import OrderedDict
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
           
#New Function

def artworksByDateAquired():
    controller.sortArtworksDateAquired(catalog)
    list = controller.artworksByDates(catalog,date01,date02)[0]
    count = controller.artworksByDates(catalog,date01,date02)[1]
    
    sizeList = lt.size(list)
 
    if sizeList:
      first3 = lt.subList(list,1,3)
      last3 = lt.subList(list,sizeList-2,3) 
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


def artworkArtistByTechnique():
    orderedDict = controller.artworkArtistByTechnique(catalog,artist)[0]
    idArtist = controller.artworkArtistByTechnique(catalog,artist)[1]
    countPieces = controller.artworkArtistByTechnique(catalog,artist)[2]
    countTechnique = controller.artworkArtistByTechnique(catalog,artist)[3]


    print(artist + " with MoMA ID " + idArtist + " has " + str(countPieces) + " pieces in her/his name at the museum.")
    print("There are " + str(countTechnique) + " diferent mediums/techniques in her/his work")
    print("")

    if countTechnique > 0:
     print("Her/his top 5 medium/technique are...")

    
     tam = len(orderedDict)
     if tam < 6:
        i = tam-1
        while i >= 0:
            print(orderedDict[i])
            i -= 1 
     else:
        j = len(orderedDict)-6
        i = len(orderedDict)-1
        while i >= j :
            print(orderedDict[i])
            i -= 1
            

     
     sampleList = [] 
     k = 0
     for artwork in lt.iterator(catalog['artworks']):
         if artwork['Medium'] == orderedDict[tam-1][0] and artist in artwork['ArtistsNames']: 
            sampleList.append(artwork)
            k += 1
            if k == 3:
                break   

     print("")
     print("Her/his most used medium/technique is " + orderedDict[tam-1][0] + " with " + str(orderedDict[tam-1][1]) + " pieces")
     print("A sample of 3 " + orderedDict[tam-1][0] + " form the collection are...")   

     taml = len(sampleList)
     z = 0
     while z < taml:
         print("Object ID: " + sampleList[z]['ObjectID'] + ", Title: " + sampleList[z]['Title'] + 
               ", Medium: " + sampleList[z]['Medium'] + ", Date: " + sampleList[z]['Date'] + ", Dimensions: " 
               + sampleList[z]['Dimensions'])
         z += 1      


#New Function
def byNationality():

    listNationalitys = controller.artworksByNationality(catalog)
    print("The TOP 10 countries in the MoMA are...")
    if len(listNationalitys) > 10:
     tam2 = len(listNationalitys)-1
     i = len(listNationalitys)-11    
     while tam2 >= i:
        print(listNationalitys[tam2])
        tam2 -= 1
    else:
        print(listNationalitys)    

    print("The top Nationality in the museum is: " + str(listNationalitys[len(listNationalitys)-1][0]) + " with " + str(listNationalitys[len(listNationalitys)-1][1]) + " unique pieces" )
    
    print("The first and last 3 objects in the " + str(listNationalitys[len(listNationalitys)-1][0]) + " artwork list are...")
    print("")
    
    artworksNationality = controller.objectsByNacionality(catalog,str(listNationalitys[len(listNationalitys)-1][0]))
    sizeList = lt.size(artworksNationality)

    first3 = lt.subList(artworksNationality,sizeList-2,3)
    last3 = lt.subList(artworksNationality,1,3)

    for artwork in lt.iterator(first3):
        print('ObjectID: ' + artwork['ObjectID'] + ',  Title: ' +
             artwork['Title']  +  ', Medium: ' + artwork['Medium'] + ', Date: ' + artwork['Date'] +
             ', Dimensions: ' + artwork['Dimensions'] + ', Department: ' 
             + artwork['Department'] +  ', Classification: ' + artwork['Classification'] + 
             ', URL: ' + artwork['URL'])

    print("")

    for artwork in lt.iterator(last3):
        print('ObjectID: ' + artwork['ObjectID'] + ',  Title: ' +
             artwork['Title']  +  ', Medium: ' + artwork['Medium'] + ', Date: ' + artwork['Date'] +
             ', Dimensions: ' + artwork['Dimensions'] + ', Department: ' 
             + artwork['Department'] +  ', Classification: ' + artwork['Classification'] + 
             ', URL: ' + artwork['URL'])


def transportCostByDepartment():
    
    list = controller.transportCostByDepartment(catalog,department)[0]
    totalCost = controller.transportCostByDepartment(catalog,department)[1]
    totalWeight = controller.transportCostByDepartment(catalog,department)[2]
    totalArtworks = lt.size(list)
    print("The MoMA is going to transport " + str(totalArtworks) + " artifacts from the " + str(department) + " MoMA's department")
    print("REMEMBER!, NOT all MoMA´s data is complete!!!... These are estimates")
    print("Estimated cargo weight (kg): " + str(totalWeight))
    print("Estimated cargo cost (USD): " + str(totalCost))




    listByDate = controller.transportCostByDepartment(catalog,department)[0]
    listByCost = controller.transportCostByDepartment(catalog,department)[0]
    controller.sortArtworksCost(listByCost)
    controller.sortArtworksDate(listByDate)

    top5Expensive = lt.subList(listByCost,lt.size(listByCost)-5,5)
    top5Oldest = lt.subList(listByDate,1,5)
    
    print("")
    print("The most 5 expensive items to transport are...")
    
    for artwork in lt.iterator(top5Expensive):
        print('ObjectID: ' + artwork['ObjectID'] + ',  Title: ' +
             artwork['Title']  +  ', Medium: ' + artwork['Medium'] + ', Date: ' + artwork['Date'] +
             ', Dimensions: ' + artwork['Dimensions'] + ', Department: ' 
             + artwork['Department'] +  ', Classification: ' + artwork['Classification'] + 
             ', URL: ' + artwork['URL'])

    print("")
    print("The top 5 oldest items to transport are...")   

    for artwork in lt.iterator(top5Oldest):
        print('ObjectID: ' + artwork['ObjectID'] + ',  Title: ' +
             artwork['Title']  +  ', ArtistsNames: ' + artwork['ArtistsNames']+
              ', Medium: ' + artwork['Medium'] + ', Date: ' + artwork['Date'] +
             ', Dimensions: ' + artwork['Dimensions'] +  ', Classification: ' + artwork['Classification'] + 
             +  ', TransCost (USD): ' + artwork['cost'] + ', URL: ' + artwork['URL']) 
        

    
    
    



    

    




#Menu


def printMenu():
    print("Bienvenido")
    print("1- Load artists and artworks information")
    print("2- list chronologically artists born in a range of years") 
    print("3- list chronologically artworks by date acquired")
    print("4- Artworks of an artist by technique") 
    print("5- Nationalitys with most artworks")
    print("6- Artworks cost by department")
    print("0- Salir")

catalog = None

while True:
    printMenu()
    inputs = input('Select an option to continue\n')
    if int(inputs[0]) == 1:
        print("Loading files information ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Arstists loaded: ' + str(lt.size(catalog['artists'])))
        print('Artworks loaded: ' + str(lt.size(catalog['artworks'])))
        


    elif int(inputs[0]) == 2:
        date01 = int(input('First year (YYYY) '))
        date02 = int(input('Last year (YYYY) '))
        artistsByDates()

    elif int(inputs[0]) == 3:
        date01 = int(input('First Date (AAAAMMDD) '))
        date02 = int(input('Last Date  (AAAAMMDD) '))
        artworksByDateAquired()     

    elif int(inputs[0]) == 4:
        artist = input("Enter the artist name ")
        artworkArtistByTechnique()


    elif int(inputs[0]) == 5:
        byNationality()
    

    elif int(inputs[0]) == 6:
        department = input("Enter department ")
        transportCostByDepartment()

    elif int(inputs[0]) == 7:
        print(catalog['artworks'])   
        

    else:
        sys.exit(0)
        

