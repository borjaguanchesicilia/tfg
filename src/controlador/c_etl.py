import sys
from src.controlador.librerias import *
from src.controlador.etl import *
from src.controlador.funciones_aux import obtener_nombre


class ControladorEtl:
    def __init__(self, vista, vista_parametros, controlador_parametros):

        self.__vista = vista
        self.__vista_parametros = vista_parametros

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
        lista_aeropuertos = [conversor_aeropuertos[aer] for aer in self.__aeropuertos]

        try:
            etl.eliminacion_columnas()
        except:
            print("ERROR: Al eliminar columnas innecesarias")
        else:
            try:
                etl.cambio_formato_dias(self.__semana)
            except:
                print("ERROR: Al cambiar formato días")
            else:
                try:
                    etl.separar_dias_semana()
                except:
                    print("ERROR: Al separar días de la semana")
                else:
                    try:
                        etl.adicionar_columnas()
                    except:
                        print("ERROR: Al adicionar nuevas columnas")
                    else:
                        try:
                            etl.cambiar_nombres_regiones()
                        except:
                            print("ERROR: Al cambiar nombres de regiones")
                        else:
                            try:
                                etl.cambiar_dias_num()
                            except:
                                print("ERROR: Al cambiar de días a números")
                            else:
                                try:
                                    etl.convertir_dias()
                                except:
                                    print("ERROR: Al contar los días")
                                else:
                                    try:
                                        etl.dividir(lista_aeropuertos)
                                    except:
                                        print("ERROR: Al dividir")
                                    else:
                                        self.__vista_parametros.destroy()
                                        self.__vista.boton_etl.desactivar_boton()
                                        self.__vista.boton_ver_dataframes.activar_boton()
                                        self.__vista.boton_planificar.activar_boton()
