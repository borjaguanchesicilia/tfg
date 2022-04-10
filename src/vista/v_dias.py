from src.controlador.librerias import *
from src.vista.v_parametros import *
from src.vista.componentes.check_list import ChecklistBox
from src.vista.componentes.scroll import ScrollBar
from src.vista.componentes.parametro_dia import ParametroDia


class VistaDias:
    def __init__(self, v_parametros):

        self.__vista_parametros = v_parametros

        self.set_ventana_dias()

        self.__lista_dias = []

    def set_ventana_dias(self):
        self.__ventana_dias = Toplevel(self.__vista_parametros)

        # Aspecto de la ventana "Días"
        self.__ventana_dias.title("Días")
        self.__ventana_dias.minsize(400, 150)
        self.__ventana_dias.maxsize(400, 150)

        # Configuración de la ventana "Días"
        self.__ventana_dias.protocol("WM_DELETE_WINDOW", self.descativar)
        self.__ventana_dias.attributes('-topmost',True)

        self.__scroll_bar = ScrollBar(self.__ventana_dias)
        self.__scroll_bar.pack()

    def get_lista(self):
        return self.__lista_dias

    def get_tam_lista_dias(self):
        return len(self.__lista_dias)

    def introducir_dia(self):
        fecha = self.__vista_parametros.obtener_dia()
        fecha = str(fecha[2]) + "/" + str(fecha[1]) + "/" + str(fecha[0])
        self.__lista_dias.append(
            ParametroDia(self.get_scroll_bar(), self, fecha, self.get_tam_lista_dias())
        )

    def borrar_dia(self, objeto):
        self.__lista_dias.remove(objeto)

        [i.actualizar_fila() for i in self.__lista_dias]

        self.__ventana_dias.destroy()
        self.set_ventana_dias()

        lista_aux = self.__lista_dias
        self.__lista_dias = []
        self.__lista_dias = [ParametroDia(self.get_scroll_bar(), self, i.get_dia(), i.get_fila()) for i in lista_aux]

    def get_scroll_bar(self):
        return self.__scroll_bar.get_frame_scroll()

    def actualizar_vista(self):
        self.__ventana_dias.update()

    def descativar(self):
        pass