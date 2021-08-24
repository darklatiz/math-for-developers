"""Modulo que provee de clases y metodos para poder crear graficas"""
import tkinter

from mx.gigabyte.labs.math.Vector import Vector


class PlanoCartesiano:
    """Clase que representa un plano cartesiano"""

    def __init__(self, altura=500, ancho=600):
        """Inicializamos el area de trabajo del plano cartesiano"""
        self.window = tkinter.Tk()
        self.altura = altura
        self.ancho = ancho
        self.canvas = tkinter.Canvas(self.window, height=altura, width=ancho)

        self.canvas.create_line(0, self.altura // 2, self.ancho, self.altura // 2, width=2, arrow=tkinter.BOTH) # eje X
        self.canvas.create_line(self.ancho // 2, 0, self.ancho // 2, self.altura, width=2, arrow=tkinter.BOTH) # eje y

        # self.agregar_linea(eje_y_punto_inicial, eje_y_punto_final, dash=(2, 2), arrow=tkinter.BOTH)

        self.__origen = (self.ancho // 2, self.altura // 2)

    def grafica(self):
        self.canvas.pack()
        self.window.mainloop()

    def __transforma_coordenada(self, punto):
        """Transforma el punto en base al nuevo origen"""
        if punto[0] > 0 and punto[1] > 0:
            x_trasnformada = self.origen[0] + abs(punto[0])
            y_trasnformada = self.origen[1] - abs(punto[1])
        elif punto[0] < 0 and punto[1] > 0:
            x_trasnformada = self.origen[0] - abs(punto[0])
            y_trasnformada = self.origen[1] - abs(punto[1])
        elif punto[0] < 0 and punto[1] < 0:
            x_trasnformada = self.origen[0] - abs(punto[0])
            y_trasnformada = self.origen[1] + abs(punto[1])
        elif punto[0] > 0 and punto[1] < 0:
            x_trasnformada = self.origen[0] + abs(punto[0])
            y_trasnformada = self.origen[1] + abs(punto[1])
        else:
            x_trasnformada = self.origen[0]
            y_trasnformada = self.origen[1]

        return (x_trasnformada, y_trasnformada)

    def agregar_linea(self, punto_inicial: tuple, punto_final: tuple, **kwargs):
        """Agrega una line al plano cartesiano"""
        pi_x, pi_y = self.__transforma_coordenada(punto_inicial)
        pf_x, pf_y = self.__transforma_coordenada(punto_final)
        self.canvas.create_line(pi_x, pi_y, pf_x, pf_y, kwargs)

    def agregar_vector(self, vector: Vector, **kwargs):
        """Agrega el vector al plano cartesiano"""
        self.agregar_linea(vector.origen, vector.punta, **kwargs)

    @property
    def origen(self):
        return self.__origen

    def __str__(self):
        return f"Plano cartesiano con origen = {self.origen}"
