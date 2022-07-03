from src.modelo.funciones_aux import conversor_aeropueros
from src.controlador.c_parametros import ControladorParametros


class ModeloEtl:

    def __init__(self, controlador_parametros):

        self.__dias = controlador_parametros.get_modelo_parametros().get_dias()
        self.__aeropuertos = controlador_parametros.get_modelo_parametros().get_aeropuertos()
        self.__df_vue = None
        self.__df_avi = None

    def set_df_vuelos(self, df_vuelos):
        self.__df_vue = df_vuelos

    def set_df_aviones(self, df_aviones):
        self.__df_avi = df_aviones

    def get_dias(self):
        return self.__dias

    def get_aeropuertos(self):
        return self.__aeropuertos 

    def get_df_vuelos(self):
        return self.__df_vue

    def get_df_aviones(self):
        return self.__df_avi