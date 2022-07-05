def obtener_nombre(ruta):
    """
    Se realiza la extracción del nombre de un fichero dada la ruta donde se
    encuentra.

    Parameters
    ----------
    ruta : str
        Cadena de texto que contiene la ruta dónde se encuentra el fichero

    Returns
    -------
    str
        Cadena de texto que contiene el nombre del fichero.
    """

    nombre_fichero = ruta[::-1]

    indice = 0
    while nombre_fichero[indice] != "/":
        indice += 1

    nombre_fichero = nombre_fichero[0:indice][::-1]

    return nombre_fichero


def conversor_aeropueros(lista_original):
    """
    Se realiza la conversión de los nombres de los aeropuertos en sus
    correspondientes códigos de la IATA.

    Parameters
    ----------
    lista_original : list
        Lista que contiene nombres de aeropuertos

    Returns
    -------
    list
        Lista que contiene los aeropuertos convertidos a código IATA.
    """

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
