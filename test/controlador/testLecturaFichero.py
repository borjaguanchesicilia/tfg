import sys
sys.path.insert(1, './')
#sys.path.insert(1, '/home/borja/Desktop/tfg/proyecto')
from src.modelo.lecturaFichero import *

fichero = FicheroCsv("./ficheros/aviones.csv")


def testGetFilas():

    assert fichero.getFilas() == 38


def testGetColumnas():

    assert fichero.getColumnas() == 3


def testGetCabecera():

    assert fichero.getCabecera(1) == 'asientos'


def testGetElemento():

    assert fichero.getElemento('asientos', 1) == 180