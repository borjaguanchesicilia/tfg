from src.controlador.c_lectura_fichero import FicheroCsv
from src.controlador.librerias import *
from src.vista.v_parametros import *
from src.vista.componentes.check_list import ChecklistBox


class VistaEtl(Toplevel):
    def __init__(self, app):
        super().__init__(app)

        self.app = app

        self.__controlador = None

        # Aspecto de la ventana "Etl"
        self.title("Menú ETL")
        self.geometry("1200x500")
        self["bg"] = "#333333"
        self.minsize(1100, 500)
        self.attributes("-topmost", True)

        # Etiqueta cabecera
        cabecera = Frame(self)
        cabecera.config(bg="#333333")

        titulo = Label(cabecera, text="Menú de ETL")

        titulo.config(
            font=("Adobe Caslon Pro", 20, "bold"), fg="#FFFFFF", bg="#333333"
        )

        titulo.pack(padx=5, pady=15)

        cabecera.pack(padx=10, pady=20)

        # Etiqueta cabecera
        f_seleccion = Frame(self)
        f_seleccion.config(bg="#333333")

        # Introducir fichero GESLOT
        self.__e_fichero_vue = Etiqueta(f_seleccion, "Fichero:", 2, 2)

        self.__b_fichero_vue = Boton(
            f_seleccion,
            "Introducir fichero GESLOT",
            partial(self.introducir_fic_vue, self.__e_fichero_vue),
            2,
            0,
            15,
        )

        # Introducir fichero aviones
        self.__e_fichero_avi = Etiqueta(f_seleccion, "Fichero:", 3, 2)

        self.__b_fichero_avi = Boton(
            f_seleccion,
            "Introducir fichero aviones",
            partial(self.introducir_fic_avi, self.__e_fichero_avi),
            3,
            0,
            15,
        )

        self.boton_etl = Boton(
            f_seleccion, "Aplicar ETL", self.aplicar_etl, 4, 0, 15, 2
        )

        f_seleccion.pack(padx=10, pady=20)

    def set_controlador(self, controlador):
        self.__controlador = controlador

    def introducir_fic_vue(self, etiqueta):
        self.__fic_vue = FicheroCsv(self, etiqueta)

    def introducir_fic_avi(self, etiqueta):
        self.__fic_avi = FicheroCsv(self, etiqueta)

    def get_fic_vue(self):
        return self.__fic_vue.get_df()

    def get_fic_avi(self):
        return self.__fic_avi.get_df()

    def set_etiqueta_fichero(self, nombre_fichero, etiqueta):
        etiqueta.set_texto("Fichero: " + nombre_fichero)

    def aplicar_etl(self):
        if self.__controlador != None:
            try:
                test = self.get_fic_vue()
            except:
                showerror(
                    "ERROR", "Falta introducir el fichero GESLOT", parent=self
                )
            else:
                try:
                    test = self.get_fic_avi()
                except:
                    showerror(
                        "ERROR",
                        "Falta introducir el fichero de aviones",
                        parent=self,
                    )
                else:
                    self.__controlador.aplicar_etl(
                        self.get_fic_vue(), self.get_fic_avi()
                    )
