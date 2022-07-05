from src.librerias import *


class Modelo:
    def __init__(
        self,
        origen,
        df,
        aviones,
        jornada,
        entrevistadores,
        descanso,
        velocidad,
        ocupacion,
        exito,
        f_o,
        solucionador,
    ):
        self.__origen = origen
        self.__df = df
        self.__df_solucion = pd.DataFrame()
        self.__df_aviones = aviones
        self.__jornada = jornada
        self.__entrevistadores = entrevistadores
        self.__descanso = descanso
        self.__velocidad = velocidad
        self.__ocupacion = ocupacion
        self.__exito = exito
        self.__f_o = f_o
        self.__solucionador = solucionador
        self.__solver = None
        self._computo_total = 0

        # Parámetros calculados
        self.__numero_de_vuelos = len(self.__df)
        self.__numero_de_entrevistadores = self.__entrevistadores
        self.__numero_de_paises = len(self.__df.groupby("pais").pais.nunique())
        self.__descanso_min = datetime.strptime(
            str(self.__descanso), "%M"
        ).time()
        self.__jornada_min = datetime.strptime(
            str(self.__jornada), "%H"
        ).time()

        # Creación de los vectores con los índices
        self.__I = [i for i in range(self.__numero_de_vuelos)]
        self.__K = [k for k in range(self.__numero_de_entrevistadores)]
        self.__P = [p for p in range(self.__numero_de_paises)]

        # Parámetros a calcular
        self.__encuestas_minimas = []
        self.__maximo_pasajeros = []
        self.__encuestas_maximas = []
        self.__destinos = []
        self.__i_p = []

        # Variables
        self.__x = {}
        self.__y1 = {}
        self.__y2 = {}
        self.__z = {}

    def calculos_iniciales(self):

        self.__df = self.__df.assign(num_asientos=0)
        self.__df = self.__df.assign(ocupacion=0)
        self.__df = self.__df.assign(total_encuestas=0)
        self.__df = self.__df.assign(consumo=0)

        for i in range(len(self.__df_aviones)):
            modelo = self.__df_aviones["codigo_IATA"][i]
            asientos = self.__df_aviones["asientos"][i]

            ocupacion = ceil(asientos * self.__ocupacion)
            encuestas = ceil(ocupacion * self.__exito)
            auxConsumo = "{:%H:%M:%S}".format(
                datetime.min + timedelta(minutes=encuestas * self.__velocidad)
            )
            consumo = datetime.strptime(auxConsumo, "%H:%M:%S").time()

            self.__df.loc[
                (self.__df.aeronave == modelo), "num_asientos"
            ] = asientos
            self.__df.loc[
                (self.__df.aeronave == modelo), "ocupacion"
            ] = ocupacion
            self.__df.loc[
                (self.__df.aeronave == modelo), "total_encuestas"
            ] = encuestas
            self.__df.loc[(self.__df.aeronave == modelo), "consumo"] = consumo

    def calculo_encuestas(self):

        df_estimacion_pasajeros = self.__df.groupby("pais")["ocupacion"].sum()

        for pais in self.__P:
            if df_estimacion_pasajeros[pais] < 60:
                self.__encuestas_minimas.append(20)
            elif (
                df_estimacion_pasajeros[pais] >= 60
                and df_estimacion_pasajeros[pais] <= 999
            ):
                self.__encuestas_minimas.append(80)
            elif (
                df_estimacion_pasajeros[pais] >= 1000
                and df_estimacion_pasajeros[pais] <= 9999
            ):
                self.__encuestas_minimas.append(200)
            elif (
                df_estimacion_pasajeros[pais] >= 10000
                and df_estimacion_pasajeros[pais] <= 24999
            ):
                self.__encuestas_minimas.append(400)
            elif (
                df_estimacion_pasajeros[pais] >= 25000
                and df_estimacion_pasajeros[pais] <= 39999
            ):
                self.__encuestas_minimas.append(500)
            elif (
                df_estimacion_pasajeros[pais] >= 40000
                and df_estimacion_pasajeros[pais] <= 59999
            ):
                self.__encuestas_minimas.append(600)
            elif df_estimacion_pasajeros[pais] >= 60000:
                self.__encuestas_minimas.append(700)

        self.__df_aux = df_estimacion_pasajeros.to_frame()

        # Calculamos cuál sería el número máximo de encuestas que se podría obtener de cada región para ver si podría satisfacerse el mínimo necesario.
        self.__maximo_pasajeros = [
            df_estimacion_pasajeros[p] for p in self.__P
        ]
        self.__encuestas_maximas = [
            ceil(
                self.__df_aux["ocupacion"][p] * self.__ocupacion * self.__exito
            )
            for p in self.__P
        ]

        self.__df_aux.insert(
            loc=1, column="encuestas_minimas", value=self.__encuestas_minimas
        )
        self.__df_aux.insert(
            loc=2, column="encuestas_maximas", value=self.__encuestas_maximas
        )

    def formatos_horas(self):
        # Se cambia el formato de las horas de salida
        horas = (self.__df["hora_salida"]).unique()
        for hora in horas:
            self.__df.loc[
                (self.__df.hora_salida == hora), "hora_salida"
            ] = datetime.strptime(hora, "%H:%M").time()

        # Se cambia el formato del consumo
        consumos = (self.__df["consumo"]).unique()
        for consumo in consumos:
            self.__df.loc[
                (self.__df.consumo == consumo), "consumo"
            ] = datetime.strptime(str(consumo), "%H:%M:%S").time()

        return horas

    def calculos_destinos(self):
        self.__destinos = sorted((self.__df["pais"]).unique())

        # Se guardan los indices de los vuelos con destino a cada país
        self.__i_p = [
            (self.__df.index[self.__df.pais == self.__destinos[p]]).tolist()
            for p in self.__P
        ]

    def get_df(self):
        return self.__df

    def get_encuestas_minimas(self):
        return self.__encuestas_minimas

    def get_maximo_pasajeros(self):
        return self.__maximo_pasajeros

    def get_encuestas_maximas(self):
        return self.__encuestas_maximas

    def get_destinos(self):
        return self.__destinos

    def get_i_p(self):
        return self.__i_p

    def resolver(self):
        # VARIABLES
        self.__x = {}
        for i in self.__I:
            for k in self.__K:
                self.__x[i, k] = LpVariable(
                    "x(" + str(i) + "," + str(k) + ")", 0, 1, LpBinary
                )

        self.__y1 = {}
        for i in self.__I:
            self.__y1[i] = LpVariable("y1(" + str(i) + ")", 0, 1, LpBinary)

        self.__y2 = {}
        for i in self.__I:
            self.__y2[i] = LpVariable("y2(" + str(i) + ")", 0, 1, LpBinary)

        self.__z = {}
        for p in self.__P:
            self.__z[p] = LpVariable("z(" + str(p) + ")", 0, 1, LpBinary)

        # FUNCION OBJETIVO
        self.__solver = LpProblem(
            f"Problema_FRONTUR_{self.__origen}", LpMaximize
        )

        if self.__f_o == 0:
            self.__solver += lpSum(
                self.__df["total_encuestas"][i] * (self.__y1[i] + self.__y2[i])
                for i in self.__I
            ) - 100000 * lpSum(
                self.__maximo_pasajeros[p] * self.__z[p] for p in self.__P
            )
        elif self.__f_o == 1:
            self.__solver += lpSum(
                self.__df["total_encuestas"][i]
                * (self.__y1[i] + 5 * self.__y2[i])
                for i in self.__I
            ) - 100000 * lpSum(
                self.__maximo_pasajeros[p] * self.__z[p] for p in self.__P
            )
        else:
            self.__solver += lpSum(
                self.__df["total_encuestas"][i]
                * (-1 * self.__y1[i] + self.__y2[i])
                for i in self.__I
            ) - 100000 * lpSum(
                self.__maximo_pasajeros[p] * self.__z[p] for p in self.__P
            )

        # RESTRICCIONES
        for i in self.__I:
            self.__solver += self.__y1[i] + self.__y2[i] <= 1

        for i in self.__I:
            self.__solver += (
                lpSum(self.__x[i, k] for k in self.__K)
                == self.__y1[i] + 2 * self.__y2[i]
            )

        for p in self.__P:
            if (
                self.__encuestas_maximas[p] >= self.__encuestas_minimas[p]
            ):  # Se puede cumplir con el mínimo de encuestas
                self.__solver += lpSum(
                    self.__df["total_encuestas"][i]
                    * (self.__y1[i] + self.__y2[i])
                    for i in self.__i_p[p]
                ) >= self.__encuestas_minimas[p] * (1 - self.__z[p])
            elif (
                self.__encuestas_maximas[p] < self.__encuestas_minimas[p]
            ):  # No se puede cumplir con el mínimo de encuestas
                self.__solver += lpSum(
                    self.__df["total_encuestas"][i]
                    * (self.__y1[i] + self.__y2[i])
                    for i in self.__i_p[p]
                ) >= self.__encuestas_maximas[p] * (1 - self.__z[p])

        for i in self.__I:
            for j in self.__I:
                if (
                    i != j
                    and self.__df["dia_sem"][i] == self.__df["dia_sem"][j]
                    and self.__df["hora_salida"][i]
                    <= self.__df["hora_salida"][j]
                ):
                    for k in self.__K:

                        hora_i = (
                            datetime.combine(
                                date.min, self.__df["hora_salida"][i]
                            )
                            - datetime.min
                        )

                        hora_j = (
                            datetime.combine(
                                date.min, self.__df["hora_salida"][j]
                            )
                            - datetime.min
                        )

                        consumo_i = (
                            datetime.combine(date.min, self.__df["consumo"][i])
                            - datetime.min
                        )

                        consumo_j = (
                            datetime.combine(date.min, self.__df["consumo"][j])
                            - datetime.min
                        )

                        desc = (
                            datetime.combine(date.min, self.__descanso_min)
                            - datetime.min
                        )

                        jorn = (
                            datetime.combine(date.min, self.__jornada_min)
                            - datetime.min
                        )

                        if (
                            hora_i > hora_j - (consumo_j / 2) - desc
                            # or hora_i - (consumo_i / 2) + jorn < hora_j):
                            or hora_i - (consumo_i / 2) < hora_j - jorn
                        ):
                            # or hora_i - (consumo_i / 2) - desc + jorn < hora_j):
                            self.__solver += (
                                self.__x[i, k] + self.__x[j, k] <= 1
                            )

                        elif hora_i > hora_j - consumo_j - desc:
                            self.__solver += self.__x[i, k] + self.__x[
                                j, k
                            ] <= 1 + lpSum(
                                self.__x[j, l] for l in self.__K if l != k
                            )
                        elif hora_i - consumo_i < hora_j - jorn:
                            # elif hora_i - consumo_i + jorn < hora_j:
                            # elif hora_i - consumo_i - desc + jorn < hora_j:
                            self.__solver += self.__x[i, k] + self.__x[
                                j, k
                            ] <= 1 + lpSum(
                                self.__x[i, l] for l in self.__K if l != k
                            )

        if self.__solucionador == 1:
            self.__solver.solve(GUROBI(msg=False))
        else:
            self.__solver.solve()

        self._computo_total = self.__solver.solutionTime

    def formatear_solucion(self):

        origen = []
        regiones = []

        l_vuelos_encuestador_1 = []
        l_vuelos_encuestador_2 = []
        num_vuelos_encuestados = []
        l_encuestas_1 = []
        l_encuestas_2 = []
        pasajeros_encuestados = []

        pasajeros_total = []
        num_vuelos_total = []
        encuestas_minimas = []
        encuestas_maximas = []
        donaciones = []

        for p in self.__P:
            encuestas_1 = 0
            encuestas_2 = 0
            vuelos_encuestador_1 = 0
            vuelos_encuestador_2 = 0
            regiones.append(self.__destinos[p])
            origen.append(self.__origen)
            for i in self.__i_p[p]:
                if (
                    self.__y1[i].varValue <= 1.1
                    and self.__y1[i].varValue >= 0.9
                ):
                    vuelos_encuestador_1 += 1
                    encuestas_1 += self.__df["total_encuestas"][i]
                elif (
                    self.__y2[i].varValue <= 1.1
                    and self.__y2[i].varValue >= 0.9
                ):
                    vuelos_encuestador_2 += 1
                    encuestas_2 += self.__df["total_encuestas"][i]

            l_encuestas_1.append(encuestas_1)
            l_encuestas_2.append(encuestas_2)
            pasajeros_encuestados.append(encuestas_1 + encuestas_2)
            l_vuelos_encuestador_1.append(vuelos_encuestador_1)
            l_vuelos_encuestador_2.append(vuelos_encuestador_2)
            num_vuelos_encuestados.append(
                vuelos_encuestador_1 + vuelos_encuestador_2
            )
            num_vuelos_total.append(len(self.__i_p[p]))
            pasajeros_total.append(
                self.__df_aux["ocupacion"][self.__destinos[p]]
            )
            encuestas_minimas.append(
                self.__df_aux["encuestas_minimas"][self.__destinos[p]]
            )
            encuestas_maximas.append(
                self.__df_aux["encuestas_maximas"][self.__destinos[p]]
            )

            if (
                pasajeros_encuestados[-1]
                < self.__df_aux["encuestas_minimas"][self.__destinos[p]]
            ):
                donaciones.append(
                    self.__df_aux["encuestas_minimas"][self.__destinos[p]]
                    - pasajeros_encuestados[-1]
                )
            else:
                donaciones.append(0)

        self.__df_solucion = pd.concat(
            [
                self.__df_solucion,
                pd.DataFrame(
                    {
                        "origen": origen,
                        "regiones": regiones,
                        "vuelos_total": num_vuelos_total,
                        "pasajeros_total": pasajeros_total,
                        "encuestas_min": encuestas_minimas,
                        "encuestas_max": encuestas_maximas,
                        "encuestas_1_encuestador": l_encuestas_1,
                        "encuestas_2_encuestadores": l_encuestas_2,
                        "total_encuestas": pasajeros_encuestados,
                        "donaciones": donaciones,
                        "vuelos_encuestados_1_encuestador": l_vuelos_encuestador_1,
                        "vuelos_encuestados_2_encuestadores": l_vuelos_encuestador_2,
                        "total_vuelos_encuestados": num_vuelos_encuestados,
                    }
                ),
            ]
        )

        return [
            origen,
            regiones,
            l_vuelos_encuestador_1,
            l_vuelos_encuestador_2,
            num_vuelos_encuestados,
            l_encuestas_1,
            l_encuestas_2,
            pasajeros_encuestados,
            pasajeros_total,
            num_vuelos_total,
            encuestas_minimas,
            encuestas_maximas,
            donaciones,
        ]

    def get_solucion(self):
        return self.__df_solucion
