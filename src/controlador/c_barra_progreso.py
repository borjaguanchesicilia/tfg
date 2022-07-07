from src.librerias import *


class BarraProgreso(Thread):
    """
    Clase para representar el controlador de la vista que contiene la barra de
    progreso.

    Atributes
    ----------
    vista : VistaBarraProgreso
        Toplevel widget para representar la ventana que contiene la barra de
        progreso.

    """
    def __init__(self, vista):
        """

        Parameters
        ----------
        vista : VistaBarraProgreso
            Vista a la que se le asigna el controlador.

        """
        super().__init__()

        self.__vista = vista
        self.start()

    def aumentar_progreso(self, operacion):
        """
        Se indica al controlador de la barra de progreso que operación se está
        realizando. Se aumenta el valor de la barra y se indica la operación
        a realizar.

        Parameters
        ----------
        operacion : str
            Cadena de texto que contiene el paso que se va a realizar en el
            proceso que se está realizando

        Returns
        -------
        bool
            Valor booleano para indicar si el tipo de operación es str (True) o
            no (False).
        """
        if type(operacion) == str:
            self.__vista.set_valor_barra()
            self.__vista.set_paso_barra(operacion)
            self.__vista.after(300)
            self.__vista.update_idletasks()
            return True
        else:
            return False
