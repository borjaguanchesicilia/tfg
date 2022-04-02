from src.controlador.c_lectura_fichero import FicheroCsv
from src.controlador.librerias import *
from src.vista.componentes.boton import Boton
from src.vista.componentes.etiqueta import Etiqueta
from src.vista.componentes.parametro import ParametroModelo
from src.vista.v_parametros import *


class VistaParametros:
    def __init__(self, app):

        self.__controlador = None

        self.__ventana_planificar = Toplevel(app)

        # Aspecto de la ventana "Planificar"
        self.__ventana_planificar.title("Menú planificación")
        self.__ventana_planificar.geometry("1200x500")
        self.__ventana_planificar["bg"] = "#333333"
        self.__ventana_planificar.minsize(1100, 500)

        # Etiqueta cabecera
        cabecera = Frame(self.__ventana_planificar)
        cabecera.config(bg="#333333")

        titulo = Label(
            cabecera, text=("Menú de planificación de " "encuestas")
        )

        titulo.config(
            font=("Adobe Caslon Pro", 20, "bold"), fg="#FFFFFF", bg="#333333"
        )

        titulo.pack(padx=5, pady=15)

        cabecera.pack(padx=10, pady=20)

        # Parametros
        self.__f_parametros = Frame(self.__ventana_planificar)
        self.__f_parametros.config(bg="#333333")

        # Parametros de configuracion
        self.__f_config = Frame(self.__f_parametros)
        self.__f_config.config(bg="#333333")

        self.__jornada_laboral = ParametroModelo(
            self.__f_config,
            "Jornada Laboral Máxima (en horas):",
            0,
            0,
            1,
            8,
            1,
            0,
            1,
        )

        self.__descanso = ParametroModelo(
            self.__f_config,
            "Descanso entre vuelos (en minutos):",
            1,
            0,
            10,
            60,
            0.5,
            1,
            1,
        )

        self.__velocidad = ParametroModelo(
            self.__f_config,
            "Velocidad de encuesta (en minutos):",
            2,
            0,
            0.1,
            1,
            0.05,
            2,
            1,
        )

        self.__ocupacion = ParametroModelo(
            self.__f_config, "Ocupación (en %):", 3, 0, 0.1, 1, 0.05, 3, 1
        )

        self.__exito = ParametroModelo(
            self.__f_config,
            "Éxito (en %):",
            4,
            0,
            0.1,
            1,
            0.05,
            4,
            1,
        )

        # Introducir fichero GESLOT
        self.__e_fichero_vue = Etiqueta(self.__f_config, "", 8, 0)

        self.__b_fichero_vue = Boton(
            self.__f_config,
            "Introducir fichero GESLOT",
            partial(self.introducir_fic_vue, self.__e_fichero_vue),
            7,
            0,
            15,
        )

        # Introducir fichero aviones
        self.__e_fichero_avi = Etiqueta(self.__f_config, "", 10, 0)

        self.__b_fichero_avi = Boton(
            self.__f_config,
            "Introducir fichero aviones",
            partial(self.introducir_fic_avi, self.__e_fichero_avi),
            9,
            0,
            15,
        )

        self.__e_dias = Etiqueta(self.__f_config, "", 11, 0, 8)

        self.__f_config.pack(padx=60, side=LEFT)

        # Calendario
        self.__f_calendario = Frame(self.__f_parametros)
        self.__f_calendario.config(bg="#333333")

        fecha = str(date.today()).split("-")

        self.__calendario = Calendar(
            self.__f_calendario,
            selectmode="day",
            year=int(fecha[0]),
            month=int(fecha[1]),
            day=int(fecha[2]),
            date_pattern="y-mm-dd",
        )

        self.__calendario.grid(
            pady=5,
            padx=10,
            row=0,
            column=0,
            columnspan=1,
            sticky=S + N + E + W,
        )

        # Boton introducir día
        self.__boton__intro_dia = Boton(
            self.__f_calendario,
            "Introducir día",
            self.introducir_dia,
            1,
            0,
            20,
        )

        self.__dias = []

        # Boton ayuda
        self.__boton_ayuda = Boton(
            self.__f_calendario, "Ayuda", self.ayuda, 2, 0
        )

        # Boton introducir parametros
        self.__boton__intro_par = Boton(
            self.__f_calendario,
            "Introducir parámetros",
            self.introducir_parametros,
            3,
            0,
            20,
        )

        self.__f_calendario.pack(padx=20, side=LEFT)

        self.__f_parametros.pack(padx=10, pady=20)

    def set_controlador(self, controlador):
        self.__controlador = controlador

    def introducir_fic_vue(self, etiqueta):
        self.__fic_vue = FicheroCsv(self, etiqueta)

    def introducir_fic_avi(self, etiqueta):
        self.__fic_avi = FicheroCsv(self, etiqueta)

    def introducir_dia(self):
        fecha = str(self.__calendario.get_date()).split("-")
        """fecha = datetime.combine(
            date(
                int(fecha[0]),
                int(fecha[1]),
                int(fecha[2]),  # Año  # Mes
            ),  # Día
            datetime.min.time(),
        )"""
        fecha = str(fecha[2]) + "/" + str(fecha[1]) + "/" + str(fecha[0])
        if len(self.__dias) == 0:
            self.__dias.append("Días:")

        self.__dias.append(fecha)

        if len(self.__dias) < 10:
            self.__e_dias.set_texto(self.__dias)
            self.__ventana_planificar.update()

    def introducir_parametros(self):
        if self.__controlador != None:
            try:
                test = self.get_fic_vue()
            except:
                showerror("ERROR", "Falta introducir el fichero GESLOT")
            else:
                try:
                    test = self.get_fic_avi()
                except:
                    showerror(
                        "ERROR", "Falta introducir el fichero de aviones"
                    )
                else:
                    try:
                        assert len(self.__dias) > 0
                    except:
                        showerror("ERROR", "Debe introducir al menos 1 día")
                    else:
                        self.__controlador.guardar_parametros(
                            self.get_dias(),
                            self.get_jornada_laboral(),
                            self.get_descanso(),
                            self.get_velocidad(),
                            self.get_ocupacion(),
                            self.get_exito(),
                            self.get_fic_vue(),
                            self.get_fic_avi(),
                        )

                        self.__ventana_planificar.destroy()
                        del self

    def ayuda(self):
        pass

    def get_dias(self):
        return self.__dias

    def get_jornada_laboral(self):
        return self.__jornada_laboral.get_valor_selector()

    def get_descanso(self):
        return self.__descanso.get_valor_selector()

    def get_velocidad(self):
        return self.__velocidad.get_valor_selector()

    def get_ocupacion(self):
        return self.__ocupacion.get_valor_selector()

    def get_exito(self):
        return self.__exito.get_valor_selector()

    def get_fic_vue(self):
        return self.__fic_vue.get_nombre_fichero()

    def get_fic_avi(self):
        return self.__fic_avi.get_nombre_fichero()

    def set_etiqueta_fichero(self, nombre_fichero, etiqueta):
        etiqueta.set_texto("Fichero: " + nombre_fichero)
        self.__ventana_planificar.update()
