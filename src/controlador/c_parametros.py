class ControladorParametros:
    def __init__(self, vista):
        self.__vista = vista

        self.__semana = ""
        self.__jornada = 0
        self.__descanso = 0
        self.__velocidad = 0
        self.__ocupacion = 0
        self.__exito = 0

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
