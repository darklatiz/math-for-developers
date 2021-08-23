"""Modulo que provee de clases y metodos para poder crear graficas"""
import tkinter


class PlanoCartesiano:
    """Clase que representa un plano cartesiano"""

    def __init__(self, altura=250, ancho=300):
        """Inicializamos el area de trabajo del plano cartesiano"""
        self.window = tkinter.Tk()
        self.altura = altura
        self.ancho = ancho
        self.canvas = tkinter.Canvas(self.window, height=altura, width=ancho)
        eje_x_punto_inicial = (0, self.altura // 2)
        eje_x_punto_final = (self.ancho, self.altura // 2)

        eje_y_punto_inicial = (self.ancho // 2, 0)
        eje_y_punto_final = (self.ancho // 2, self.altura)

        self.agregar_linea(eje_x_punto_inicial, eje_x_punto_final)
        self.agregar_linea(eje_y_punto_inicial, eje_y_punto_final)

        self.__origen = (self.ancho // 2, self.altura // 2)

    def grafica(self):
        self.canvas.pack()
        self.window.mainloop()

    def agregar_linea(self, punto_inicial, punto_final):
        """Agrega una line al plano cartesiano"""
        pi_x, pi_y = punto_inicial
        pf_x, pf_y = punto_final
        self.canvas.create_line(pi_x, pi_y, pf_x, pf_y, dash=(2, 2))

    @property
    def origen(self):
        return self.__origen

    def __str__(self):
        return f"Plano cartesiano con origen = {self.origen}"

