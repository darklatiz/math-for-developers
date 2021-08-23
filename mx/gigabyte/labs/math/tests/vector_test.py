"""Modulo de pruebas unitarias para la clase Vector"""
import unittest

from mx.gigabyte.labs.math.Vector import Vector


class VectorTest(unittest.TestCase):

    @classmethod
    def set_up(cls) -> None:
        """Metodo que sirve para definir ciertas variables que seran usadas en todos los escenarios de pruebas"""
        pass

    def test_vector_creacion(self):
        v1 = Vector((2, 1))
        self.assertIsNotNone(v1)
        v1.grafica()
        print(v1)

