from src.controlador.c_barra_progreso import BarraProgreso
from src.librerias import *
from src.modelo.etl import *
from src.modelo.funciones_aux import (
    conversor_aeropueros,
    obtener_nombre,
)
from src.vista.v_barra_progreso import VistaBarraProgreso


class ControladorEtl:
    def __init__(self, vista_etl, controlador_parametros, controlador_general):

        self.__vista_etl = vista_etl
        self.__controlador_general = controlador_general

        self.__dias = controlador_parametros.get_dias()
        self.__aeropuertos = controlador_parametros.get_aeropuertos()
        self.__df_vue = None
        self.__df_avi = None

    def get_df_vuelos(self):
        return self.__df_vue

    def get_df_aviones(self):
        return self.__df_avi

    def aplicar_etl(self, df_vuelos, df_aviones):

        self.__df_vue = df_vuelos
        self.__df_avi = df_aviones

        lista_aeropuertos = conversor_aeropueros(self.__aeropuertos)

        etl = Etl(self.__df_vue, lista_aeropuertos)

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
                etl.extraer_semana(self.__dias)
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
                                etl.dividir()
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
