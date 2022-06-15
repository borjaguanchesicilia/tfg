from src.librerias import *


class ChecklistBox(Frame):
    def __init__(self, vista, parametros):
        Frame.__init__(self, vista)

        self.__variables = []

        for parametro in parametros:
            variables = StringVar(value=parametro)
            self.__variables.append(variables)
            check_box = Checkbutton(
                self,
                var=variables,
                text=parametro,
                onvalue=parametro,
                offvalue="",
                anchor="w",
                width=40,
                relief="flat",
                highlightthickness=0,
            )
            check_box.config(
                font=("Adobe Caslon Pro", 8, "bold"),
                fg="#FFFFFF",
                bg="#333333",
                selectcolor="#333333",
            )
            check_box.pack(side="top", fill="x", anchor="w")

    def get_valores(self):
        valores = []
        for variable in self.__variables:
            valor_aux = variable.get()
            if valor_aux != "":
                valores.append(valor_aux.replace("  ", ""))

        return valores
