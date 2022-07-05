from src.modelo.m_planificar import ModeloPlanificar
from src.funciones_aux import conversor_aeropueros
from src.librerias import *
from src.vista.v_barra_progreso import VistaBarraProgreso
from src.controlador.c_barra_progreso import BarraProgreso
from src.modelo.operaciones.modelo_matematico import Modelo


class ControladorPlanificar:
    def __init__(
        self,
        vista_planificar,
        controlador_general,
        controlador_parametros,
        controlador_etl,
    ):

        self.__v_planificar = vista_planificar
        self.__controlador_general = controlador_general
        self.__controlador_parametros = controlador_parametros
        self.__controlador_etl = controlador_etl
        self.__modelo_planificar = ModeloPlanificar()
        self.__f_o = -1
        self.__solver = -1

    def comprobar_funcion_objetivo(self):
        f_objetivo = self.__v_planificar.get_funcion_objetivo()
        if type(f_objetivo) != list:
            f_objetivo = f_objetivo.get_valores()
        if len(f_objetivo) != 1:
            showerror(
                "ERROR",
                "Debe seleccionar 1 solo tipo de función objetivo",
                parent=self.__v_planificar,
            )
            return False
        else:
            if len(f_objetivo[0]) == 7:  # Neutral
                self.__f_o = 0
            elif (
                len(f_objetivo[0]) == 40
            ):  # Priorizar empleo de varios encuestadores
                self.__f_o = 1
            else:  # Penalizar empleo de un encuestador
                self.__f_o = 2
            return True

    def comprobar_solver(self):
        solver = self.__v_planificar.get_solver()
        if type(solver) != list:
            solver = solver.get_valores()
        if len(solver) != 1:
            showerror(
                "ERROR",
                "Debe seleccionar 1 solo solver",
                parent=self.__v_planificar,
            )
            return False
        else:
            if len(solver[0]) == 3:  # CBC
                self.__solver = 0
            else:  # Gurobi
                self.__solver = 1
            return True

    def get_funcion_objetivo(self):
        return self.__f_o

    def get_solver(self):
        return self.__solver

    def planificar(self):
        if self.comprobar_funcion_objetivo() != False:

            if self.comprobar_solver() != False:
                origenes = (
                    self.__controlador_etl.get_modelo_etl().get_aeropuertos()
                )

                for aer in origenes:

                    df = self.__controlador_etl.get_modelo_etl().get_df(aer)
                    aviones = (
                        self.__controlador_etl.get_modelo_etl().get_df_aviones()
                    )
                    jornada = (
                        self.__controlador_parametros.get_modelo_parametros().get_jornada()
                    )
                    entrevistadores = 2
                    descanso = (
                        self.__controlador_parametros.get_modelo_parametros().get_descanso()
                    )
                    velocidad = (
                        self.__controlador_parametros.get_modelo_parametros().get_velocidad()
                    )
                    ocupacion = (
                        self.__controlador_parametros.get_modelo_parametros().get_ocupacion()
                    )
                    exito = (
                        self.__controlador_parametros.get_modelo_parametros().get_exito()
                    )

                    modelo = Modelo(
                        aer,
                        df,
                        aviones,
                        jornada,
                        entrevistadores,
                        descanso,
                        velocidad,
                        ocupacion,
                        exito,
                        self.__f_o,
                        self.__solver,
                    )

                    self.__v_planificar.attributes("-topmost", False)

                    self.__v_barra_progreso = VistaBarraProgreso(
                        self.__v_planificar,
                        "Progreso SOL",
                        f"Resolviendo para {aer}...",
                    )
                    controlador_barra_progreso = BarraProgreso(
                        self.__v_barra_progreso
                    )
                    self.__v_barra_progreso.set_controlador(
                        controlador_barra_progreso
                    )

                    try:
                        controlador_barra_progreso.aumentar_progreso(
                            "16%: Realizando calculos iniciales"
                        )
                        modelo.calculos_iniciales()
                    except:
                        showerror(
                            "ERROR",
                            "Al realizar calculos iniciales",
                            parent=self.__v_planificar,
                        )
                    else:
                        try:
                            controlador_barra_progreso.aumentar_progreso(
                                "32%: Calculando encuestas"
                            )
                            modelo.calculo_encuestas()
                        except:
                            showerror(
                                "ERROR",
                                "Al obtener el total de encuestas",
                                parent=self.__v_planificar,
                            )
                        else:
                            try:
                                controlador_barra_progreso.aumentar_progreso(
                                    "48%: Formateando las horas"
                                )
                                modelo.formatos_horas()
                            except:
                                showerror(
                                    "ERROR",
                                    "Al formatear las horas",
                                    parent=self.__v_planificar,
                                )
                            else:
                                try:
                                    controlador_barra_progreso.aumentar_progreso(
                                        "64%: Calculando destinos"
                                    )
                                    modelo.calculos_destinos()
                                except:
                                    showerror(
                                        "ERROR",
                                        "Al calcular los destinos",
                                        parent=self.__v_planificar,
                                    )
                                else:
                                    # iniciar_crono = time()
                                    try:
                                        controlador_barra_progreso.aumentar_progreso(
                                            "84%: Resolviendo problema"
                                        )
                                        modelo.resolver()
                                    except:
                                        showerror(
                                            "ERROR",
                                            "Al resolver",
                                            parent=self.__v_planificar,
                                        )
                                    else:

                                        self.__modelo_planificar.set_tiempos(
                                            aer, modelo
                                        )
                                        try:
                                            controlador_barra_progreso.aumentar_progreso(
                                                "100%: Formateando solución"
                                            )
                                            modelo.formatear_solucion()
                                        except:
                                            showerror(
                                                "ERROR",
                                                "Al formatear la solución",
                                                parent=self.__v_planificar,
                                            )
                                        else:
                                            self.__modelo_planificar.set_solucion(
                                                modelo
                                            )
                                            self.__v_barra_progreso.destroy()

                self.__v_planificar.destroy()
                self.__controlador_general.planificaion_realizada()
                self.__modelo_planificar.generar_fichero_solucion()
                self.__modelo_planificar.generar_fichero_tiempos()
            else:
                return -2
        else:
            return -1
