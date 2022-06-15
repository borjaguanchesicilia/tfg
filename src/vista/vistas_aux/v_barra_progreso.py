from src.librerias import *


class VistaBarraProgreso(Toplevel):
    def __init__(self, app, titulo, texto):
        super().__init__(app)

        self.app = app

        self.__controlador = None

        # Aspecto de la ventana "Barra de progreso"
        self.title(titulo)
        self.geometry("300x100")
        self["bg"] = "#333333"
        self.minsize(500, 100)
        self.attributes("-topmost", True)
        self.attributes("-type", "splash")

        self.__f_principal = LabelFrame(self, text=texto)
        self.__f_principal.config(
            font=("Adobe Caslon Pro", 12, "bold"),
            fg="#FFFFFF",
            bg="#333333",
            labelanchor="n",
            borderwidth=2,
        )

        self.__estilo_barra = ttk.Style()
        self.__estilo_barra.configure(
            "estilo.Horizontal.TProgressbar", background="#38EA60"
        )

        self.__barra_progreso = ttk.Progressbar(
            self.__f_principal,
            orient=HORIZONTAL,
            length=100,
            mode="determinate",
            style="estilo.Horizontal.TProgressbar",
        )
        self.__barra_progreso.pack(fill=X, expand=1)
        self.__etiqueta = Label(self.__f_principal, text="")
        self.__etiqueta.config(
            font=("Adobe Caslon Pro", 8, "bold"), fg="#FFFFFF", bg="#333333"
        )
        self.__etiqueta.pack()

        self.__f_principal.pack(fill=BOTH)

    def set_controlador(self, controlador):
        self.__controlador = controlador

    def set_valor_barra(self):
        self.__barra_progreso["value"] += 12.4

    def set_paso_barra(self, operacion):
        self.__etiqueta.config(text=operacion)
