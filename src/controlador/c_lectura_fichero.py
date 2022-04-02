from src.controlador.funciones_aux import obtener_nombre
from src.controlador.librerias import *


class FicheroCsv:
    def __init__(self, vista, etiqueta):

        self.__v_parametros = vista
        self.__etiqueta = etiqueta

        ruta = str(os.path.dirname(os.path.abspath(__file__)))
        self.__ruta_fichero = str(
            filedialog.askopenfilename(
                initialdir=ruta, title="Abrir fichero vuelos"
            )
        )

        self.__nombre_fichero = obtener_nombre(self.__ruta_fichero)

        try:
            if ".csv" not in self.__nombre_fichero:
                raise NameError()
        except:
            print(showerror("ERROR", "El fichero no es .csv"))
        else:
            self.__df = pd.read_csv(self.__ruta_fichero, sep=";")
            self.cambiar_nombre_etiqueta()
            self.__filas = len(self.__df.axes[0])
            self.__columnas = len(self.__df.axes[1])
            self.__cabeceras = list(self.__df.columns)

    def get_nombre_fichero(self):
        return self.__nombre_fichero

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
