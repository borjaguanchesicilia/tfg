from src.controlador.librerias import *


class VistaBarraProgreso(Toplevel):
    def __init__(self, app):
        super().__init__(app)

        self.app = app

        self.__controlador = None

        # Aspecto de la ventana "Barra de progreso"
        self.title("Progreso ETL")
        self.geometry("300x300")
        self["bg"] = "#333333"
        self.minsize(500, 300)
        self.attributes("-topmost", True)
        self.attributes('-type', 'splash')

        self.__titulo = Label(self, text="Aplicando ETL...")
        self.__titulo.config(
            font=("Adobe Caslon Pro", 20, "bold"), fg="#FFFFFF", bg="#333333"
        )
        self.__titulo.pack()

        self.__estilo_barra = ttk.Style()
        self.__estilo_barra.configure("estilo.Horizontal.TProgressbar", background='#38EA60')

        self.__barra_progreso = ttk.Progressbar(self, orient=HORIZONTAL, length=100, mode='determinate', style="estilo.Horizontal.TProgressbar")
        self.__barra_progreso.pack(fill=X, expand=1)
        self.__etiqueta = Label(self, text="")
        self.__etiqueta.config(
            font=("Adobe Caslon Pro", 15, "bold"), fg="#FFFFFF", bg="#333333"
        )
        self.__etiqueta.pack()

    def set_controlador(self, controlador):
        self.__controlador = controlador

    def set_valor_barra(self):
        self.__barra_progreso['value'] += 12.4

    def set_paso_barra(self, operacion):
        self.__etiqueta.config(text=operacion)