from src.controlador.librerias import *


class ChecklistBox(Frame):
    def __init__(self, vista):
        Frame.__init__(self, vista)

        aeropuertos = [
            "Arrecife",
            "Fuerteventura",
            "Gran Canaria",
            "Tenerife Norte",
            "Tenerife Sur",
            "La Palma",
        ]
        self.__variables = []

        for aeropuerto in aeropuertos:
            variables = StringVar(value=aeropuerto)
            self.__variables.append(variables)
            check_box = Checkbutton(
                self,
                var=variables,
                text=aeropuerto,
                onvalue=aeropuerto,
                offvalue="",
                anchor="w",
                width=20,
                fg="#333333",
                bg="#FFFFFF",
                relief="flat",
                highlightthickness=0,
            )
            check_box.pack(side="top", fill="x", anchor="w")

    def get_aeropuertos(self):
        aeropuertos = []
        for variable in self.__variables:
            aeropuerto = variable.get()
            if aeropuerto != "":
                aeropuertos.append(aeropuerto)

        return aeropuertos
