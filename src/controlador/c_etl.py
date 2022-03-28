from src.controlador.librerias import *
from src.controlador.etl import *
from src.controlador.funciones_aux import obtener_nombre


class ControladorEtl:
    def __init__(self, vista):
        self.__v_parametros = vista

        ruta = str(os.path.dirname(os.path.abspath(__file__)))
        self.__ruta_fichero = str(
            filedialog.askopenfilename(
                initialdir=ruta, title="Abrir fichero vuelos"
            )
        )

        self.__nombre_fichero = obtener_nombre(self.__ruta_fichero)

        self.cambiar_nombre_etiqueta()

        try:
            if ".csv" not in self.__nombre_fichero:
                raise NameError()
        except:
            print(showerror("ERROR", "El fichero no es .csv"))
        else:
            self.__df = pd.read_csv(self.__ruta_fichero, sep=";")
            etl = Etl(self.__df)

            try:
                etl.eliminacion_columnas()
            except:
                print()
            else:
                try:
                    etl.separar_dias_semana()
                except:
                    print()
                else:
                    try:
                        etl.adicionar_columnas()
                    except:
                        print()
                    else:
                        try:
                            etl.cambiar_nombres_regiones()
                        except:
                            print()
                        else:
                            pass

    def cambiar_nombre_etiqueta(self):
        self.__v_parametros.set_etiqueta_fichero(self.__nombre_fichero)
