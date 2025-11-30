"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    resultado = {}
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            letra_columna_1 = columnas[0]
            suma_columna_5 = sum(int(valor.split(":")[1]) for valor in columnas[4].split(","))
            if letra_columna_1 in resultado:
                resultado[letra_columna_1] += suma_columna_5
            else:
                resultado[letra_columna_1] = suma_columna_5
    return resultado
