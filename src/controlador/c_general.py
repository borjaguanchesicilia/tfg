class ControladorGeneral:
    """
    Clase para representar el controlador de la vista general.

    Atributes
    ----------
    vista : VistaGeneral
        Toplevel widget para representar la ventana general.
    """

    def __init__(self, vista):
        """
        Parameters
        ----------
        vista : VistaGeneral
            Toplevel widget para representar la ventana general.
        """

        self.__vista = vista

        # Se desactivan todos los botones no accesibles
        for boton in [
            self.__vista.boton_etl,
            self.__vista.boton_planificar,
        ]:
            boton.desactivar_boton()

    def parametros_guardados(self):
        """
        Se desactiva la opción de seleccionar el boton para introducir los
        parámetros y se activa la opción de seleccionar el botón para realizar
        el ETL.
        """

        self.__vista.boton_parametros.desactivar_boton()
        self.__vista.boton_etl.activar_boton()

    def etl_realizado(self):
        """
        Se desactiva la opción de seleccionar el botón para realizar el ETL y
        se activa la opción de seleccionar el botón para realizar la
        planificación.
        """

        self.__vista.boton_etl.desactivar_boton()
        self.__vista.boton_planificar.activar_boton()

    def planificaion_realizada(self):
        """
        Se desactiva la opción de seleccionar el botón para realizar la
        planificación.
        """
        self.__vista.boton_planificar.desactivar_boton()
