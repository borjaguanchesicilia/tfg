from src.controlador.controladores_aux.c_barra_progreso import BarraProgreso
from src.librerias import *
from src.controlador.herramientas.etl import *
from src.controlador.herramientas.funciones_aux import obtener_nombre
from src.vista.vistas_aux.v_barra_progreso import VistaBarraProgreso


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

        self.__vista_etl.attributes("-topmost", False)

        self.__v_barra_progreso = VistaBarraProgreso(self.__vista_etl)
        controlador_barra_progreso = BarraProgreso(self.__v_barra_progreso)
        self.__v_barra_progreso.set_controlador(controlador_barra_progreso)

        try:
            etl.eliminacion_columnas()
            controlador_barra_progreso.aumentar_progreso(
                "12.5%: Eliminación columnas"
            )
        except:
            showerror(
                "ERROR",
                "Al eliminar columnas innecesarias",
                parent=self.__vista_etl,
            )
        else:
            try:
                etl.cambio_formato_dias(self.__dias)
                controlador_barra_progreso.aumentar_progreso(
                    "25%: Cambio formato días"
                )
            except:
                showerror(
                    "ERROR", "Al cambiar formato días", parent=self.__vista_etl
                )
            else:
                try:
                    etl.separar_dias_semana()
                    controlador_barra_progreso.aumentar_progreso(
                        "37.5%: Separación días semanas"
                    )
                except:
                    showerror(
                        "ERROR",
                        "Al separar días de la semana",
                        parent=self.__vista_etl,
                    )
                else:
                    try:
                        etl.adicionar_columnas()
                        controlador_barra_progreso.aumentar_progreso(
                            "50%: Adicionar columnas"
                        )
                    except:
                        showerror(
                            "ERROR",
                            "Al adicionar nuevas columnas",
                            parent=self.__vista_etl,
                        )
                    else:
                        try:
                            etl.cambiar_nombres_regiones()
                            controlador_barra_progreso.aumentar_progreso(
                                "62.5%: Cambio nombres regiones"
                            )
                        except:
                            showerror(
                                "ERROR",
                                "Al cambiar nombres de regiones",
                                parent=self.__vista_etl,
                            )
                        else:
                            try:
                                etl.cambiar_dias_num()
                                controlador_barra_progreso.aumentar_progreso(
                                    "75%: Cambio Días a números"
                                )
                            except:
                                showerror(
                                    "ERROR",
                                    "Al cambiar de días a números",
                                    parent=self.__vista_etl,
                                )
                            else:
                                try:
                                    etl.convertir_dias()
                                    controlador_barra_progreso.aumentar_progreso(
                                        "87.5%: Conversión días"
                                    )
                                except:
                                    showerror(
                                        "ERROR",
                                        "Al contar los días",
                                        parent=self.__vista_etl,
                                    )
                                else:
                                    try:
                                        etl.dividir(lista_aeropuertos)
                                        controlador_barra_progreso.aumentar_progreso(
                                            "100%: División"
                                        )
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
