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

        self.__df_inicio = self.__df_inicio.assign(dia_sem="")

        combinaciones_dias = np.unique(
            np.array(list(self.__df_inicio["Dia_semana"]))
        )

        indices = []

        for combinacion in combinaciones_dias:
            indices.append(
                (
                    self.__df_inicio[
                        self.__df_inicio["Dia_semana"] == combinacion
                    ].index.values
                )[0]
            )

        for i in indices:
            diasI = str(self.__df_inicio["Dia_semana"][i])
            aux = self.__df_inicio["Dia_semana"][i]
            diasI = diasI.replace(" ", "-")
            dias = ""
            for i in range(7):
                dias += diasI[i] + "|"

            dias = dias[:-1]

            self.__df_inicio.loc[
                (self.__df_inicio.Dia_semana == aux), "dia_sem"
            ] = dias

        self.df = pd.DataFrame(
            self.__df_inicio.dia_sem.str.split("|").tolist(),
            index=self.__df_inicio.Num_vuelo,
        ).stack()

        self.df = self.df.reset_index([0, "Num_vuelo"])
        self.df.columns = ["Num_vuelo", "dia_sem"]

        self.df = self.df.drop(self.df[self.df["dia_sem"] == "-"].index)

    def adicionar_columnas(self):

        # Adición de nuevas columnas
        self.df = self.df.assign(destino="")
        self.df = self.df.assign(codigo="")
        self.df = self.df.assign(opera_desde="")
        self.df = self.df.assign(opera_hasta="")
        self.df = self.df.assign(hora_salida="")
        self.df = self.df.assign(aeronave="")
        self.df = self.df.assign(pais="")
        self.df = self.df.assign(opera_desde="")
        self.df = self.df.assign(origen="")

        indices = (self.__df_inicio.index).tolist()

        # Completar las nuevas columnas con los datos correspondientes
        for i in indices:
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
                (self.df.Num_vuelo == num_vuelo), "hora_salida"
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

    def cambio_formato_dias(self, semana):
        self.__dias = []

        for dia in semana:
            dia = dia.split("/")
            self.__dias.append(
                datetime.combine(
                    date(
                        int(dia[2]),
                        int(dia[1]),
                        int(dia[0]),
                    ),
                    datetime.min.time(),
                )
            )

        self.__df_inicio["Opera_hasta"] = pd.to_datetime(
            self.__df_inicio["Opera_hasta"], dayfirst=True
        )
        self.__df_inicio["Opera_desde"] = pd.to_datetime(
            self.__df_inicio["Opera_desde"], dayfirst=True
        )

        inicio_operaciones = self.__df_inicio.loc[:, "Opera_desde"] <= max(
            self.__dias
        )
        sub_df_ini = self.__df_inicio.loc[inicio_operaciones]
        sub_df_ini.head()

        fin_operaciones = sub_df_ini.loc[:, "Opera_hasta"] >= min(self.__dias)
        sub_df_fin = sub_df_ini.loc[fin_operaciones]
        sub_df_fin.head()
        self.__df_inicio = sub_df_fin

    def cambiar_dias_num(self):
        conversor = [
            ("L", 1),
            ("M", 2),
            ("X", 3),
            ("J", 4),
            ("V", 5),
            ("S", 6),
            ("D", 7),
        ]

        for dia in conversor:
            self.df.loc[(self.df.dia_sem == dia[0]), "dia_sem"] = dia[1]

    def convertir_dias(self):

        cont_dias = min(self.__dias)
        cont_dias = pd.to_datetime(cont_dias, dayfirst=True)

        while cont_dias <= max(self.__dias):
            # Lunes
            if datetime.weekday(cont_dias) == 0:
                self.df.loc[(self.df.dia_sem == 1), "dia_sem"] = cont_dias
            # Martes
            elif datetime.weekday(cont_dias) == 1:
                self.df.loc[(self.df.dia_sem == 2), "dia_sem"] = cont_dias
            # Miércoles
            elif datetime.weekday(cont_dias) == 2:
                self.df.loc[(self.df.dia_sem == 3), "dia_sem"] = cont_dias
            # Juevas
            elif datetime.weekday(cont_dias) == 3:
                self.df.loc[(self.df.dia_sem == 4), "dia_sem"] = cont_dias
            # Viernes
            elif datetime.weekday(cont_dias) == 4:
                self.df.loc[(self.df.dia_sem == 5), "dia_sem"] = cont_dias
            # Sábado
            elif datetime.weekday(cont_dias) == 5:
                self.df.loc[(self.df.dia_sem == 6), "dia_sem"] = cont_dias
            # Domingo
            elif datetime.weekday(cont_dias) == 6:
                self.df.loc[(self.df.dia_sem == 7), "dia_sem"] = cont_dias

            cont_dias = pd.to_datetime(
                cont_dias + timedelta(days=1), dayfirst=True
            )

        # Borrado de días sueltos
        self.df = self.df[
            self.df["dia_sem"].apply(lambda x: not isinstance(x, int))
        ]

    def dividir(self, aeropuertos):

        self.df.to_csv(f"salida.csv", sep=";", columns=None, index=False)

        self.df = self.df.drop(["opera_desde", "opera_hasta"], axis=1)

        self.df["dia_sem"] = pd.to_datetime(self.df["dia_sem"], dayfirst=True)

        for aeropuerto in aeropuertos:
            df2 = self.df[self.df["origen"] == aeropuerto]
            df2.to_csv(f"{aeropuerto}.csv", sep=";", columns=None, index=False)
