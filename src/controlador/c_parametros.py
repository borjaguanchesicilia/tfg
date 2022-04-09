class ControladorParametros:
    def __init__(self, vista):
        self.__vista = vista

        self.__semana = ""
        self.__jornada = 0
        self.__descanso = 0
        self.__velocidad = 0
        self.__ocupacion = 0
        self.__exito = 0
        self.__df_vue = ""
        self.__df_avi = ""

    def guardar_parametros(
        self, semana, jornada, descanso, velocidad, ocupacion, exito, vue, avi
    ):
        self.__semana = semana[1:]
        self.__jornada = jornada
        self.__descanso = descanso
        self.__velocidad = velocidad
        self.__ocupacion = ocupacion
        self.__exito = exito
        self.__df_vue = vue
        self.__df_avi = avi

    def get_semana(self):
        return self.__semana

    def get_jornada(self):
        return self.__jornada

    def get_descanso(self):
        return self.__descanso

    def get_velocidad(self):
        return self.__velocidad

    def get_ocupacion(self):
        return self.__ocupacion

    def get_exito(self):
        return self.__exito

    def get_df_vuelos(self):
        return self.__df_vue

    def get_df_aviones(self):
        return self.__df_avi
