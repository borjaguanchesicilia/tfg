from src.controlador.librerias import *


class ParametroModelo:
    def __init__(
        self,
        frame,
        texto,
        f_etiqueta,
        c_etiqueta,
        ini_selector,
        fin_selector,
        incr_selector,
        f_selector,
        c_selector,
    ):

        # Atributo etiqueta
        self.__etiqueta = Label(frame, text=texto)

        self.__etiqueta.config(
            font=("Adobe Caslon Pro", 15, "bold"), fg="#FFFFFF", bg="#333333"
        )

        self.__etiqueta.grid(row=f_etiqueta, column=c_etiqueta, padx=10)

        # Atributo selector
        self.__selector = Spinbox(
            frame, from_=ini_selector, to=fin_selector, increment=incr_selector
        )

        self.__selector.config(
            fg="#333333",
            font=("Adobe Caslon Pro", 10, "bold"),
            state="readonly",
        )

        self.__selector.grid(
            row=f_selector, column=c_selector, pady=7, padx=10
        )

    def get_valor_selector(self):
        return float(self.__selector.get())
