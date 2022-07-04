from src.modelo.m_parametros import ModeloParametros
from src.vista.componentes_vistas.parametro_dia import ParametroDia
from src.librerias import *


class ControladorParametros:
    def __init__(self, vista_parametros, controlador_general):

        self.__vista_parametros = vista_parametros
        self.__controlador_general = controlador_general
        self.__modelo_parametros = ModeloParametros()

    def get_modelo_parametros(self):
        return self.__modelo_parametros

    def introducir_parametros(self):
        try:
            assert self.__vista_parametros.get_len_dias() > 0
        except:
            showerror(
                "ERROR",
                "Debe introducir al menos 1 día",
                parent=self.__vista_parametros,
            )
        else:
            try:
                # No se ha seleccionado ningún aeropuerto
                assert len(self.__vista_parametros.get_aeropuertos()) > 0
            except:
                showerror(
                    "ERROR",
                    "Debe seleccionar al menos un aeropuerto",
                    parent=self.__vista_parametros,
                )
            else:
                self.guardar_parametros(
                    self.__vista_parametros.get_dias(),
                    self.__vista_parametros.get_jornada_laboral(),
                    self.__vista_parametros.get_descanso(),
                    self.__vista_parametros.get_velocidad(),
                    self.__vista_parametros.get_ocupacion(),
                    self.__vista_parametros.get_exito(),
                    self.__vista_parametros.get_aeropuertos(),
                )

                self.__vista_parametros.destroy()
                del self.__vista_parametros

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
