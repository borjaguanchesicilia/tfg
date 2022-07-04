from pruebas.configuracion_test import *


def test_comprobar_funcion_objetivo():
    vista_planificar.set_funcion_objetivo(['Neutral'])
    controlador_planificar.comprobar_funcion_objetivo()
    assert controlador_planificar.get_funcion_objetivo() == 0


def test_comprobar_solver():
    vista_planificar.set_solver(['GUROBI'])
    controlador_planificar.comprobar_solver()
    assert controlador_planificar.get_solver() == 1