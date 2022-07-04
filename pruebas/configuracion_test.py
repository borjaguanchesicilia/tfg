from app import Aplicacion
from src.vista.v_general import *
from src.controlador.c_general import *
from src.vista.v_parametros import *
from src.controlador.c_parametros import *

app = Aplicacion()
vista_general = Vista(app)
controlador_general = ControladorGeneral(vista_general)

# Parámetros
vista_parametros = VistaParametros(app)
controlador_parametros = ControladorParametros(
    vista_parametros, controlador_general
)
vista_parametros.set_controlador(controlador_parametros)
controlador_parametros.guardar_parametros(
    ["01/03/2022", "02/03/2022", "03/03/2022"],
    8,
    10,
    0.5,
    80,
    60,
    ["La Palma", "Tenerife Norte", "Tenerife Sur"],
)

# ETL
vista_etl = VistaEtl(app)
controlador_etl = ControladorEtl(
    vista_etl, controlador_parametros, controlador_general
)
vista_etl.set_controlador(controlador_etl)
vista_etl.set_botones()

# Planificar
vista_planificar = VistaPlanificar(app)
controlador_planificar = ControladorPlanificar(
    vista_planificar,
    controlador_general,
    controlador_parametros,
    controlador_etl,
)
vista_planificar.set_controlador(controlador_planificar)
