from src.modelo.operaciones.lectura_fichero import FicheroCsv
from src.modelo.m_etl import ModeloEtl
from src.controlador.c_barra_progreso import BarraProgreso
from src.librerias import *
from src.modelo.operaciones.proceso_etl import *
from src.funciones_aux import (
    conversor_aeropueros,
    obtener_nombre,
)
from src.vista.v_barra_progreso import VistaBarraProgreso


class ControladorEtl:
    def __init__(self, vista_etl, controlador_parametros, controlador_general):

        self.__vista_etl = vista_etl
        self.__controlador_general = controlador_general
        self.__df_vuelos = pd.DataFrame()
        self.__df_aviones = pd.DataFrame()
        self.__modelo_etl = ModeloEtl(controlador_parametros)

    def set_fichero_vuelos(self, etiqueta, fichero=None):
        cabeceras = [
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
        self.__df_vuelos = FicheroCsv(
            self.__vista_etl, etiqueta, cabeceras, fichero
        ).get_df()

    def set_fichero_aviones(self, etiqueta, fichero=None):
        cabeceras = ["codigo_IATA", "asientos", "modelo"]
        self.__df_aviones = FicheroCsv(
            self.__vista_etl, etiqueta, cabeceras, fichero
        ).get_df()

    def get_fichero_vuelos(self):
        return self.__df_vuelos

    def get_fichero_aviones(self):
        return self.__df_aviones

    def get_modelo_etl(self):
        return self.__modelo_etl

    def comprobar_etl(self):
        try:
            assert self.get_fichero_vuelos().empty == False
        except:
            showerror(
                "ERROR",
                "Falta introducir el fichero GESLOT",
                parent=self.__vista_etl,
            )
        else:
            try:
                assert self.get_fichero_aviones().empty == False
            except:
                showerror(
                    "ERROR",
                    "Falta introducir el fichero de aviones",
                    parent=self.__vista_etl,
                )
            else:
                self.aplicar_etl()
                return True

    def aplicar_etl(self):

        self.__modelo_etl.set_df_vuelos(self.__df_vuelos)
        self.__modelo_etl.set_df_aviones(self.__df_aviones)

        etl = Etl(
            self.__modelo_etl.get_df_vuelos(),
            self.__modelo_etl.get_aeropuertos(),
            self.__modelo_etl.get_dias(),
        )

        self.__vista_etl.attributes("-topmost", False)

        self.__v_barra_progreso = VistaBarraProgreso(
            self.__vista_etl, "Progreso ETL", "Aplicando ETL..."
        )
        controlador_barra_progreso = BarraProgreso(self.__v_barra_progreso)
        self.__v_barra_progreso.set_controlador(controlador_barra_progreso)

        try:
            controlador_barra_progreso.aumentar_progreso(
                "16%: Eliminación columnas"
            )
            etl.eliminacion_columnas()
        except:
            showerror(
                "ERROR",
                "Al eliminar columnas innecesarias",
                parent=self.__vista_etl,
            )
        else:
            try:
                controlador_barra_progreso.aumentar_progreso(
                    "32%: Extracción de días"
                )
                etl.extraer_semana()
            except:
                showerror(
                    "ERROR",
                    "Al realizar la extracción de días",
                    parent=self.__vista_etl,
                )
            else:
                try:
                    controlador_barra_progreso.aumentar_progreso(
                        "48%: Cambio nombres regiones"
                    )
                    etl.cambiar_nombres_regiones()
                except:
                    showerror(
                        "ERROR",
                        "Al cambiar nombres de regiones",
                        parent=self.__vista_etl,
                    )
                else:
                    try:
                        controlador_barra_progreso.aumentar_progreso(
                            "64%: Separación días semanas"
                        )
                        etl.dias_operacion()
                    except:
                        showerror(
                            "ERROR",
                            "Al separar días de la semana",
                            parent=self.__vista_etl,
                        )
                    else:
                        try:
                            controlador_barra_progreso.aumentar_progreso(
                                "84%: Conversión días"
                            )
                            etl.convertir_dias()
                        except:
                            showerror(
                                "ERROR",
                                "Al contar los días",
                                parent=self.__vista_etl,
                            )
                        else:
                            try:
                                controlador_barra_progreso.aumentar_progreso(
                                    "100%: División"
                                )
                                self.__modelo_etl.set_df(etl.get_df())
                                self.__modelo_etl.guardar_df()
                            except:
                                showerror(
                                    "ERROR",
                                    "Al dividir",
                                    parent=self.__vista_etl,
                                )
                            else:
                                self.__v_barra_progreso.destroy()
                                self.__vista_etl.destroy()
                                self.__controlador_general.etl_realizado()
