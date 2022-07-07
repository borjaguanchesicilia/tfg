from src.modelo.m_parametros import ModeloParametros
from src.vista.componentes_vistas.parametro_dia import ParametroDia
from src.librerias import *


class ControladorParametros:
    """
    Clase para representar el controlador de la vista para introducir los
    parámetros.

    Atributes
    ----------
    vista_parametros : VistaParametros
        Toplevel widget para representar la ventana para introducir los
        parámetros.
    
    controlador_general : ControladorGeneral
        Controlador para manipular la ventana principal.

    modelo_parametros : ModeloParametros
        Modelo para almacenar y realizar operaciones sobre los datos de los
        parámetros que introduce el usuario.
    """

    def __init__(self, vista_parametros, controlador_general):
        """
        Parameters
        ----------
        vista_parametros : VistaParametros
            Toplevel widget para representar la ventana para introducir los
            parámetros.

        controlador_general : ControladorGeneral
            Controlador para manipular la ventana principal.
        """

        self.__vista_parametros = vista_parametros
        self.__controlador_general = controlador_general
        self.__modelo_parametros = ModeloParametros()

    def get_modelo_parametros(self):
        """Método getter para obtener el modelo donde se almacena los
        parámetros introducidos por el usuario.
        """

        return self.__modelo_parametros

    def introducir_parametros(self):
        """
        Se comprueban si los parámetros que ha introducido el usuario son
        correctos y en caso afirmativo, se invoca al método para almacenar
        dichos parámetros en el modelo.
        """
        
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
        """
        Método para almacenar en el modelos los parámetros introducidos por el
        usuario. 
        """

        self.__modelo_parametros.set_dias(dias)
        self.__modelo_parametros.set_jornada(jornada)
        self.__modelo_parametros.set_descanso(descanso)
        self.__modelo_parametros.set_velocidad(velocidad)
        self.__modelo_parametros.set_ocupacion(ocupacion)
        self.__modelo_parametros.set_exito(exito)
        self.__modelo_parametros.set_aeropuertos(aeropuertos)

        self.__controlador_general.parametros_guardados()
