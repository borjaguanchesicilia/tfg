from src.librerias import *
from src.modelo.funciones_aux import conversor_aeropueros
from src.controlador.c_parametros import ControladorParametros


class ModeloEtl:
    def __init__(self, controlador_parametros):

        self.__dias = controlador_parametros.get_modelo_parametros().get_dias()
        self.__aeropuertos = (
            controlador_parametros.get_modelo_parametros().get_aeropuertos()
        )
        self.__df_vue = None
        self.__df_avi = None
        self.__df_general = pd.DataFrame()
        self.__lista_df = []

    def set_df_vuelos(self, df_vuelos):
        self.__df_vue = df_vuelos

    def set_df_aviones(self, df_aviones):
        self.__df_avi = df_aviones

    def set_df(self, df):
        self.__df_general = df

    def get_dias(self):
        return self.__dias

    def get_aeropuertos(self):
        return self.__aeropuertos

    def get_df_vuelos(self):
        return self.__df_vue

    def get_df_aviones(self):
        return self.__df_avi

    def get_df(self, aeropuerto):
        i = 0
        while self.__lista_df[i][0] != aeropuerto:
            i += 1

        return self.__lista_df[i][1]

    def guardar_df(self):
        self.__df_general.to_csv(
            f"geslot_etl.csv", sep=";", columns=None, index=False
        )
        self.__df_general = self.__df_general.drop(
            ["opera_desde", "opera_hasta"], axis=1
        )
        self.__df_general["dia_sem"] = pd.to_datetime(
            self.__df_general["dia_sem"], dayfirst=True
        )

        for aeropuerto in self.__aeropuertos:
            df_aux = self.__df_general[
                self.__df_general["origen"] == aeropuerto
            ]
            df_aux.to_csv(
                f"{aeropuerto}.csv", sep=";", columns=None, index=False
            )
            df_aux = df_aux.reset_index()
            self.__lista_df.append((aeropuerto, df_aux))
