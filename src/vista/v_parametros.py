from src.controlador.c_etl import ControladorEtl
from src.controlador.librerias import *
from src.vista.componentes.boton import Boton
from src.vista.componentes.etiqueta import Etiqueta
from src.vista.componentes.parametro import ParametroModelo
from src.vista.v_parametros import *


class VistaParametros:
    def __init__(self, app):

        self.__controlador = None

        self.__ventana_planificar = Toplevel(app)

        # Aspecto de la ventana 'Planificar'
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

        # Boton 'Introducir fichero'
        self.__b_fichero = Boton(
            self.__f_config,
            "Introducir fichero",
            self.introducir_fichero,
            7,
            0,
            15,
        )

        self.__e_fichero = Etiqueta(self.__f_config, "Fichero:", 8, 0)

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

        # Boton introducir parametros
        self.__boton_ayuda = Boton(
            self.__f_calendario,
            "Introducir parámetros",
            self.introducir_parametros,
            1,
            0,
            20,
        )

        # Boton ayuda
        self.__boton_ayuda = Boton(
            self.__f_calendario, "Ayuda", self.ayuda, 2, 0
        )

        self.__f_calendario.pack(padx=20, side=LEFT)

        self.__f_parametros.pack(padx=10, pady=20)

    def set_controlador(self, controlador):
        self.__controlador = controlador

    def introducir_fichero(self):
        controlador = ControladorEtl(self)
        self.set_controlador(controlador)

    def ayuda(self):
        pass

    def introducir_parametros(self):
        if self.__controlador != None:
            self.__controlador.guardar_parametros(
                self.get_semana(),
                self.get_jornada_laboral(),
                self.get_descanso(),
                self.get_velocidad(),
                self.get_ocupacion(),
                self.get_exito(),
            )

    def get_semana(self):

        semana = ""
        fecha_ini = str(self.__calendario.get_date()).split("-")
        fecha_ini = datetime.combine(
            date(
                int(fecha_ini[0]),
                int(fecha_ini[1]),
                int(fecha_ini[2]),  # Año  # Mes
            ),  # Día
            datetime.min.time(),
        )

        for i in range(0, 7):
            fecha_aux = fecha_ini + timedelta(days=i)
            fecha_formateada = fecha_aux.strftime("%d/%m/%Y")
            semana += str(fecha_formateada) + " \n"

        return semana[:-1]

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

    def set_etiqueta_fichero(self, nombre_fichero):
        self.__e_fichero.set_texto(nombre_fichero)
        self.__ventana_planificar.update()
