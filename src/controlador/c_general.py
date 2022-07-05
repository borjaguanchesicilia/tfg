class ControladorGeneral:
    def __init__(self, vista):
        self.__vista = vista

        # Se desactivan todos los botones no accesibles
        for boton in [
            self.__vista.boton_etl,
            self.__vista.boton_planificar,
        ]:
            boton.desactivar_boton()

    def parametros_guardados(self):
        self.__vista.boton_parametros.desactivar_boton()
        self.__vista.boton_etl.activar_boton()

    def etl_realizado(self):
        self.__vista.boton_etl.desactivar_boton()
        self.__vista.boton_planificar.activar_boton()

    def planificaion_realizada(self):
        self.__vista.boton_planificar.desactivar_boton()
