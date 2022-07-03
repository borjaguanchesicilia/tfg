from src.librerias import *


class ModeloPlanificar:
    def __init__(self):

        self.__tiempos = pd.DataFrame()
        self.__df_solucion = pd.DataFrame()

    def set_tiempos(self, aer, modelo):
        self.__tiempos = pd.concat(
            [
                self.__tiempos,
                pd.DataFrame(
                    {
                        "origen": aer,
                        "tiempo": modelo._computo_total,
                    },
                    index=[0],
                ),
            ]
        )

    def set_solucion(self, modelo):
        self.__df_solucion = pd.concat(
            [
                self.__df_solucion,
                modelo.get_solucion(),
            ]
        )

    def generar_fichero_tiempos(self):
        self.__tiempos.to_csv("./tiempos_computo.csv", sep=";", index=False)

    def generar_fichero_solucion(self):
        self.__df_solucion.to_csv("./solucion.csv", sep=";", index=False)
