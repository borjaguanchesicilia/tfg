class ControladorParametros:
    def __init__(self, vista_parametros, controlador_general):
        
        self.__vista_parametros = vista_parametros
        self.__controlador_general = controlador_general

        self.__semana = ""
        self.__jornada = 0
        self.__descanso = 0
        self.__velocidad = 0
        self.__ocupacion = 0
        self.__exito = 0
        self.__aeropuertos = []

    def guardar_parametros(
        self,
        dias,
        jornada,
        descanso,
        velocidad,
        ocupacion,
        exito,
        aeropuertos,
    ):
        self.__dias = dias
        self.__jornada = jornada
        self.__descanso = descanso
        self.__velocidad = velocidad
        self.__ocupacion = ocupacion
        self.__exito = exito
        self.__aeropuertos = aeropuertos

        self.__controlador_general.parametros_guardados()

    def get_dias(self):
        return self.__dias

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

    def get_aeropuertos(self):
        return self.__aeropuertos
