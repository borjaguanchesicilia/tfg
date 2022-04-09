from src.controlador.librerias import *
from src.vista.v_parametros import *
from src.vista.componentes.check_list import ChecklistBox


class VistaEtl:
    def __init__(self, app):

        self.__controlador = None

        self.__ventana_etl = Toplevel(app)

        # Aspecto de la ventana "Etl"
        self.__ventana_etl.title("Menú ETL")
        self.__ventana_etl.geometry("1200x500")
        self.__ventana_etl["bg"] = "#333333"
        self.__ventana_etl.minsize(1100, 500)

        # Etiqueta cabecera
        cabecera = Frame(self.__ventana_etl)
        cabecera.config(bg="#333333")

        titulo = Label(cabecera, text="Menú de ETL")

        titulo.config(
            font=("Adobe Caslon Pro", 20, "bold"), fg="#FFFFFF", bg="#333333"
        )

        titulo.pack(padx=5, pady=15)

        cabecera.pack(padx=10, pady=20)

        # Etiqueta cabecera
        f_seleccion = Frame(self.__ventana_etl)
        f_seleccion.config(bg="#333333")

        boton_planificar = Boton(
            f_seleccion, "Aplicar ETL", self.aplicar_etl, 0, 1
        )

        # Introducir fichero GESLOT
        self.__e_fichero_vue = Etiqueta(f_seleccion, "", 1, 0)

        self.__b_fichero_vue = Boton(
            f_seleccion,
            "Introducir fichero GESLOT",
            partial(self.introducir_fic_vue, self.__e_fichero_vue),
            7,
            0,
            15,
        )

        # Introducir fichero aviones
        self.__e_fichero_avi = Etiqueta(f_seleccion, "", 3, 0)

        self.__b_fichero_avi = Boton(
            f_seleccion,
            "Introducir fichero aviones",
            partial(self.introducir_fic_avi, self.__e_fichero_avi),
            9,
            0,
            15,
        )

        f_seleccion.pack(padx=10, pady=20)

    def set_controlador(self, controlador):
        self.__controlador = controlador

    def introducir_fic_vue(self, etiqueta):
        self.__fic_vue = FicheroCsv(self.__ventana_etl, etiqueta)

    def introducir_fic_avi(self, etiqueta):
        self.__fic_avi = FicheroCsv(self.__ventana_etl, etiqueta)

    def aplicar_etl(self):
        if self.__controlador != None:
            try:
                test = self.get_fic_vue()
            except:
                showerror("ERROR", "Falta introducir el fichero GESLOT", parent=self.__ventana_parametros)
            else:
                try:
                    test = self.get_fic_avi()
                except:
                    showerror(
                        "ERROR", "Falta introducir el fichero de aviones", parent=self.__ventana_parametros
                    )
                else:
                    self.__controlador.aplicar_etl()
