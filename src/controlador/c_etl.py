import sys
from src.controlador.librerias import *
from src.controlador.etl import *
from src.controlador.funciones_aux import obtener_nombre


class ControladorEtl:
    def __init__(self, vista, vista_etl, controlador_parametros):

        self.__vista = vista
        self.__vista_etl = vista_etl

        self.__semana = controlador_parametros.get_semana()
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

        etl = Etl(self.__df_vue)

        conversor_aeropuertos = {
            "Arrecife": "ACE",
            "Fuerteventura": "FUE",
            "Gran Canaria": "LPA",
            "Tenerife Norte": "TFN",
            "Tenerife Sur": "TFS",
            "La Palma": "SPC",
        }
        lista_aeropuertos = [
            conversor_aeropuertos[aer] for aer in self.__aeropuertos
        ]

        try:
            etl.eliminacion_columnas()
        except:
            showerror(
                "ERROR",
                "Al eliminar columnas innecesarias",
                parent=self.__vista_etl,
            )
        else:
            try:
                etl.cambio_formato_dias(self.__semana)
            except:
                showerror(
                    "ERROR", "Al cambiar formato días", parent=self.__vista_etl
                )
            else:
                try:
                    etl.separar_dias_semana()
                except:
                    showerror(
                        "ERROR",
                        "Al separar días de la semana",
                        parent=self.__vista_etl,
                    )
                else:
                    try:
                        etl.adicionar_columnas()
                    except:
                        showerror(
                            "ERROR",
                            "Al adicionar nuevas columnas",
                            parent=self.__vista_etl,
                        )
                    else:
                        try:
                            etl.cambiar_nombres_regiones()
                        except:
                            showerror(
                                "ERROR",
                                "Al cambiar nombres de regiones",
                                parent=self.__vista_etl,
                            )
                        else:
                            try:
                                etl.cambiar_dias_num()
                            except:
                                showerror(
                                    "ERROR",
                                    "Al cambiar de días a números",
                                    parent=self.__vista_etl,
                                )
                            else:
                                try:
                                    etl.convertir_dias()
                                except:
                                    showerror(
                                        "ERROR",
                                        "Al contar los días",
                                        parent=self.__vista_etl,
                                    )
                                else:
                                    try:
                                        etl.dividir(lista_aeropuertos)
                                    except:
                                        showerror(
                                            "ERROR",
                                            "Al dividir",
                                            parent=self.__vista_etl,
                                        )
                                    else:
                                        self.__vista_parametros.destroy()
                                        self.__vista.boton_etl.desactivar_boton()
                                        self.__vista.boton_ver_dataframes.activar_boton()
                                        self.__vista.boton_planificar.activar_boton()
