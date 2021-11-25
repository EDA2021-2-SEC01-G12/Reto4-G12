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
        print("Total de aeropuertos que cuentan con rutas de ida y vuelta con otros aeropuertos: "+str(rds))
        print("Total de ciudades registradas: "+str(cs)+"\n_____________________________________________________________________________________________________")
        nombreAeropuerto,cod,ciudad,pais,lat,lon=primer["Name"],primer["IATA"],primer["City"],primer["Country"],primer["Latitude"],primer["Longitude"]
        city,poblacion,lati,long=ultima["city"],ultima["population"],ultima["lat"],ultima["lng"]
        print("\nEl primer aeropuerto registrado es el "+nombreAeropuerto+" ("+cod+"):\n")
        print("Ciudad: "+ciudad+"\nPais: "+pais+"\nLatitud: "+lat+"\nLongitud: "+lon+"\n_____________________________________________________________________________________________________")
        print("\nLa ultima ciudad registrada es "+city+":\n")
        print("Poblacion: "+poblacion+"\nLatitud: "+lati+"\nLongitud: "+long+"\n_____________________________________________________________________________________________________")
    elif int(inputs[0]) == 2:
        pass
    else:
        sys.exit(0)
sys.exit(0)
