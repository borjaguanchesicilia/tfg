from src.funciones_aux import conversor_aeropueros, obtener_nombre


def test_obtener_nombre():
    assert obtener_nombre("./ficheros/aviones.csv") == "aviones.csv"


def test_conversor_aeropueros():
    assert conversor_aeropueros(["Tenerife Norte", "Tenerife Sur"]) == [
        "TFN",
        "TFS",
    ]
