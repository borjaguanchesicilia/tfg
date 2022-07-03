def obtener_nombre(ruta):

    nombre_fichero = ruta[::-1]

    indice = 0
    while nombre_fichero[indice] != "/":
        indice += 1

    nombre_fichero = nombre_fichero[0:indice][::-1]

    return nombre_fichero


def conversor_aeropueros(lista_original):
    conversor_aeropuertos = {
        "Arrecife": "ACE",
        "Fuerteventura": "FUE",
        "Gran Canaria": "LPA",
        "Tenerife Norte": "TFN",
        "Tenerife Sur": "TFS",
        "La Palma": "SPC",
    }

    lista_conversion = [conversor_aeropuertos[aer] for aer in lista_original]

    return lista_conversion
