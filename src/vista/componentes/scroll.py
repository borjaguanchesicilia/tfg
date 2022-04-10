from src.controlador.librerias import *


class ScrollBar(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.__canvas = Canvas(self)
        self.__scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.__canvas.yview)
        self.__frame_scroll = ttk.Frame(self.__canvas)

        self.__frame_scroll.bind(
            "<Configure>",
            lambda e: self.__canvas.configure(scrollregion=self.__canvas.bbox("all")),
        )

        self.__canvas.create_window((0, 0), window=self.__frame_scroll, anchor="nw")

        self.__canvas.configure(yscrollcommand=self.__scrollbar.set)

        self.__canvas.pack(side="left", fill="both")

        self.__scrollbar.pack(side="right", fill="y")


    def get_frame_scroll(self):
        return self.__frame_scroll