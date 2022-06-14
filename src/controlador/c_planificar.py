class ControladorPlanificar:
    def __init__(self, vista_planificar, controlador_general):
        
        self.__v_planificar = vista_planificar
        self.__controlador_general = controlador_general
        self.__f_o = ""
        self.__solver = []

    def planificar(self):
        self.comprobar_funcion_objetivo()
    
    
    def comprobar_funcion_objetivo(self):
        f_o = self.__v_planificar.get_funcion_objetivo().get_aeropuertos()
        if len(f_o) != 1:
            print("ERROR")
        else:
            self.__f_o = f_o


    def comprobar_solver(self, solver):
        solver = self.__v_planificar.get_solver().get_aeropuertos()
        if len(solver) == 0:
            print("ERROR")
        else:
            print()