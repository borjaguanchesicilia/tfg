from src.modelo.funciones_aux import conversor_aeropueros


class ModeloParametros:

    def __init__(self):

        self.__semana = ""
        self.__jornada = 0
        self.__descanso = 0
        self.__velocidad = 0
        self.__ocupacion = 0
        self.__exito = 0
        self.__aeropuertos = []

    def set_dias(self, dias):
        self.__dias = dias

    def set_jornada(self, jornada):
        self.__jornada = int(jornada)

    def set_descanso(self, descanso):
        self.__descanso = int(descanso)

    def set_velocidad(self, velocidad):
        self.__velocidad = float(velocidad)

    def set_ocupacion(self, ocupacion):
        self.__ocupacion = float(ocupacion / 100)

    def set_exito(self, exito):
        self.__exito = float(exito / 100)

    def set_aeropuertos(self, aeropuertos):
        self.__aeropuertos = conversor_aeropueros(aeropuertos)

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