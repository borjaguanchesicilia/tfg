from pruebas.configuracion_test import *


def test_get_modelo():
    assert type(controlador_parametros.get_modelo_parametros()) == ModeloParametros

    
def test_get_dias():
    assert controlador_parametros.get_modelo_parametros().get_dias() == [
        "01/03/2022",
        "02/03/2022",
        "03/03/2022",
    ]


def test_get_jornada():
    assert controlador_parametros.get_modelo_parametros().get_jornada() == 8


def test_get_descanso():
    assert controlador_parametros.get_modelo_parametros().get_descanso() == 10


def test_get_velocidad():
    assert (
        controlador_parametros.get_modelo_parametros().get_velocidad() == 0.5
    )


def test_get_ocupacion():
    assert (
        controlador_parametros.get_modelo_parametros().get_ocupacion() == 0.80
    )


def test_get_exito():
    assert controlador_parametros.get_modelo_parametros().get_exito() == 0.60


def test_get_aeropuertos():
    assert (
        controlador_parametros.get_modelo_parametros().get_aeropuertos()
        == ["SPC", "TFN", "TFS"]
    )
