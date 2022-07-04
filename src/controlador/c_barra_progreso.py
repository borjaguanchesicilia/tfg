from src.librerias import *


class BarraProgreso(Thread):
    def __init__(self, vista):
        super().__init__()

        self.__vista = vista
        self.start()

    def aumentar_progreso(self, operacion):
        if type(operacion) == str:
            self.__vista.set_valor_barra()
            self.__vista.set_paso_barra(operacion)
            self.__vista.after(300)
            self.__vista.update_idletasks()
            return True
        else:
            return False
            
