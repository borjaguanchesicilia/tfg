from src.controlador.librerias import *
from src.controlador.scroll import *
 
 
class Tabla:
    
    def __init__(self, master, tituloVentana, fichero, filas, columnas, alto, ancho):
        
        self.__master = master
        self.__fichero = fichero
 
        self.__frame = Frame(self.__master)
 

        self.__aspecto = Frame(self.__frame)
 
        self.__titulo = Label(self.__aspecto, text= tituloVentana)
        self.__titulo.config(font=("Adobe Caslon Pro", 30))
        self.__titulo.pack(padx = 5, pady = 5)
     
        self.__aspecto.pack(padx = 5, pady = 5)



        self.__botones = LabelFrame(self.__frame, text= 'Opciones')
 
        self.__botonGuardar = Button(self.__botones, text = "Guardar", command = self.guardar); self.__botonGuardar.pack(padx = 5, pady = 5, side = RIGHT)
        self.__botonCargar = Button(self.__botones, text = "Mostrar aviones", command = self.cargar); self.__botonCargar.pack(padx = 5, pady = 5, side = RIGHT)
        self.__botonLimpiar = Button(self.__botones, text = "Limpiar", command = self.limpiar); self.__botonLimpiar.pack(padx = 5, pady = 5, side = RIGHT)
         
        self.__botones.pack(padx = 5, pady = 5, side= TOP)
         
 
        self.__middle = ScrollableFrame(self.__frame, alto, ancho)

        self.__row = filas; self.__col = columnas
        self.__celdas = [[None for i in range(self.__col)] for j in range(self.__row)]

        for i in range(self.__row):
            for j in range(self.__col):
                if j == 2:
                    self.__celdas[i][j] = Entry(self.__middle.scrollable_frame, width = 20); self.__celdas[i][j].grid(row= i, column= j)
                else:
                    self.__celdas[i][j] = Entry(self.__middle.scrollable_frame, width = 10); self.__celdas[i][j].grid(row= i, column= j)
         
        self.__middle.pack(padx = 5, pady = 5)
 
         
        self.__frame.pack(padx = 5, pady = 5, expand = True, fill = X)
 
 
    def guardar(self):

        file = open("data.txt", "w")

        for i in range(self.__row):
            for j in range(self.__col):
                file.write(self.__celdas[i][j].get() + ";")
            file.write("\n")
 
        file.close()
 

    def cargar(self):

        self.limpiar()

        for i in range(self.__row):
            for j in range(self.__col):
                cabecera = self.__fichero.getCabecera(j)
                if i == 0:
                    self.__celdas[i][j].insert(0, cabecera)
                else:
                    self.__celdas[i][j].insert(0, self.__fichero.getElemento(cabecera, i))


    def limpiar(self):

        [self.__celdas[i][j].delete(0, 'end') for j in range(self.__col) for i in range(self.__row)]