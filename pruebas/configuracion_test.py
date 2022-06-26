from app import Aplicacion
from src.vista.v_general import *
from src.controlador.c_general import *
from src.vista.v_parametros import *
from src.controlador.c_parametros import *

app = Aplicacion()
vista_general = Vista(app)
controlador_general = ControladorGeneral(vista_general)
vista_parametros = VistaParametros(app)
controlador_parametros = ControladorParametros(
    vista_parametros, controlador_general
)
controlador_parametros.guardar_parametros(
    ["01/03/2022", "02/03/2022", "03/03/2022"],
    8,
    10,
    0.5,
    80,
    60,
    ["SPC", "TFN", "TFS"],
)
