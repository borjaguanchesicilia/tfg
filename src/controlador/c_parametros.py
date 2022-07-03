from src.modelo.m_parametros import ModeloParametros


class ControladorParametros:
    def __init__(self, vista_parametros, controlador_general):

        self.__vista_parametros = vista_parametros
        self.__controlador_general = controlador_general
        self.__modelo_parametros = ModeloParametros()

    def get_modelo_parametros(self):
        return self.__modelo_parametros

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
        self.__modelo_parametros.set_dias(dias)
        self.__modelo_parametros.set_jornada(jornada)
        self.__modelo_parametros.set_descanso(descanso)
        self.__modelo_parametros.set_velocidad(velocidad)
        self.__modelo_parametros.set_ocupacion(ocupacion)
        self.__modelo_parametros.set_exito(exito)
        self.__modelo_parametros.set_aeropuertos(aeropuertos)

        self.__controlador_general.parametros_guardados()
