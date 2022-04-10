from src.controlador.librerias import *
from src.vista.vista import Vista


class Aplicacion(Tk):
    def __init__(self):

        super().__init__()

        vista = Vista(self)
        vista.pack()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
