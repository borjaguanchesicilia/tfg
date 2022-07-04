from pruebas.configuracion_test import *


parametro_prueba = ParametroDia(vista_parametros, vista_parametros, 5, 4)

def test_get_dia():
    assert parametro_prueba.get_dia() == 5

def test_get_fila():
    assert parametro_prueba.get_fila() == 4