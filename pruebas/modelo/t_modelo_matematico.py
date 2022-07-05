from pyexpat import model
from src.modelo.operaciones.modelo_matematico import Modelo
from pruebas.configuracion_test import *
from pruebas.modelo.t_proceso_etl import *


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
    aeropuertos, etl_mod.get_df(), aviones, 8, 2, 10, 0.5, 0.8, 0.6, 2, 1
)


def test_calculos_iniciales():
    modelo.calculos_iniciales()
    assert list(modelo.get_df().columns) == [
        "num_vuelo",
        "dia_sem",
        "destino",
        "codigo",
        "opera_desde",
        "opera_hasta",
        "hora_salida",
        "aeronave",
        "pais",
        "origen",
        "num_asientos",
        "ocupacion",
        "total_encuestas",
        "consumo",
    ]


def test_calculo_encuestas():
    modelo.calculo_encuestas()
    assert modelo.get_encuestas_minimas() == [80, 600, 80]


def test_get_encuestas_minimas():
    assert modelo.get_encuestas_minimas() == [80, 600, 80]


def test_get_maximo_pasajeros():
    assert modelo.get_maximo_pasajeros() == [288, 50378, 116]


def test_get_encuestas_maximas():
    assert modelo.get_encuestas_maximas() == [139, 24182, 56]


def test_formato_horas():
    assert len(modelo.formatos_horas()) == 94


def test_calculos_destinos():
    modelo.calculos_destinos()
    assert modelo.get_destinos() == ["DINAMARCA", "ESPANIA", "PORTUGAL"]


def test_get_destinos():
    assert modelo.get_destinos() == ["DINAMARCA", "ESPANIA", "PORTUGAL"]


def test_i_p():
    assert len(modelo.get_i_p()) == 3
