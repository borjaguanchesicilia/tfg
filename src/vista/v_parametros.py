from src.controlador.librerias import *


class VistaParametros(Frame):

    def __init__(self, master, titulo_ventana):
        
        self.__frame = Frame(master)


        # Controlador
        self.__controlador = None

 
        # Etiqueta cabecera
        self.__cabecera = Frame(master)
        self.__titulo = Label(self.__cabecera, text=titulo_ventana)
        self.__titulo.config(font=("Adobe Caslon Pro", 30))
        self.__titulo.pack(padx=5, pady=5)
        self.__cabecera.pack(padx=10, pady=20)


        # Lista de parámetros
        self.__jornada_laboral = ParametroModelo(
            self.__frame, ["Jornada Laboral Máxima (en horas):", 
            0, 0, 1, 8, 1, 0, 1])
        
        self.__descanso = ParametroModelo(
            self.__frame, ["Descanso entre vuelos (en minutos):",
            1, 0, 10, 60, 0.5, 1, 1])

        self.__velocidad = ParametroModelo(
            self.__frame, ["Velocidad de encuesta (en minutos):",
            2, 0, 0.1, 1, 0.05, 2, 1])
        
        self.__ocupacion = ParametroModelo(
            self.__frame, ["Ocupación (en %):", 
            3, 0, 0.1, 1, 0.05, 3, 1])
        
        self.__exito = ParametroModelo(
            self.__frame, ["Éxito (en %):", 4, 0, 0.1, 1, 0.05, 4, 1])


        # Boton introducir parametros
        self.__boton_introducir = Button(
            self.__frame, text="Introducir parámetros", 
            command=self.introducir_parametros)
        
        self.__boton_introducir.config(
            font=("Adobe Caslon Pro", 10, 'bold'))
        
        self.__boton_introducir.grid(
            pady=30, padx=10, row=5,
            column=0, columnspan=2,
            sticky=S+N+E+W)
 
         
        self.__frame.pack(padx=5, pady=5, expand=True, fill=X)


    def set_controlador(self, controlador):
        self.__controlador = controlador


    def introducir_parametros(self):
        if self.__controlador != None:
            self.__controlador.guardar_parametros(
                self.get_jornada_laboral(), self.get_descanso(),
                self.get_velocidad(), self.get_ocupacion(),
                self.get_exito())

    
    def get_jornada_laboral(self):
        return self.__jornada_laboral.get_valor_selector()

    
    def get_descanso(self):
        return self.__descanso.get_valor_selector()


    def get_velocidad(self):
        return self.__velocidad.get_valor_selector()


    def get_ocupacion(self):
        return self.__ocupacion.get_valor_selector()

    
    def get_exito(self):
        return self.__exito.get_valor_selector()


class ParametroModelo():

    def __init__(self, frame, aspecto):

        # Configuración etiqueta
        texto_etiqueta = aspecto[0]; fila_etiqueta = aspecto[1]
        columna_etiqueta = aspecto[2]

        # Configuración selector
        inicio_selector = aspecto[3]; fin_selector = aspecto[4]
        incremento_selector = aspecto[5]; fila_selector = aspecto[6]
        columna_selector = aspecto[7] 


        # Atributo etiqueta
        self.__etiqueta = Label(frame, text=texto_etiqueta)
        self.__etiqueta.config(font=("Adobe Caslon Pro", 15, 'bold'))
        self.__etiqueta.grid(
            row=fila_etiqueta, column=columna_etiqueta, padx=5)
        
        # Atributo selector
        self.__selector = Spinbox(
            frame, from_=inicio_selector, to=fin_selector,
            increment=incremento_selector)

        self.__selector.config(
            fg='#333333', font=("Adobe Caslon Pro", 10, 'bold'),
            state='readonly')

        self.__selector.grid(
            row=fila_selector, column=columna_selector, pady=5, padx=5)

    
    def get_valor_selector(self):
        return float(self.__selector.get())