"""Modulo que provee de clases y metodos para poder crear graficas"""
import tkinter


class PlanoCartesiano:
    """Clase que representa un plano cartesiano"""

    def __init__(self, altura=500, ancho=600):
        """Inicializamos el area de trabajo del plano cartesiano"""
        self.window = tkinter.Tk()
        self.altura = altura
        self.ancho = ancho
        self.canvas = tkinter.Canvas(self.window, height=altura, width=ancho)

        self.canvas.create_line(0, self.altura // 2, self.ancho, self.altura // 2, width=2, arrow=tkinter.BOTH)
        self.canvas.create_line(self.ancho // 2, 0, self.ancho // 2, self.altura , width=2, arrow=tkinter.BOTH)

        # self.agregar_linea(eje_y_punto_inicial, eje_y_punto_final, dash=(2, 2), arrow=tkinter.BOTH)

        self.__origen = (self.ancho // 2, self.altura // 2)

    def grafica(self):
        self.canvas.pack()
        self.window.mainloop()

    def __transforma_coordenada(self, punto):
        """Transforma el punto en base al nuevo origen"""
        return (punto[0] + self.__origen[0], punto[1] + self.__origen[1])

    def agregar_linea(self, punto_inicial, punto_final, **kwargs):
        """Agrega una line al plano cartesiano"""
        pi_x, pi_y = self.__transforma_coordenada(punto_inicial)
        pf_x, pf_y = self.__transforma_coordenada(punto_final)
        self.canvas.create_line(pi_x, pi_y, pf_x, pf_y, kwargs)

    @property
    def origen(self):
        return self.__origen

    def __str__(self):
        return f"Plano cartesiano con origen = {self.origen}"
