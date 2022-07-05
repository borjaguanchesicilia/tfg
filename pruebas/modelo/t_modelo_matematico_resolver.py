from src.modelo.operaciones.proceso_etl import Etl
from src.modelo.operaciones.lectura_fichero import FicheroCsv
from src.modelo.operaciones.modelo_matematico import Modelo
from pruebas.configuracion_test import *


cabeceras_geslot = [
    "Unnamed: 0",
    "Unnamed: 1",
    "Destino",
    "Codigo",
    "Dia_semana",
    "Opera_desde",
    "Opera_hasta",
    "Hora_Salida",
    "Aeronave",
    "Num_vuelo",
    "Pais",
    "Escala",
    "Origen",
]
geslot = FicheroCsv(
    vista_etl,
    vista_etl.get_etiqueta_fichero_aviones(),
    cabeceras_geslot,
    "./ficheros/geslot_marzo_22.csv",
).get_df()


semana = [
    "07/03/2022",
    "08/03/2022",
    "09/03/2022",
    "10/03/2022",
    "11/03/2022",
    "13/03/2022",
    "13/03/2022",
]
aeropuertos = ["TFN"]
etl_mod = Etl(geslot, aeropuertos, semana)

cabeceras_aviones = ["codigo_IATA", "asientos", "modelo"]
aviones = FicheroCsv(
    vista_etl,
    vista_etl.get_etiqueta_fichero_aviones(),
    cabeceras_aviones,
    "./ficheros/aviones.csv",
).get_df()


# Proceso ETL
etl_mod.eliminacion_columnas()
etl_mod.extraer_semana()
etl_mod.cambiar_nombres_regiones()
etl_mod.dias_operacion()
etl_mod.convertir_dias()


modelo = Modelo(
    aeropuertos, etl_mod.get_df(), aviones, 8, 2, 10, 0.5, 0.8, 0.6, 2, 0
)
modelo.calculos_iniciales()
modelo.calculo_encuestas()
modelo.formatos_horas()
modelo.calculos_destinos()

modelo.resolver()
solucion = modelo.formatear_solucion()


def test_formatear_solucion_origen():
    assert solucion[0][0] == ["TFN"]


def test_formatear_solucion_regiones():
    assert solucion[1] == ["DINAMARCA", "ESPANIA", "PORTUGAL"]


"""def test_formatear_vuelos_totales():
    assert solucion[2] == [2, 589, 2]"""
