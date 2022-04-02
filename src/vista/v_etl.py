from src.controlador.librerias import *
from src.vista.v_parametros import *


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

        """# Texto informátivo
        f_texto_info = Frame(ventana_etl)
        f_texto_info.config(bg="#333333")

        texto_info = Text(f_texto_info)

        texto_info.insert(END, "Se espera que se "
            "introduzca un fichero GESLOT proporcionado por AENA. "
            "A dicho fichero se le aplicará un ETL (), y como "
            "resultado se obtendrá un dataframe por cada aeropuerto "
            "de manera que se podrá proceder a modificar algunos de "
            "los datos o bien proceder a introducir los parámetros de "
            "configuración para el modelo.")

        texto_info.config(font=("Adobe Caslon Pro", 10), fg="#FFFFFF",
            bg="#333333")

        texto_info.pack()
        
        
        f_texto_info.pack(padx=10, pady=20)"""

        # Botón "Planificar"
        frame_botones = Frame(ventana_etl)
        frame_botones.config(bg="#333333")

        boton_planificar = Button(
            frame_botones, text="Introducir fichero de vuelos"
        )

        boton_planificar.config(
            font=("Adobe Caslon Pro", 15, "bold"),
            fg="#FFFFFF",
            bg="#333333",
            command=self.aplicar_etl,
        )

        boton_planificar.grid(
            pady=30,
            padx=10,
            row=0,
            column=0,
            columnspan=2,
            sticky=S + N + E + W,
        )

        frame_botones.pack(padx=10, pady=20)

    def set_controlador(self, controlador):
        self.__controlador = controlador

    def aplicar_etl(self):
        print("Aplicar ETL")
        if self.__controlador != None:
            self.__controlador.etl()
