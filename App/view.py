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
    print("2- los n videos con más LIKES para el nombre de una categoría " +
          "específica")
    print("3- Salir")


def initCatalog():
    return controller.initCatalog()


def loadData(catalog):
    return controller.loadData(catalog)


def printVideos1(videos, cantidad):
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
              "Memoria [kB]: ", f"{answer[1]:.3f}")

    elif int(inputs[0]) == 2:
        categoria = input("Seleccione una categoria: ")
        top = input('Top?: ')
        categoryID = controller.getCategoryid(catalog, categoria)
        lista = controller.sortVideos(catalog, categoryID)
        printVideos1(lista, int(top))

    else:
        sys.exit(0)
sys.exit(0)
