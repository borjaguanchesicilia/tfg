import sys

sys.path.insert(1, "./")
# sys.path.insert(1, '/home/borja/Desktop/tfg/proyecto')
from src.controlador.c_lectura_fichero import *

fichero = FicheroCsv("./ficheros/aviones.csv")


def test_get_filas():

    assert fichero.get_filas() == 38


def test_get_columnas():

    assert fichero.get_columnas() == 3


def test_get_cabecera():

    assert fichero.get_cabecera(1) == "asientos"


def test_get_elemento():

    assert fichero.get_elemento("asientos", 1) == 180
