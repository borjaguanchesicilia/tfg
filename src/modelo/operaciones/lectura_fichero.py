from src.librerias import *
from src.funciones_aux import obtener_nombre


class FicheroCsv:
    def __init__(self, vista, etiqueta, cabeceras, fichero=None):

        self.__v_parametros = vista
        self.__etiqueta = etiqueta

        if fichero != None:
            self.__ruta_fichero = fichero
        else:
            ruta = str(os.path.dirname(os.path.abspath(__file__)))
            self.__ruta_fichero = str(
                filedialog.askopenfilename(
                    initialdir=ruta,
                    title="Abrir fichero vuelos",
                    parent=self.__v_parametros,
                )
            )

        try:
            assert self.__ruta_fichero != "()"
        except:
            showerror(
                "ERROR",
                "Debe seleccionar un fichero",
                parent=self.__v_parametros,
            )
        else:
            self.__nombre_fichero = obtener_nombre(self.__ruta_fichero)

            try:
                if ".csv" not in self.__nombre_fichero:
                    raise NameError()
            except:
                showerror(
                    "ERROR",
                    "El fichero no es .csv",
                    parent=self.__v_parametros,
                )
            else:
                self.__df = pd.read_csv(self.__ruta_fichero, sep=";")
                try:
                    cabeceras_aux = [
                        cabecera for cabecera in self.__df.columns
                    ]
                    assert cabeceras == cabeceras_aux
                except:
                    showerror(
                        "ERROR",
                        "El fichero no tiene las cabeceras correctas",
                        parent=self.__v_parametros,
                    )
                else:
                    self.cambiar_nombre_etiqueta()
                    self.__filas = len(self.__df.axes[0])
                    self.__columnas = len(self.__df.axes[1])
                    self.__cabeceras = list(self.__df.columns)

    def get_nombre_fichero(self):
        return self.__nombre_fichero

    def get_df(self):
        return self.__df

    def get_filas(self):
        return self.__filas

    def get_columnas(self):
        return self.__columnas

    def get_cabecera(self, indice):
        return self.__cabeceras[indice]

    def get_elemento(self, cabecera, indice):
        return self.__df[f"{cabecera}"][indice]

    def cambiar_nombre_etiqueta(self):
        self.__v_parametros.set_etiqueta_fichero(
            self.__nombre_fichero, self.__etiqueta
        )
