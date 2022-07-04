from src.librerias import *
from src.vista.componentes_vistas.check_list import ChecklistBox
from src.vista.componentes_vistas.etiqueta import Etiqueta
from src.vista.componentes_vistas.boton import Boton


class VistaPlanificar(Toplevel):
    def __init__(self, app):
        super().__init__(app)

        self.app = app
        self.__controlador = None

        # Aspecto de la ventana "Planificar"
        self.title("Menú planificación")
        self.geometry("1200x500")
        self["bg"] = "#333333"
        self.minsize(1100, 500)
        self.attributes("-topmost", True)

        self.__menu = LabelFrame(self, text=("Planificador:"))
        self.__menu.config(
            font=("Adobe Caslon Pro", 20, "bold"),
            fg="#FFFFFF",
            bg="#333333",
            labelanchor="n",
        )

        # Selector función objetivo
        self.__e_fo = Etiqueta(self.__menu, "Función objetivo:", 0, 0)
        funcion_objetivo = [
            "Neutral",
            "Priorizar empleo de varios encuestadores",
            "Penalizar empleo de un encuestador",
        ]
        self.__checklist_fo = ChecklistBox(self.__menu, funcion_objetivo)
        self.__checklist_fo.grid(padx=15, pady=5, row=0, column=1)

        # Selector solver
        self.__e_solver = Etiqueta(self.__menu, "Solver:", 1, 0)
        solver = ["CBC", "GUROBI"]
        self.__checklist_solver = ChecklistBox(self.__menu, solver)
        self.__checklist_solver.grid(padx=15, pady=5, row=1, column=1)

        # BOtón planificar
        self.boton_planificar = Boton(
            self.__menu, "Planificar", self.invocar_planificador, 2, 0
        )

        self.__menu.pack(padx=20, pady=20)

    def set_controlador(self, controlador):
        self.__controlador = controlador

    def get_funcion_objetivo(self):
        return self.__checklist_fo

    def get_solver(self):
        return self.__checklist_solver

    def set_funcion_objetivo(self, f_objetivo):
        self.__checklist_fo = f_objetivo

    def set_solver(self, solver):
        self.__checklist_solver = solver

    def invocar_planificador(self):
        self.__controlador.planificar()
