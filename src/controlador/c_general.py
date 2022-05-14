class ControladorGeneral:
    def __init__(self, vista):
        self.__vista = vista

        # Se desactivan todos los botones no accesibles
        for boton in [
            self.__vista.boton_ver_parametros,
            self.__vista.boton_etl,
            self.__vista.boton_ver_dataframes,
            #self.__vista.boton_planificar,
            self.__vista.boton_ver_planificacion,
        ]:
            boton.desactivar_boton()

    def parametros_guardados(self):
        self.__vista.boton_parametros.desactivar_boton()
        self.__vista.boton_ver_parametros.activar_boton()
        self.__vista.boton_etl.activar_boton()

    def etl_realizado(self):
        self.__vista.boton_etl.desactivar_boton()
        self.__vista.boton_ver_dataframes.activar_boton()
        self.__vista.boton_planificar.activar_boton()
