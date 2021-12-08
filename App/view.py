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

def printInfo(lista):
    i=1
    while i!=6:
        ae=lt.getElement(lista,i)
        info=ae[2]
        iata,nombre,ciudad,pais=info['IATA'],info['Name'],info['City'],info['Country']
        print("\nNombre: "+nombre+"\nIATA: "+iata+"\nPais: "+pais+"\nCiudad: "+ciudad+"\n")
        print("***********************************************************************************************")
        i+=1

def printInfo(lst,num1,num2,total):
    if lt.size(lst)>=total:
        i=num1
        j=lt.size(lst)-num2
        avi=True
        while avi:
            if i!=4:
                avistamientoActual=lt.getElement(lst,i)
                i+=1
            else:
                avistamientoActual=lt.getElement(lst,j)
                j+=1
                if j==lt.size(lst)+1:
                    avi=False
            fechaHora,ciudad,pais,duracion,forma,longitud,latitud=avistamientoActual['datetime'],avistamientoActual['city'].title(),avistamientoActual['country'].upper(),avistamientoActual['duration (seconds)'],avistamientoActual['shape'],avistamientoActual['longitude'],avistamientoActual['latitude']
            if fechaHora=="":
                fechaHora="Desconocidas"
            if ciudad=="":
                ciudad="Desconocida"
            if pais=="":
                pais="Desconocido"
            if duracion=="":
                duracion="Desconocida"
            if forma=="":
                forma="Forma desconocida"
            print("- Fecha y hora del avistamiento: "+fechaHora+"\n- Pais: "+pais+"\n- Ciudad: "+ciudad+"\n- Duracion: "+duracion+" segundos\n- Forma: "+forma.title()+"\n- Longitud: "+str(longitud)+"\n- Latitud: "+str(latitud)+"\n_________________________________________________________________________________________________________________________\n")
    else:
        for avis in lt.iterator(lst):
            fechaHora,ciudad,pais,duracion,forma,longitud,latitud=avis['datetime'],avis['city'].title(),avis['country'].upper(),avis['duration (seconds)'],avis['shape'],avis['longitude'],avis['latitude']
            if fechaHora=="":
                fechaHora="Desconocidas"
            if ciudad=="":
                ciudad="Desconocida"
            if pais=="":
                pais="Desconocido"
            if duracion=="":
                duracion="Desconocida"
            if forma=="":
                forma="Forma desconocida"

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
        print("Poblacion: "+poblacion+"\nLatitud: "+lati+"\nLongitud: "+long+"\n_____________________________________________________________________________________________________")
    elif int(inputs[0]) == 2:
        aeropuertos=controller.interconectados(catalogo)
        num=aeropuertos[1]
        lista=aeropuertos[0]
        print("\nExisten "+str(num)+" aeropuertos interconectados\n")
        print("***********************************************************************************************")
        printInfo(lista)
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
        print((catalogo['cities']))
    elif int(inputs[0]) == 5:
        millas=int(input("Ingrese las millas disponibles: \n"))
        ciudad=input("Ingrese la ciudad de origen:\n")
        controller.millasUsuario(catalogo,millas,ciudad)
    elif int(inputs[0]) == 6:
        aeropuerto=input('Ingrese el codigo IATA del aeropuerto: \n')
        lista=controller.aeropuertoCerrado(catalogo,aeropuerto)
        print(lista)
    else:
        sys.exit(0)
sys.exit(0)
