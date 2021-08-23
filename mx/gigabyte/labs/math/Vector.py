"""Class Vector"""
import tkinter

import matplotlib.pyplot as plt

from mx.gigabyte.labs.math.gui.math_gui import PlanoCartesiano


class Vector:

    def __init__(self, vector: tuple):
        """Crea un vector desde el origen (0, 0) hacia la punta"""
        self.origen = (0, 0)
        self.punta = vector

    def __str__(self):
        """Imprime informacion relevante del vector"""
        o_x, o_y = self.origen
        p_x, p_y = self.punta
        return f"Vector con origen = ({o_y}, {o_y}) y con un punta = ({p_x}, {p_y})"

    def grafica(self):
        # puntos_x, puntos_y = Vector.extrae_puntos(self.origen, self.punta)
        # plt.figure(figsize=(20, 30))
        # plt.plot(puntos_x, puntos_y)
        # plt.show()
        plano_cartesiano = PlanoCartesiano()
        print(plano_cartesiano)
        plano_cartesiano.agregar_linea(self.origen, self.punta, arrow=tkinter.LAST, width=2)
        plano_cartesiano.grafica()


    @staticmethod
    def extrae_puntos(*vectores):
        """Extrae y crea una lista de 2 tuplas con base a una lista de vectores (x1, y1)...(xn, yn):
        :returns
            resultado[0] es una tupla con todos los puntos en X
            resultado[1] es una tupla con todos los puntos en y
        """
        puntos_x = []
        puntos_y = []
        for v in vectores:
            x, y = v
            puntos_x.append(x)
            puntos_y.append(y)
        return tuple(puntos_x), tuple(puntos_y)
