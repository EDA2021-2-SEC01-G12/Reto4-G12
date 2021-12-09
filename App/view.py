"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as mp

default_limit = 1000 
sys.setrecursionlimit(default_limit*10)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def initCatalog():
    return controller.initCatalog()

def sizes(catalogo):
    return controller.sizes(catalogo)

def printInfo5(lista):
    i=1
    while i!=6:
        ae=lt.getElement(lista,i)
        info=ae[2]
        iata,nombre,ciudad,pais=info['IATA'],info['Name'],info['City'],info['Country']
        print("Nombre: "+nombre+"\nIATA: "+iata+"\nPais: "+pais+"\nCiudad: "+ciudad+"\n")
        print("_____________________________________________________________________________________________________\n")
        i+=1

def printInfo(lst,num1,num2,total):
    if lt.size(lst)>=total:
        i=num1
        j=lt.size(lst)-num2
        avi=True
        while avi:
            if i!=4:
                info=lt.getElement(lst,i)[1]
                i+=1
            else:
                info=lt.getElement(lst,j)[1]
                j+=1
                if j==lt.size(lst)+1:
                    avi=False
            iata,nombre,ciudad,pais=info['IATA'],info['Name'],info['City'],info['Country']
            print("Nombre: "+nombre+"\nIATA: "+iata+"\nPais: "+pais+"\nCiudad: "+ciudad+"\n_____________________________________________________________________________________________________\n")
    else:
        for info in lt.iterator(lst):
            info=info[1]
            iata,nombre,ciudad,pais=info['IATA'],info['Name'],info['City'],info['Country']
            print("Nombre: "+nombre+"\nIATA: "+iata+"\nPais: "+pais+"\nCiudad: "+ciudad+"\n_____________________________________________________________________________________________________\n")

def printCiudad(lista,ciudades,tipo):
    if tipo=="city":
        i=1
        for c in lt.iterator(lista):
            ciudad,pais,long,lat,poblacion=c["city"],c["country"],c["lng"],c["lat"],c["population"]
            print(str(i)+".\nNombre: "+ciudad+"\nPais: "+pais+"\nPoblacion: "+poblacion+"\nLongitud: "+long+"\nLatitud: "+lat+"\n_____________________________________________________________________________________________________\n")
            ciudades[i]=c
            i+=1
    else:
        i=1
        for c in lt.iterator(lista):
            ciudad,pais,long,lat,nombre,iata=c["City"],c["Country"],c["Longitude"],c["Latitude"],c["Name"],c["IATA"]
            print(str(i)+".\nNombre: "+nombre+"\nCiudad: "+ciudad+"\nPais: "+pais+"\nIATA: "+iata+"\nLongitud: "+long+"\nLatitud: "+lat+"\n_____________________________________________________________________________________________________\n")
            ciudades[i]=c
            i+=1

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar puntos de interconexión aérea")
    print("3- Encontrar clústeres de tráfico aéreo")
    print("4- Encontrar la ruta más corta entre ciudades")
    print("5- Utilizar las millas de viajero")
    print("6- Cuantificar el efecto de un aeropuerto cerrado")
    print("0- Salir")

catalogo = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalogo=initCatalog()
        controller.addAirport(catalogo)
        controller.addRoute(catalogo)
        controller.addCiudad(catalogo)
        rs,rds,cs,primer,ultima=sizes(catalogo)
        print("\nTotal de aeropuertos disponibles: "+str(rs))
        print("Total de rutas entre aeropuertos que cuentan con vuelos de ida y vuelta: "+str(rds))
        print("Total de ciudades registradas: "+str(cs)+"\n_____________________________________________________________________________________________________")
        nombreAeropuerto,cod,ciudad,pais,lat,lon=primer["Name"],primer["IATA"],primer["City"],primer["Country"],primer["Latitude"],primer["Longitude"]
        city,poblacion,lati,long=ultima["city"],ultima["population"],ultima["lat"],ultima["lng"]
        print("\nEl primer aeropuerto registrado es el "+nombreAeropuerto+" ("+cod+"):\n")
        print("Ciudad: "+ciudad+"\nPais: "+pais+"\nLatitud: "+lat+"\nLongitud: "+lon+"\n_____________________________________________________________________________________________________")
        print("\nLa ultima ciudad registrada es "+city+":\n")
        print("Poblacion: "+poblacion+"\nLatitud: "+lati+"\nLongitud: "+long+"\n_____________________________________________________________________________________________________\n")
    elif int(inputs[0]) == 2:
        aeropuertos=controller.interconectados(catalogo)
        num=aeropuertos[1]
        lista=aeropuertos[0]
        print("\nExisten "+str(num)+" aeropuertos interconectados\n")
        print("_____________________________________________________________________________________________________\n")
        printInfo5(lista)
    elif int(inputs[0]) == 3:
        v1=input("Ingrese el codigo IATA del aeropuerto 1:\n")
        v2=input("Ingrese el codigo IATA del aeropuerto 2:\n")
        componentes=controller.fuertementeConectados(catalogo,v1,v2)
        numComponentes=componentes[0]
        com=componentes[1]
        print("\nExisten "+str(numComponentes)+" clusteres aereos")
        if com==False:
            print("\nLos aeropuertos "+componentes[2]+" y "+componentes[3]+" no pertenecen al mismo cluster\n")
        else:
            print("\nLos aeropuertos "+componentes[2]+" y "+componentes[3]+" pertenecen al mismo cluster\n")
    elif int(inputs[0]) == 4:
        origen=False
        destino=False
        while not origen:
            ciudadOrigen=input("Ingrese la ciudad de origen:\n")
            ciudad1=controller.buscarCiudades(catalogo,ciudadOrigen)
            if ciudad1!=None:
                if lt.size(ciudad1)>1:
                    print("\nSe encontaron "+str(lt.size(ciudad1))+" ciudades con el nombre de "+ciudadOrigen+"\n")
                    ciudadesOrigen={}
                    print("_____________________________________________________________________________________________________\n")
                    printCiudad(ciudad1,ciudadesOrigen,"city")
                    ciudad1Opcion=int(input("Seleccione cual desea consultar:\n"))
                    ciudad1=ciudadesOrigen[ciudad1Opcion]
                else:
                    ciudad1=lt.getElement(ciudad1,1)
                origen=True
                aerosOrigen=controller.buscarAerosCiudad(catalogo,ciudad1)
                if lt.size(aerosOrigen)>1:
                    print("\nSe encontaron "+str(lt.size(aerosOrigen))+" aeropuertos en "+ciudadOrigen+"\n")
                    aeros={}
                    print("_____________________________________________________________________________________________________\n")
                    printCiudad(aerosOrigen,aeros,"aero")
                    aero1Opcion=int(input("Seleccione cual desea consultar:\n"))
                    aerosOrigen=aeros[aero1Opcion]
                else:
                    aerosOrigen=lt.getElement(aerosOrigen,1)
            else:
                print("La ciudad ingresada no existe")
        while not destino:
            ciudadDestino=input("Ingrese la ciudad de destino:\n")
            ciudad2=controller.buscarCiudades(catalogo,ciudadDestino)
            if ciudad2!=None:
                if lt.size(ciudad2)>1:
                    ciudadesDestino={}
                    print("\nSe encontaron "+str(lt.size(ciudad2))+" ciudades con el nombre de "+ciudadDestino+", seleccione cual desea consultar:\n")
                    print("_____________________________________________________________________________________________________\n")
                    printCiudad(ciudad2,ciudadesDestino,"city")
                    ciudad2Opcion=int(input("Seleccione cual desea consultar:\n"))
                    ciudad2=ciudadesDestino[ciudad2Opcion]
                else:
                    ciudad2=lt.getElement(ciudad2,1)
                destino=True
                aerosDestino=controller.buscarAerosCiudad(catalogo,ciudad2)
                if lt.size(aerosDestino)>1:
                    print("\nSe encontaron "+str(lt.size(aerosDestino))+" aeropuertos en "+ciudadDestino+"\n")
                    aeros2={}
                    print("_____________________________________________________________________________________________________\n")
                    printCiudad(aerosDestino,aeros2,"aero")
                    aero2Opcion=int(input("Seleccione cual desea consultar:\n"))
                    aerosDestino=aeros[aero2Opcion]
                else:
                    aerosDestino=lt.getElement(aerosDestino,1)
            else:
                print("La ciudad ingresada no existe")
        if ciudad1!=None and ciudad2!=None:
            ruta=controller.rutaMinimaCiudades(catalogo,ciudad1,ciudad2)
        print("\nAeropuerto de salida: "+aerosOrigen["Name"]+"\n\nCiudad: "+aerosOrigen["City"]+"\nPais: "+aerosOrigen["Country"]+"\nLongitud: "+aerosOrigen["Longitude"]+"\nLatitud: "+aerosOrigen["Latitude"]+"\nIATA: "+aerosOrigen["IATA"])
        print("\nAeropuerto de llegada: "+aerosDestino["Name"]+"\n\nCiudad: "+aerosDestino["City"]+"\nPais: "+aerosDestino["Country"]+"\nLongitud: "+aerosDestino["Longitude"]+"\nLatitud: "+aerosDestino["Latitude"]+"\nIATA: "+aerosDestino["IATA"])
    elif int(inputs[0]) == 5:
        millas=int(input("Ingrese las millas disponibles: \n"))
        ciudad=input("Ingrese la ciudad de origen:\n")
        controller.millasUsuario(catalogo,millas,ciudad)
    elif int(inputs[0]) == 6:
        aeropuerto=input('Ingrese el codigo IATA del aeropuerto: \n')
        lista=controller.aeropuertoCerrado(catalogo,aeropuerto)
        print("\nLos aeroepuertos afectados por cerrar el "+lista[1]+"\n")
        print("_____________________________________________________________________________________________________\n")
        printInfo(lista[0],1,2,6)
    elif int(inputs[0]) == 0:
        sys.exit(0)
    else:
        print("Seleccione una opcion valida")
sys.exit(0)
