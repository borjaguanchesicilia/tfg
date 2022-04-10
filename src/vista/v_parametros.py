from src.controlador.c_lectura_fichero import FicheroCsv
from src.controlador.librerias import *
from src.vista.componentes.boton import Boton
from src.vista.componentes.etiqueta import Etiqueta
from src.vista.componentes.parametro import ParametroModelo
from src.vista.v_parametros import *
from src.vista.componentes.check_list import ChecklistBox
from src.vista.v_dias import VistaDias


class VistaParametros(Toplevel):
    def __init__(self, app):
        super().__init__(app)

        self.app = app

        self.__controlador = None

        # self = Toplevel(app)

        self.__vista_dias = VistaDias(self)

        # Aspecto de la ventana "Planificar"
        self.title("Menú planificación")
        self.geometry("1200x500")
        self["bg"] = "#333333"
        self.minsize(1100, 500)

        # Etiqueta cabecera
        cabecera = Frame(self)
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
        self.__f_parametros = Frame(self)
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
            self.__f_config, "Ocupación (en %):", 3, 0, 10, 100, 5, 3, 1
        )

        self.__exito = ParametroModelo(
            self.__f_config,
            "Éxito (en %):",
            4,
            0,
            10,
            100,
            5,
            4,
            1,
        )

        self.__e_checklist = Etiqueta(self.__f_config, "Aerpuertos:", 5, 0)

        self.__checklist_aer = ChecklistBox(self.__f_config)

        self.__checklist_aer.grid(padx=5, pady=5, row=6, column=0)

        self.__e_dias = Etiqueta(self.__f_config, "", 7, 0, 8)

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
            self.__vista_dias.introducir_dia,
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

    def introducir_parametros(self):
        if self.__controlador != None:

            try:
                assert len(self.get_dias()) > 0
            except:
                showerror(
                    "ERROR", "Debe introducir al menos 1 día", parent=self
                )
            else:
                try:
                    # No se ha seleccionado ningún aeropuerto
                    assert len(self.get_aeropuertos()) > 0
                except:
                    showerror(
                        "ERROR",
                        "Debe seleccionar al menos un aeropuerto",
                        parent=self,
                    )
                else:
                    self.__controlador.guardar_parametros(
                        self.get_dias(),
                        self.get_jornada_laboral(),
                        self.get_descanso(),
                        self.get_velocidad(),
                        self.get_ocupacion(),
                        self.get_exito(),
                        self.get_aeropuertos(),
                    )

                    self.destroy()
                    del self

    def obtener_dia(self):
        return str(self.__calendario.get_date()).split("-")

    def ayuda(self):
        pass

    def get_dias(self):
        self.__dias = []
        self.__dias = [dia.get_dia() for dia in self.__vista_dias.get_lista()]
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

    def get_aeropuertos(self):
        return self.__checklist_aer.get_aeropuertos()
