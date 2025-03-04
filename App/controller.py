﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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

from App.model import fuertementeConectados
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    return model.initCatalog()

# Funciones para la carga de datos

def addAirport(catalogo):
    airportsFile = cf.data_dir + "airports-utf8-small.csv"
    airports = csv.DictReader(open(airportsFile, encoding="utf-8"),delimiter=",")
    primer=None
    for ai in airports:
        if primer==None:
            model.primerCargado(catalogo,ai)
            primer=ai
        model.addAirport(catalogo,ai)
        model.addAirCity(catalogo,ai)

def addRoute(catalogo):
    routesFile = cf.data_dir + "routes-utf8-small.csv"
    routes = csv.DictReader(open(routesFile, encoding="utf-8"),delimiter=",")
    for rt in routes:
        model.addRoute(catalogo,rt)
        model.addRouteDi(catalogo,rt)

def addCiudad(catalogo):
    citiesFile = cf.data_dir + "worldcities-utf8.csv"
    cities = csv.DictReader(open(citiesFile, encoding="utf-8"),delimiter=",")
    contador=0
    for ct in cities:
        model.addCity(catalogo,ct)
        contador+=1
        if contador==41001:
            model.ultimo(catalogo,ct)

def sizes(catalogo):
    return model.sizes(catalogo)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def interconectados(catalogo):
    return model.interconectados(catalogo)

def fuertementeConectados(catalogo,v1,v2):
    return model.fuertementeConectados(catalogo,v1,v2)

def millasUsuario(catalogo,millas,v1):
    return model.millasUsuario(catalogo,millas,v1)

def aeropuertoCerrado(catalogo,iata):
    return model.aeropuertoCerrado(catalogo,iata)

def buscarCiudades(catalogo,ciudad):
    return model.buscarCiudades(catalogo,ciudad)

def buscarAerosCiudad(catalogo,ciudad):
    return model.buscarAerosCiudad(catalogo,ciudad)

def rutaMinimaCiudades(catalogo,ciudad1,ciudad2):
    return model.rutaMinimaCiudades(catalogo,ciudad1,ciudad2)
