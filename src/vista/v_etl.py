from src.controlador.librerias import *
from src.vista.v_parametros import *
from src.vista.componentes.check_list import ChecklistBox


class VistaEtl:
    def __init__(self, app):

        self.__controlador = None

        ventana_etl = Toplevel(app)

        # Aspecto de la ventana "Etl"
        ventana_etl.title("Menú ETL")
        ventana_etl.geometry("1200x500")
        ventana_etl["bg"] = "#333333"
        ventana_etl.minsize(1100, 500)

        # Etiqueta cabecera
        cabecera = Frame(ventana_etl)
        cabecera.config(bg="#333333")

        titulo = Label(cabecera, text="Menú de ETL")

        titulo.config(
            font=("Adobe Caslon Pro", 20, "bold"), fg="#FFFFFF", bg="#333333"
        )

        titulo.pack(padx=5, pady=15)

        cabecera.pack(padx=10, pady=20)

        # Etiqueta cabecera
        f_seleccion = Frame(ventana_etl)
        f_seleccion.config(bg="#333333")

        e_f_seleccion = Label(
            f_seleccion,
            text="Seleccione sobre que aeropuerto o aeropuertos quiere planificar:",
        )

        e_f_seleccion.config(
            font=("Adobe Caslon Pro", 15, "bold"), fg="#FFFFFF", bg="#333333"
        )

        e_f_seleccion.grid(
            pady=5,
            padx=5,
            row=0,
            column=0,
            columnspan=2,
            sticky=S + N + E + W,
        )

        self.__checklist_aer = ChecklistBox(f_seleccion)

        self.__checklist_aer.grid(padx=5, pady=5, row=1, column=0)

        boton_planificar = Boton(
            f_seleccion, "Aplicar ETL", self.aplicar_etl, 1, 1
        )

        f_seleccion.pack(padx=10, pady=20)

    def set_controlador(self, controlador):
        self.__controlador = controlador

    def aplicar_etl(self):
        if self.__controlador != None:
            lista_aeropuertos = self.__checklist_aer.get_aeropuertos()
            if len(lista_aeropuertos) == 0:
                showerror("ERROR", "Debe seleccionar al menos un aeropuerto")
            else:
                self.__controlador.aplicar_etl(lista_aeropuertos)
