from src.librerias import *
from src.vista.componentes_vistas.check_list import ChecklistBox
from src.vista.componentes_vistas.etiqueta import Etiqueta


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

        # Etiqueta cabecera
        self.__cabecera = Frame(self)
        self.__cabecera.config(bg="#333333")

        self.__titulo = Label(
            self.__cabecera,
            text=("Planificador:"),
            fg="#FFFFFF",
            bg="#333333",
        )

        self.__titulo.config(font=("Adobe Caslon Pro", 20, "bold"))
        self.__titulo.pack(padx=5, pady=15)

        self.__cabecera.pack(padx=10, pady=20)

        # Selector función objetivo
        self.__f_fo = LabelFrame(self)
        self.__f_fo.config(
            font=("Adobe Caslon Pro", 15, "bold"),
            fg="#FFFFFF",
            bg="#333333",
            labelanchor="n",
        )


        self.__e_fo = Etiqueta(self.__f_fo, "Función objetivo:", 0, 0)
        funcion_objetivo = ['Tipo 1', 'Tipo 2', 'Tipo 3']
        self.__checklist_fo = ChecklistBox(self.__f_fo, funcion_objetivo)
        self.__checklist_fo.grid(padx=5, pady=5, row=1, column=0)

        self.__f_fo.pack(padx=10, pady=20)


        # Selector solver
        self.__f_solver = LabelFrame(self)
        self.__f_solver.config(
            font=("Adobe Caslon Pro", 15, "bold"),
            fg="#FFFFFF",
            bg="#333333",
            labelanchor="n",
        )


        self.__e_solver = Etiqueta(self.__f_solver, "Solver:", 0, 0)
        solver = ['CBC', 'GUROBI']
        self.__checklist_solver = ChecklistBox(self.__f_solver, solver)
        self.__checklist_solver.grid(padx=5, pady=5, row=1, column=0)

        self.__f_solver.pack(padx=10, pady=20)


    def set_controlador(self, controlador):
        self.__controlador = controlador