from src.modelo.operaciones.lectura_fichero import FicheroCsv
from pruebas.configuracion_test import *


cabeceras = ["codigo_IATA", "asientos", "modelo"]
fichero = "./ficheros/aviones.csv"
df_aviones = FicheroCsv(
    vista_etl, vista_etl.get_etiqueta_fichero_aviones(), cabeceras, fichero
)


def test_get_nombre_fichero():
    assert df_aviones.get_nombre_fichero() == 'aviones.csv'

def test_get_filas():
    assert df_aviones.get_filas() == 46

def test_get_columnas():
    assert df_aviones.get_columnas() == 3

def test_get_cabecera():
    assert df_aviones.get_cabecera(0) == 'codigo_IATA'

def test_get_elemento():
    assert df_aviones.get_elemento('codigo_IATA', 0) == '223'