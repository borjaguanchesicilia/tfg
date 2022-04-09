import sys
from src.controlador.librerias import *
from src.controlador.etl import *
from src.controlador.funciones_aux import obtener_nombre


class ControladorEtl:
    def __init__(self, vista, controlador_parametros):

        self.__vista = vista

        self.__semana = controlador_parametros.get_semana()
        self.__jornada = controlador_parametros.get_jornada()
        self.__descanso = controlador_parametros.get_descanso()
        self.__velocidad = controlador_parametros.get_velocidad()
        self.__ocupacion = controlador_parametros.get_ocupacion()
        self.__exito = controlador_parametros.get_exito()
        self.__df_vue = controlador_parametros.get_df_vuelos()
        self.__df_avi = controlador_parametros.get_df_aviones()

        print(
            self.__semana,
            self.__jornada,
            self.__descanso,
            self.__velocidad,
            self.__ocupacion,
            self.__exito,
            self.__df_vue,
            self.__df_avi,
        )

    def aplicar_etl(self, aeropuertos):

        etl = Etl(self.__df_vue)

        conversor_aeropuertos = {
            "Arrecife": "ACE",
            "Fuerteventura": "FUE",
            "Gran Canaria": "LPA",
            "Tenerife Norte": "TFN",
            "Tenerife Sur": "TFS",
            "La Palma": "SPC",
        }
        lista_aeropuertos = [conversor_aeropuertos[aer] for aer in aeropuertos]

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
                                        pass
