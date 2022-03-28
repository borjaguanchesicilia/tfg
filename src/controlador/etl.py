from src.controlador.librerias import *


class Etl:
    def __init__(self, df):

        self.__df_inicio = df

    def eliminacion_columnas(self):

        self.__df_inicio = self.__df_inicio.drop(["Escala"], axis=1)
        self.__df_inicio = self.__df_inicio.drop(
            self.__df_inicio.columns[[0, 1]], axis="columns"
        )

    def separar_dias_semana(self):

        self.__df_inicio = self.__df_inicio.assign(dia_sem_sep="a")

        for i in range(len(self.__df_inicio)):
            diasI = str(self.__df_inicio["Dia_semana"][i])
            aux = self.__df_inicio["Dia_semana"][i]
            diasI = diasI.replace(" ", "-")
            dias = ""
            for i in range(7):
                dias += diasI[i] + "|"

            dias = dias[:-1]
            self.__df_inicio.loc[
                (self.__df_inicio.Dia_semana == aux), "dia_sem_sep"
            ] = dias

        self.df = pd.DataFrame(
            self.__df_inicio.dia_sem_sep.str.split("|").tolist(),
            index=self.__df_inicio.Num_vuelo,
        ).stack()

        self.df = self.df.reset_index([0, "Num_vuelo"])
        self.df.columns = ["Num_vuelo", "dia_sem_sep"]

        self.df = self.df.drop(self.df[self.df["dia_sem_sep"] == "-"].index)

    def adicionar_columnas(self):

        # Adición de nuevas columnas
        self.df = self.df.assign(destino="")
        self.df = self.df.assign(codigo="")
        self.df = self.df.assign(opera_desde="")
        self.df = self.df.assign(opera_hasta="")
        self.df = self.df.assign(hora_Salida="")
        self.df = self.df.assign(aeronave="")
        self.df = self.df.assign(pais="")
        self.df = self.df.assign(opera_desde="")
        self.df = self.df.assign(origen="")

        # Completar las nuevas columnas con los datos correspondientes
        for i in range(len(self.__df_inicio)):
            num_vuelo = self.__df_inicio["Num_vuelo"][i]

            self.df.loc[
                (self.df.Num_vuelo == num_vuelo), "destino"
            ] = self.__df_inicio["Destino"][i]

            self.df.loc[
                (self.df.Num_vuelo == num_vuelo), "codigo"
            ] = self.__df_inicio["Codigo"][i]

            self.df.loc[
                (self.df.Num_vuelo == num_vuelo), "opera_desde"
            ] = self.__df_inicio["Opera_desde"][i]

            self.df.loc[
                (self.df.Num_vuelo == num_vuelo), "opera_hasta"
            ] = self.__df_inicio["Opera_hasta"][i]

            self.df.loc[
                (self.df.Num_vuelo == num_vuelo), "hora_Salida"
            ] = self.__df_inicio["Hora_Salida"][i]

            self.df.loc[
                (self.df.Num_vuelo == num_vuelo), "aeronave"
            ] = self.__df_inicio["Aeronave"][i]

            self.df.loc[
                (self.df.Num_vuelo == num_vuelo), "pais"
            ] = self.__df_inicio["Pais"][i]

            self.df.loc[
                (self.df.Num_vuelo == num_vuelo), "opera_desde"
            ] = self.__df_inicio["Opera_desde"][i]

            self.df.loc[
                (self.df.Num_vuelo == num_vuelo), "origen"
            ] = self.__df_inicio["Origen"][i]

    def cambiar_nombres_regiones(self):

        self.df.loc[(self.df.pais == "ESPANIA"), "pais"] = self.df["destino"]

        self.df.loc[(self.df.pais == "REINO UNIDO"), "pais"] = "REINO-UNIDO"

        self.df.loc[
            (self.df.pais == "FEDERACION RUSA"), "pais"
        ] = "FEDERACION-RUSA"

        self.df.loc[
            (self.df.pais == "REPUBLICA CHECA"), "pais"
        ] = "REPUBLICA-CHECA"

        for aer in ["LPA", "ACE", "FUE", "SPC", "TFN", "TFS", "VDE", "GMZ"]:
            self.df.loc[(self.df.destino == aer), "pais"] = "CANARIAS"

        print(self.df)
