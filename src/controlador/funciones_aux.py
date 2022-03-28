def obtener_nombre(ruta):

    nombre_fichero = ruta[::-1]

    indice = 0
    while nombre_fichero[indice] != "/":
        indice += 1

    nombre_fichero = nombre_fichero[0:indice][::-1]

    return nombre_fichero
