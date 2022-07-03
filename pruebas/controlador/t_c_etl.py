from pruebas.configuracion_test import *


controlador_etl.set_fichero_aviones(vista_etl.get_etiqueta_fichero_aviones(), "./ficheros/aviones.csv")
controlador_etl.set_fichero_vuelos(vista_etl.get_etiqueta_fichero_vuelos(), "./ficheros/geslot_marzo_22.csv")

def test_get_fichero_aviones():
    assert controlador_etl.get_fichero_aviones().empty == False

def test_get_fichero_vuelos():
    assert controlador_etl.get_fichero_vuelos().empty == False