"""Class Vector"""
import tkinter

import matplotlib.pyplot as plt


class Vector:

    def __init__(self, vector: tuple):
        """Crea un vector desde el origen (0, 0) hacia la punta"""
        self.origen = (0, 0)
        self.punta = vector

    @classmethod
    def from_xy(cls, x, y):
        """Crea un vector desde el origen (0, 0) hacia la punta"""
        return cls((x, y))

    def __str__(self):
        """Imprime informacion relevante del vector"""
        o_x, o_y = self.origen
        p_x, p_y = self.punta
        return f"Vector con origen = ({o_y}, {o_y}) y con un punta = ({p_x}, {p_y})"

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
