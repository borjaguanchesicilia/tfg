from pruebas.configuracion_test import *


barra = ScrollBar(vista_parametros)

def test_get_frame_scroll():
    assert type(barra.get_frame_scroll()) == ttk.Frame