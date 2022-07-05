from pruebas.configuracion_test import *


def test_planificar():
    assert controlador_planificar.planificar() == -1


def test_planificar_2():
    vista_planificar.set_funcion_objetivo(["Neutral"])
    assert controlador_planificar.planificar() == -2


def test_comprobar_funcion_objetivo_1():
    vista_planificar.set_funcion_objetivo(["Neutral"])
    controlador_planificar.comprobar_funcion_objetivo()
    assert controlador_planificar.get_funcion_objetivo() == 0


def test_comprobar_funcion_objetivo_2():
    vista_planificar.set_funcion_objetivo(
        ["Priorizar empleo de varios encuestadores"]
    )
    controlador_planificar.comprobar_funcion_objetivo()
    assert controlador_planificar.get_funcion_objetivo() == 1


def test_comprobar_funcion_objetivo_3():
    vista_planificar.set_funcion_objetivo(
        ["Penalizar empleo de un encuestador"]
    )
    controlador_planificar.comprobar_funcion_objetivo()
    assert controlador_planificar.get_funcion_objetivo() == 2


def test_comprobar_solver_1():
    vista_planificar.set_solver(["CBC"])
    controlador_planificar.comprobar_solver()
    assert controlador_planificar.get_solver() == 0


def test_comprobar_solver_2():
    vista_planificar.set_solver(["GUROBI"])
    controlador_planificar.comprobar_solver()
    assert controlador_planificar.get_solver() == 1
