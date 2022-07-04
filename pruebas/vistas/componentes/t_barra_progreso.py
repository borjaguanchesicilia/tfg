from src.controlador.c_barra_progreso import BarraProgreso
from pruebas.configuracion_test import *
from src.vista.v_barra_progreso import VistaBarraProgreso


barra = VistaBarraProgreso(app, "Ventana Prueba", "Pruebas")
controlador_barra = BarraProgreso(barra)
barra.set_controlador(controlador_barra)


def test_aumentar_progreso():
    assert controlador_barra.aumentar_progreso("operacion_prueba") == True
