from src.controlador.c_general import ControladorGeneral
from src.controlador.librerias import *
from src.vista.v_general import Vista


class Aplicacion(Tk):
    def __init__(self):

        super().__init__()

        vista = Vista(self)
        self.controlador_general = ControladorGeneral(vista)
        vista.set_controlador(self.controlador_general)
        vista.pack()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
