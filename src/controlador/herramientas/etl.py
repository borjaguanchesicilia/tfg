from src.librerias import *


class Etl:
    def __init__(self, df, aeropuertos):

        self.__df_inicio_aux = df
        self.__aeropuertos = aeropuertos

    def eliminacion_columnas(self):

        self.__df_inicio_aux = self.__df_inicio_aux.drop(["Escala"], axis=1)
        self.__df_inicio_aux = self.__df_inicio_aux.drop(
            self.__df_inicio_aux.columns[[0, 1]], axis="columns"
        )

        self.__df_inicio = pd.DataFrame()

        for aer in self.__aeropuertos:
            self.__df_inicio = pd.concat(
                [
                    self.__df_inicio,
                    self.__df_inicio_aux.drop(
                        self.__df_inicio_aux[
                            self.__df_inicio_aux["Origen"] != aer
                        ].index
                    ),
                ]
            )

    def extraer_semana(self, semana):

        self.__dias = []

        for dia in semana:
            dia = dia.split("/")
            self.__dias.append(
                dt_module.datetime.combine(
                    dt_module.date(
                        int(dia[2]),
                        int(dia[1]),
                        int(dia[0]),
                    ),
                    dt_module.datetime.min.time(),
                )
            )

        primer_dia = min(self.__dias)
        ultimo_dia = max(self.__dias)

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

    def cambiar_nombres_regiones(self):

        self.__df_inicio.loc[
            (
                (self.__df_inicio.Pais == "ESPAÑA")
                | (self.__df_inicio.Pais == "ESPAﾑA")
            ),
            "Pais",
        ] = "ESPANIA"

        self.__df_inicio.loc[
            (self.__df_inicio.Pais == "REINO UNIDO"), "Pais"
        ] = "REINO-UNIDO"

        self.__df_inicio.loc[
            (self.__df_inicio.Pais == "FEDERACION RUSA"), "Pais"
        ] = "FEDERACION-RUSA"

        self.__df_inicio.loc[
            (self.__df_inicio.Pais == "REPUBLICA CHECA"), "Pais"
        ] = "REPUBLICA-CHECA"

        for aer in ["LPA", "ACE", "FUE", "SPC", "TFN", "TFS", "VDE", "GMZ"]:
            self.__df_inicio.loc[
                (self.__df_inicio.Destino == aer), "Pais"
            ] = "CANARIAS"

    def dias_operacion(self):
        for operacion in [
            (" ", ""),
            ("L", "1"),
            ("M", "2"),
            ("X", "3"),
            ("J", "4"),
            ("V", "5"),
            ("S", "6"),
            ("D", "7"),
        ]:
            self.__df_inicio["Dia_semana"] = self.__df_inicio[
                "Dia_semana"
            ].apply(lambda x: x.replace(operacion[0], operacion[1]))

        self.__df_inicio["Dia_semana"] = self.__df_inicio["Dia_semana"].apply(
            lambda x: int(x)
        )
        self.__df_varios_dias = self.__df_inicio.drop(
            self.__df_inicio[self.__df_inicio["Dia_semana"] <= 7].index
        )
        self.__df_dias_sueltos = self.__df_inicio.drop(
            self.__df_inicio[self.__df_inicio["Dia_semana"] > 7].index
        )

        self.__df_varios_dias["Dia_semana"] = self.__df_varios_dias[
            "Dia_semana"
        ].apply(lambda x: list(map(int, str(x))))

        self.__df_varios_dias = self.__df_varios_dias.reset_index()

        df_aux = pd.DataFrame(
            columns=[
                "destino",
                "codigo",
                "dia_sem",
                "opera_desde",
                "opera_hasta",
                "hora_salida",
                "aeronave",
                "num_vuelo",
                "pais",
                "origen",
            ]
        )

        for i in range(len(self.__df_varios_dias)):
            fila = self.__df_varios_dias.iloc[i]
            dias = fila["Dia_semana"]
            while len(dias) != 0:
                df_aux = df_aux.append(
                    {
                        "destino": fila["Destino"],
                        "codigo": fila["Codigo"],
                        "dia_sem": dias[-1],
                        "opera_desde": fila["Opera_desde"],
                        "opera_hasta": fila["Opera_hasta"],
                        "hora_salida": fila["Hora_Salida"],
                        "aeronave": fila["Aeronave"],
                        "num_vuelo": fila["Num_vuelo"],
                        "pais": fila["Pais"],
                        "origen": fila["Origen"],
                    },
                    ignore_index=True,
                )
                dias.pop()

        self.__df_dias_sueltos = self.__df_dias_sueltos.reset_index(drop=True)
        self.__df_dias_sueltos.columns = [
            "destino",
            "codigo",
            "dia_sem",
            "opera_desde",
            "opera_hasta",
            "hora_salida",
            "aeronave",
            "num_vuelo",
            "pais",
            "origen",
        ]

        self.df = self.__df_dias_sueltos.append(df_aux, ignore_index=True)
        self.df = self.df[
            [
                "num_vuelo",
                "dia_sem",
                "destino",
                "codigo",
                "opera_desde",
                "opera_hasta",
                "hora_salida",
                "aeronave",
                "pais",
                "origen",
            ]
        ]
        self.df = self.df.reset_index(drop=True)

    def convertir_dias(self):

        cont_dias = min(self.__dias)
        cont_dias = pd.to_datetime(cont_dias, dayfirst=True)

        while cont_dias <= max(self.__dias):
            # Lunes
            if dt_module.datetime.weekday(cont_dias) == 0:
                self.df.loc[(self.df.dia_sem == 1), "dia_sem"] = cont_dias
            # Martes
            elif dt_module.datetime.weekday(cont_dias) == 1:
                self.df.loc[(self.df.dia_sem == 2), "dia_sem"] = cont_dias
            # Miércoles
            elif dt_module.datetime.weekday(cont_dias) == 2:
                self.df.loc[(self.df.dia_sem == 3), "dia_sem"] = cont_dias
            # Juevas
            elif dt_module.datetime.weekday(cont_dias) == 3:
                self.df.loc[(self.df.dia_sem == 4), "dia_sem"] = cont_dias
            # Viernes
            elif dt_module.datetime.weekday(cont_dias) == 4:
                self.df.loc[(self.df.dia_sem == 5), "dia_sem"] = cont_dias
            # Sábado
            elif dt_module.datetime.weekday(cont_dias) == 5:
                self.df.loc[(self.df.dia_sem == 6), "dia_sem"] = cont_dias
            # Domingo
            elif dt_module.datetime.weekday(cont_dias) == 6:
                self.df.loc[(self.df.dia_sem == 7), "dia_sem"] = cont_dias

            cont_dias = pd.to_datetime(
                cont_dias + dt_module.timedelta(days=1), dayfirst=True
            )

        # Borrado de días sueltos
        self.df = self.df[
            self.df["dia_sem"].apply(lambda x: not isinstance(x, int))
        ]

    def dividir(self):

        self.df.to_csv(f"geslot_etl.csv", sep=";", columns=None, index=False)
        self.df = self.df.drop(["opera_desde", "opera_hasta"], axis=1)
        self.df["dia_sem"] = pd.to_datetime(self.df["dia_sem"], dayfirst=True)

        for aeropuerto in self.__aeropuertos:
            df2 = self.df[self.df["origen"] == aeropuerto]
            df2.to_csv(f"{aeropuerto}.csv", sep=";", columns=None, index=False)
