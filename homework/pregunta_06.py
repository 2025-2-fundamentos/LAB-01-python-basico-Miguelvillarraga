"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    valores = {}

    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split(",")
            col5 = columnas[4]
            pares = col5.split(",")

            for par in pares:
                clave, valor = par.split(":")
                valor = int(valor)

                if clave not in valores:
                    valores[clave] = {"min": valor, "max": valor}
                else:
                    if valor < valores[clave]["min"]:
                        valores[clave]["min"] = valor
                    if valor > valores[clave]["max"]:
                        valores[clave]["max"] = valor

    resultado = []
    for clave in sorted(valores.keys()):
        resultado.append((clave, valores[clave]["min"], valores[clave]["max"]))

    return resultado
