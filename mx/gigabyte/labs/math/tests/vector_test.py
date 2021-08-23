"""Modulo de pruebas unitarias para la clase Vector"""
import tkinter
import unittest

from mx.gigabyte.labs.math.Vector import Vector
from mx.gigabyte.labs.math.gui.math_gui import PlanoCartesiano


class VectorTest(unittest.TestCase):

    @classmethod
    def set_up(cls) -> None:
        """Metodo que sirve para definir ciertas variables que seran usadas en todos los escenarios de pruebas"""
        pass

    def test_vector_creacion(self):
        v1 = Vector((69, 80))
        self.assertIsNotNone(v1)
        print(v1)

    def test_grafica_vectores(self):
        v1 = Vector.from_xy(34, 60)
        v2 = Vector.from_xy(-34, 60)
        v3 = Vector.from_xy(34, -60)
        v4 = Vector.from_xy(-34, -60)
        self.assertIsNotNone(v1)
        plano_cartesiano = PlanoCartesiano()
        print(plano_cartesiano)
        plano_cartesiano.agregar_vector(v1, arrow=tkinter.LAST, width=2)
        plano_cartesiano.agregar_vector(v2, arrow=tkinter.LAST, width=2, fill="blue")
        plano_cartesiano.agregar_vector(v3, arrow=tkinter.LAST, width=2, fill="green")
        plano_cartesiano.agregar_vector(v4, arrow=tkinter.LAST, width=2, fill="red")
        plano_cartesiano.grafica()

