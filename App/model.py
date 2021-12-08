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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.ADT import graph as gr
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Graphs import scc
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def initCatalog():
    catalogo={"airports":None,"routes":None,"routesDi":None,"cities":None}
    catalogo["airports"]=mp.newMap(9076,maptype="PROBING",loadfactor=0.5)
    catalogo["routes"]=gr.newGraph(directed=True,size=92606)
    catalogo["routesDi"]=gr.newGraph(datastructure="ADJ_LIST",directed=False,size=92606)
    catalogo["cities"]=mp.newMap(41001,maptype="CHAINING",loadfactor=8.0)
    return catalogo
    
# Funciones para agregar informacion al catalogo

def addAirport(catalogo,airport):
    ap=airport["IATA"]
    gr.insertVertex(catalogo["routes"],ap)
    mp.put(catalogo["airports"],airport["IATA"],airport)

def addRoute(catalogo,route):
    airport=route["Departure"]
    destination=route["Destination"]
    peso=route["distance_km"]
    gr.addEdge(catalogo["routes"],airport,destination,peso)

def addRouteDi(catalogo,route):
    airport=route["Departure"]
    dest=route["Destination"]
    adjAirport=gr.adjacents(catalogo["routes"],airport)
    adjDest=gr.adjacents(catalogo["routes"],dest)
    #vertices=gr.vertices(catalogo["routesDi"])
    if lt.isPresent(adjAirport,dest) and lt.isPresent(adjDest,airport):
        if gr.containsVertex(catalogo["routesDi"],airport)!=True:
            gr.insertVertex(catalogo["routesDi"],airport)
        if gr.containsVertex(catalogo["routesDi"],dest)!=True:
            gr.insertVertex(catalogo["routesDi"],dest)
        gr.addEdge(catalogo["routesDi"],airport,dest)

def addCity(catalogo,ciudad):
    ct=ciudad["city"]
    if not mp.contains(catalogo["cities"],ct):
        ciudades=lt.newList("SINGLE_LINKED")
        lt.addLast(ciudades,ciudad)
        mp.put(catalogo["cities"],ct,ciudades)
    else:
        ciudades1=me.getValue(mp.get(catalogo["cities"],ct))
        lt.addLast(ciudades1,ciudad)

def sizes(catalogo):
    routesSize=gr.numVertices(catalogo["routes"])
    routesDiSize=gr.numEdges(catalogo["routesDi"])
    citiesSize=mp.size(catalogo["cities"])
    primer=me.getValue(mp.get(catalogo["airports"],"primer"))
    ultima=me.getValue(mp.get(catalogo["cities"],"ultimo"))
    return routesSize,routesDiSize,citiesSize,primer,ultima

def primerCargado(catalogo,ai):
    mp.put(catalogo["airports"],"primer",ai)

def ultimo(catalogo,ct):
    mp.put(catalogo["cities"],"ultimo",ct)

# Funciones para creacion de datos

# Funciones de consulta

def interconectados(catalogo):
    aeropuertosInterconectados=gr.vertices(catalogo["routesDi"])
    aeroConectados=lt.newList("ARRAY_LIST")
    for aeropuerto in lt.iterator(aeropuertosInterconectados):
        adyacentes=gr.adjacents(catalogo["routesDi"],aeropuerto)
        num=lt.size(adyacentes)
        info=me.getValue(mp.get(catalogo["airports"],aeropuerto))
        lt.addLast(aeroConectados,(aeropuerto,num,info))
    aeroConectados=sa.sort(aeroConectados,cmpInterconectados)
    return aeroConectados,lt.size(aeroConectados)

def fuertementeConectados(catalogo,v1,v2):
    componentesConectados=scc.KosarajuSCC(catalogo["routes"])
    conectados=scc.stronglyConnected(componentesConectados,v1,v2)
    air1=(me.getValue(mp.get(catalogo["airports"],v1)))["Name"]
    air2=(me.getValue(mp.get(catalogo["airports"],v2)))["Name"]
    numScc=scc.connectedComponents(componentesConectados)
    return numScc,conectados,air1,air2

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpInterconectados(ap1,ap2):
    return ap1[1]>ap2[1]

# Funciones de ordenamiento

#--------------------------------------------------------------------------------------------------
''' '''