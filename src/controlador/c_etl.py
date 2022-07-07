from src.modelo.operaciones.lectura_fichero import FicheroCsv
from src.modelo.m_etl import ModeloEtl
from src.controlador.c_barra_progreso import BarraProgreso
from src.librerias import *
from src.modelo.operaciones.proceso_etl import *
from src.funciones_aux import (
    conversor_aeropueros,
    obtener_nombre,
)
from src.vista.v_barra_progreso import VistaBarraProgreso


class ControladorEtl:
    """
    Clase para representar el controlador de la vista que configura los
    ficheros para el ETL.

    Atributes
    ----------
    vista_etl : VistaETL
        Toplevel widget para representar la ventana que configura los
        ficheros para el ETL.

    controlador_general : ControladorGeneral
        Controlador para manipular el la ventana principal.

    df_vuelos : DataFrame
        Dataframe para almacenar el resultado del proceso ETL.

    df_aviones : DataFrame
        Dataframe para almacenar el fichero con los aviones.

    modelo_etl : ModeloEtl
        Modelo para almacenar y realizar operaciones sobre los datos del
        que se generan tras el proceso ETL.
    """

    def __init__(self, vista_etl, controlador_parametros, controlador_general):
        """
        Parameters
        ----------
        vista_etl : VistaETL
            Toplevel widget para representar la ventana que configura los
            ficheros para el ETL.

        controlador_parametros : ControladorGeneral
            Controlador para manipular la ventana de los parametros.

        controlador_general : ControladorGeneral
            Controlador para manipular la ventana principal.
        """

        self.__vista_etl = vista_etl
        self.__controlador_general = controlador_general
        self.__df_vuelos = pd.DataFrame()
        self.__df_aviones = pd.DataFrame()
        self.__modelo_etl = ModeloEtl(controlador_parametros)

    def set_fichero_vuelos(self, etiqueta, fichero=None):
        """Método setter para definir el fichero GESLOT

        Parameters
        ----------
        etiqueta : Etiqueta
            Etiqueta utilizada para que contenga el nombre del fichero que
            se pasó con los datos de GESLOT.

        fichero : str
            Ruta donde se encuentra el fichero GESLOT.
        """

        cabeceras = [
            "Unnamed: 0",
            "Unnamed: 1",
            "Destino",
            "Codigo",
            "Dia_semana",
            "Opera_desde",
            "Opera_hasta",
            "Hora_Salida",
            "Aeronave",
            "Num_vuelo",
            "Pais",
            "Escala",
            "Origen",
        ]
        self.__df_vuelos = FicheroCsv(
            self.__vista_etl, etiqueta, cabeceras, fichero
        ).get_df()

    def set_fichero_aviones(self, etiqueta, fichero=None):
        """Método setter para definir dataframe que contiene los aviones

        Parameters
        ----------
        etiqueta : Etiqueta
            Etiqueta utilizada para que contenga el nombre del fichero que
            se pasó con los modelos de aviones.

        fichero : str
            Ruta donde se encuentra el fichero con los modelos de aviones.
        """

        cabeceras = ["codigo_IATA", "asientos", "modelo"]
        self.__df_aviones = FicheroCsv(
            self.__vista_etl, etiqueta, cabeceras, fichero
        ).get_df()

    def get_fichero_vuelos(self):
        """Método getter para obtener el dataframe que contiene la información
        de GESLOT.
        """

        return self.__df_vuelos

    def get_fichero_aviones(self):
        """Método getter para obtener el dataframe que contiene los modelos de
        aviones.
        """

        return self.__df_aviones

    def get_modelo_etl(self):
        """Método getter para obtener el modelo donde se almacena los datos
        obtenidos tras el proceso de ETL.
        """

        return self.__modelo_etl

    def comprobar_etl(self):
        """Se utiliza para comprobar si los ficheros que se han indicado
        contienen la información que se precisa. En caso afirmativo, de invoca
        al método que inicia el proceso de ETL.
        """
        
        try:
            assert self.get_fichero_vuelos().empty == False
        except:
            showerror(
                "ERROR",
                "Falta introducir el fichero GESLOT",
                parent=self.__vista_etl,
            )
        else:
            try:
                assert self.get_fichero_aviones().empty == False
            except:
                showerror(
                    "ERROR",
                    "Falta introducir el fichero de aviones",
                    parent=self.__vista_etl,
                )
            else:
                self.aplicar_etl()
                return True

    def aplicar_etl(self):
        """Se realiza el proceso de ETL. Se ejecutan una serie de
        comprobaciones para evitar que se cometan errores.
        """

        self.__modelo_etl.set_df_vuelos(self.__df_vuelos)
        self.__modelo_etl.set_df_aviones(self.__df_aviones)

        etl = Etl(
            self.__modelo_etl.get_df_vuelos(),
            self.__modelo_etl.get_aeropuertos(),
            self.__modelo_etl.get_dias(),
        )

        self.__vista_etl.attributes("-topmost", False)

        self.__v_barra_progreso = VistaBarraProgreso(
            self.__vista_etl, "Progreso ETL", "Aplicando ETL..."
        )
        controlador_barra_progreso = BarraProgreso(self.__v_barra_progreso)
        self.__v_barra_progreso.set_controlador(controlador_barra_progreso)

        try:
            controlador_barra_progreso.aumentar_progreso(
                "16%: Eliminación columnas"
            )
            etl.eliminacion_columnas()
        except:
            showerror(
                "ERROR",
                "Al eliminar columnas innecesarias",
                parent=self.__vista_etl,
            )
        else:
            try:
                controlador_barra_progreso.aumentar_progreso(
                    "32%: Extracción de días"
                )
                etl.extraer_semana()
            except:
                showerror(
                    "ERROR",
                    "Al realizar la extracción de días",
                    parent=self.__vista_etl,
                )
            else:
                try:
                    controlador_barra_progreso.aumentar_progreso(
                        "48%: Cambio nombres regiones"
                    )
                    etl.cambiar_nombres_regiones()
                except:
                    showerror(
                        "ERROR",
                        "Al cambiar nombres de regiones",
                        parent=self.__vista_etl,
                    )
                else:
                    try:
                        controlador_barra_progreso.aumentar_progreso(
                            "64%: Separación días semanas"
                        )
                        etl.dias_operacion()
                    except:
                        showerror(
                            "ERROR",
                            "Al separar días de la semana",
                            parent=self.__vista_etl,
                        )
                    else:
                        try:
                            controlador_barra_progreso.aumentar_progreso(
                                "84%: Conversión días"
                            )
                            etl.convertir_dias()
                        except:
                            showerror(
                                "ERROR",
                                "Al contar los días",
                                parent=self.__vista_etl,
                            )
                        else:
                            try:
                                controlador_barra_progreso.aumentar_progreso(
                                    "100%: División"
                                )
                                self.__modelo_etl.set_df(etl.get_df())
                                self.__modelo_etl.guardar_df()
                            except:
                                showerror(
                                    "ERROR",
                                    "Al dividir",
                                    parent=self.__vista_etl,
                                )
                            else:
                                self.__v_barra_progreso.destroy()
                                self.__vista_etl.destroy()
                                self.__controlador_general.etl_realizado()
