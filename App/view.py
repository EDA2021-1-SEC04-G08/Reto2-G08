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


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Los n videos con más LIKES para el nombre de una categoría " +
          "específica")
    print("3- Los mejores videos por categoria y pais (views)")
    print("4- Encontrar video tendencia por pais")
    print("5- Encontrar video tendencia por categoria")
    print("6- Buscar videos con mas likes")
    print("7- Salir")


def initCatalog():
    return controller.initCatalog()


def loadData(catalog):
    return controller.loadData(catalog)


def printVideosByLikes(videos, cantidad):
    size = lt.size(videos)
    if size > cantidad:
        print(' Estos son los mejores videos: ')
        i = 0
        while i <= cantidad-1:
            video = lt.getElement(videos, i)
            print('Titulo: ' + video['title'])
            i += 1
    else:
        print('No se encontraron videos')


def printVideosByViews(videos, cantidad):
    size = lt.size(videos)
    if size == cantidad:
        print(' Estos son los mejores videos: ')
        i = 0
        while i <= cantidad-1:
            video = lt.getElement(videos, i)
            print('Titulo: ' + video['title'] + ', Trending Date:' +
                  video['trending_date'] + ', Nombre del canal:' +
                  video['channel_title'] + ', Publish Time:' +
                  video['publish_time'] + ', Reproducciones:' +
                  video['views'] + ', Likes:' + video['likes'] +
                  ', Dislikes:' + video['dislikes'])
            i += 1
    else:
        print('No se encontraron videos')


def printTendencyByCountry(video):
    video2 = video[0]
    dias = video[1]
    print('Titulo: ' + video2['title'] + ', Nombre del canal:' +
          video2['channel_title'] + ', Pais:' +
          video2['country'] + ', Dias que estuvo en tendencia:' +
          str(dias))


def printTendencyByCategory(video):
    video2 = video[0]
    dias = video[1]
    print('Titulo: ' + video2['title'] + ', Nombre del canal:' +
          video2['channel_title'] + ', ID de la categoria:' +
          video2['category_id'] + ', Dias que estuvo en tendencia:' +
          str(dias))


def printVideosByTags(videos, cantidad):
    size = lt.size(videos)
    if size <= cantidad:
        print(' Estos son los mejores videos: ')
        i = 0
        while i < size:
            video = lt.getElement(videos, i)
            print('Titulo: ' + video['title'] + ', Nombre del canal:' +
                  video['channel_title'] + ', Publish Time:' +
                  video['publish_time'] + ', Reproducciones:' +
                  video['views'] + ', Likes:' + video['likes'] +
                  ', Dislikes:' + video['dislikes'] + ', tags: '
                  + video['tags'])
            i += 1
    else:
        print('No se encontraron videos')


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        answer = loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['video'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categoryID'])))
        print("\nTiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}\n")

    elif int(inputs[0]) == 2:
        categoria = input("Seleccione una categoria: ")
        top = input('¿Top?: ')
        categoryID = controller.getCategoryid(catalog, categoria)
        lista = controller.sortVideosByLikes(catalog, categoryID)
        printVideosByLikes(lista, int(top))

    elif int(inputs[0]) == 3:
        categoria = input("Seleccione una categoria: ")
        pais = input("Seleccione un pais: ")
        top = input('¿Top?: ')
        categoryID = controller.getCategoryid(catalog, categoria)
        lista = controller.sortVideosByViews(catalog, pais)
        masVistos = controller.sublistByCategory(lista, categoryID, top)
        printVideosByViews(masVistos, int(top))

    elif int(inputs[0]) == 4:
        pais = input("Seleccione un pais: ")
        video = controller.mostDaysByCountry(catalog, pais)
        printTendencyByCountry(video)

    elif int(inputs[0]) == 5:
        categoria = input("Seleccione una categoria: ")
        categoryID = controller.getCategoryid(catalog, categoria)
        video = controller.mostDaysByCategory(catalog, categoryID)
        printTendencyByCategory(video)

    elif int(inputs[0]) == 6:
        pais = input("Seleccione un pais: ")
        tag = input('Ingrese un tag: ')
        top = input('¿Top?: ')
        lista = controller.sortVideosByLikesAndTags(catalog, pais)
        masLikes = controller.sublistByTags(lista, tag, top)
        printVideosByTags(masLikes, int(top))

    else:
        sys.exit(0)
sys.exit(0)
