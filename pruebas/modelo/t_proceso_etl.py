from src.modelo.operaciones.lectura_fichero import FicheroCsv
from src.modelo.operaciones.proceso_etl import Etl
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
aeropuertos = ["ACE", "FUE", "LPA", "TFN", "TFS", "SPC"]
etl = Etl(geslot, aeropuertos, semana)


def test_eliminacion_columnas():
    df_paso_1 = pd.read_csv(
        "./pruebas/modelo/ficheros_prueba_etl/paso1.csv", sep=";"
    )
    etl.eliminacion_columnas()
    assert list(etl.get_df_inicio().columns) == list(df_paso_1.columns)


def test_extraer_semana():
    df_paso_2 = pd.read_csv(
        "./pruebas/modelo/ficheros_prueba_etl/paso2.csv", sep=";"
    )
    etl.extraer_semana()
    assert list(etl.get_df_inicio().columns) == list(df_paso_2.columns)


def test_cambiar_nombres_regiones():
    df_paso_3 = pd.read_csv(
        "./pruebas/modelo/ficheros_prueba_etl/paso3.csv", sep=";"
    )
    etl.cambiar_nombres_regiones()
    assert list(etl.get_df_inicio().columns) == list(df_paso_3.columns)


def test_dias_operacion():
    df_paso_4 = pd.read_csv(
        "./pruebas/modelo/ficheros_prueba_etl/paso4.csv", sep=";"
    )
    etl.dias_operacion()
    assert list(etl.get_df().columns) == list(df_paso_4.columns)


def test_convertir_dias():
    df_paso_5 = pd.read_csv(
        "./pruebas/modelo/ficheros_prueba_etl/paso5.csv", sep=";"
    )
    etl.convertir_dias()
    assert list(etl.get_df().columns) == list(df_paso_5.columns)
