"""
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
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos
listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def newCatalog():
    catalog = {'video': None,
               'categoryID': None,
               'categoryByVideos': None}

    catalog['video'] = lt.newList('ARRAY_LIST')
    catalog['categoryID'] = mp.newMap(37,
                                      maptype='CHAINING',
                                      loadfactor=1.2)
    catalog['categoryByVideos'] = mp.newMap(37,
                                            maptype='CHAINING',
                                            loadfactor=1.2)
    return catalog


# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    lt.addLast(catalog['video'], video)
    addVideoCategory(catalog, video)


def addCategoryID(catalog, category):
    mp.put(catalog['categoryID'], category['name'], category['id'])


def addVideoCategory(catalog, video):
    cat = catalog['categoryByVideos']
    if (video['category_id'] != ''):
        cat1 = video['category_id']

    existcat = mp.contains(cat, cat1)
    if existcat:
        entry = mp.get(cat, cat1)
        dic = me.getValue(entry)
    else:
        dic = newId(cat1)
        mp.put(cat, cat1, dic)
    lt.addLast(dic['videos'], video)


def newId(id):
    entry = {'id': "", "videos": None}
    entry['id'] = id
    entry['videos'] = lt.newList('SINGLE_LINKED')
    return entry


# Funciones para creacion de datos


# Funciones de consulta


def getCategoryid(catalog, category):
    cat = mp.get(catalog['categoryID'], " " + category)
    element = me.getValue(cat)
    return element


# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByLikes(video1, video2):
    return (int(video1['likes']) > (int(video2['likes'])))


# Funciones de ordenamiento


def sortVideos(catalog, id):
    entry = mp.get(catalog['categoryByVideos'], id)
    sub_list = me.getValue(entry)['videos']
    sub_list = sub_list.copy()
    sorted_list = ms.sort(sub_list, cmpVideosByLikes)
    return sorted_list
