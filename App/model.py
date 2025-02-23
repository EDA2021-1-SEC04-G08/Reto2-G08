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
    catalog['countryByVideos'] = mp.newMap(100,
                                           maptype='CHAINING',
                                           loadfactor=1.2)
    return catalog
# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    lt.addLast(catalog['video'], video)
    addVideoCategory(catalog, video)
    addVideoCountry(catalog, video)


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


def addVideoCountry(catalog, video):
    cou = catalog['countryByVideos']
    if (video['country'] != ''):
        cou1 = video['country']

    existcou = mp.contains(cou, cou1)
    if existcou:
        entry = mp.get(cou, cou1)
        dic = me.getValue(entry)
    else:
        dic = newCountry(cou1)
        mp.put(cou, cou1, dic)
    lt.addLast(dic['videos'], video)


def newCountry(country):
    entry = {'country': "", "videos": None}
    entry['country'] = country
    entry['videos'] = lt.newList('SINGLE_LINKED')
    return entry

# Funciones para creacion de datos


def sublistByCategory(lista, id, top):
    size = lt.size(lista)
    sublist = lt.newList('ARRAY_LIST')
    i = 0
    T = 0

    while i < size:
        video = lt.getElement(lista, i)
        id1 = video['category_id']

        if id1 == id:
            lt.addLast(sublist, video)
            T += 1

        if T == int(top):
            break

        i += 1

    return sublist


def sublistByTags(lista, tag, top):
    size = lt.size(lista)
    sublist = lt.newList('ARRAY_LIST')
    tag = tag.lower()
    i = 0
    T = 0

    while i < size:
        video = lt.getElement(lista, i)
        tag1 = video['tags'].lower()

        if tag in tag1:
            lt.addLast(sublist, video)
            T += 1

        if T == int(top):
            break

        i += 1

    return sublist

# Funciones de consulta


def getCategoryid(catalog, category):
    cat = mp.get(catalog['categoryID'], " " + category)
    element = me.getValue(cat)
    return element


def getTendencyByCountry(catalog, country):
    entry = mp.get(catalog['countryByVideos'], country)
    sub_list = me.getValue(entry)['videos']
    size = lt.size(sub_list)
    i = 0
    dic = {}

    while i < size:
        video = lt.getElement(sub_list, i)
        video_id = video['video_id']
        t_date = video['trending_date']
        days = 1

        if video_id not in dic:
            j = 0
            while j < size:
                video2 = lt.getElement(sub_list, j)
                video_id2 = video2['video_id']
                t_date2 = video2['trending_date']

                if (t_date != t_date2) and (video_id == video_id2):
                    days += 1
                j += 1

            dic[video_id] = days

        i += 1
        return dic


def mostDaysByCountry(catalog, country):
    dic = getTendencyByCountry(catalog, country)
    lista = dic.values()
    maximo = max(lista)
    llave = 0
    for elemento in dic:
        valor = dic[elemento]
        if valor == maximo:
            llave = elemento
            break

    entry = mp.get(catalog['countryByVideos'], country)
    sub_list = me.getValue(entry)['videos']
    size = lt.size(sub_list)
    i = 0

    while i < size:
        video2 = lt.getElement(sub_list, i)
        video_id = video2['video_id']

        if video_id == llave:
            return (video2, maximo)
        i += 1


def getTendencyByCategory(catalog, id):
    entry = mp.get(catalog['categoryByVideos'], id)
    sub_list = me.getValue(entry)['videos']
    size = lt.size(sub_list)
    i = 0
    dic = {}

    while i < size:
        video = lt.getElement(sub_list, i)
        video_id = video['video_id']
        t_date = video['trending_date']
        days = 1

        if video_id not in dic:
            j = 0
            while j < size:
                video2 = lt.getElement(sub_list, j)
                video_id2 = video2['video_id']
                t_date2 = video2['trending_date']

                if (t_date != t_date2) and (video_id == video_id2):
                    days += 1
                j += 1

            dic[video_id] = days

        i += 1
        return dic


def mostDaysByCategory(catalog, id):
    dic = getTendencyByCategory(catalog, id)
    lista = dic.values()
    maximo = max(lista)
    llave = 0
    for elemento in dic:
        valor = dic[elemento]
        if valor == maximo:
            llave = elemento
            break

    entry = mp.get(catalog['categoryByVideos'], id)
    sub_list = me.getValue(entry)['videos']
    size = lt.size(sub_list)
    i = 0

    while i < size:
        video2 = lt.getElement(sub_list, i)
        video_id = video2['video_id']

        if video_id == llave:
            return (video2, maximo)
        i += 1

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByLikes(video1, video2):
    return (int(video1['likes']) > (int(video2['likes'])))


def cmpVideosByViews(video1, video2):
    return (int(video1['views']) > (int(video2['views'])))


# Funciones de ordenamiento


def sortVideosByLikes(catalog, id):
    entry = mp.get(catalog['categoryByVideos'], id)
    sub_list = me.getValue(entry)['videos']
    sub_list = sub_list.copy()
    sorted_list = ms.sort(sub_list, cmpVideosByLikes)
    return sorted_list


def sortVideosByLikesAndTags(catalog, pais):
    entry = mp.get(catalog['countryByVideos'], pais)
    sub_list = me.getValue(entry)['videos']
    sub_list = sub_list.copy()
    sorted_list = ms.sort(sub_list, cmpVideosByLikes)
    return sorted_list


def sortVideosByViews(catalog, pais):
    entry = mp.get(catalog['countryByVideos'], pais)
    sub_list = me.getValue(entry)['videos']
    sub_list = sub_list.copy()
    sorted_list = ms.sort(sub_list, cmpVideosByViews)
    return sorted_list
