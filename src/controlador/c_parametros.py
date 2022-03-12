class ControladorParametros:

    def __init__(self, vista):
        self.__vista = vista

    
    def guardar_parametros(
        self, jornada, descanso, velocidad, ocupacion, exito):
        print(jornada, descanso, velocidad, ocupacion, exito)