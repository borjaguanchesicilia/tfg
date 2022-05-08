from src.controlador.librerias import *


class BarraProgreso(Thread):
    def __init__(self, vista):
        super().__init__()

        self.__vista = vista
        self.start()

    def aumentar_progreso(self, operacion):
        self.__vista.set_valor_barra()
        self.__vista.set_paso_barra(operacion)
        self.__vista.after(500)
        self.__vista.update_idletasks()