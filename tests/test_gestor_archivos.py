import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from gestor_tareas.gestor_archivos import GestorArchivos
from gestor_tareas.modelos import Tarea

class TestGestorArchivos(unittest.TestCase):
    def setUp(self):
        self.archivo_prueba = "test_tareas.json"

    def tearDown(self):
        if os.path.exists(self.archivo_prueba):
            os.remove(self.archivo_prueba)

    def test_guardar_y_cargar_tareas(self):
        tareas = [
            Tarea("Tarea 1", "Descripción 1", 1),
            Tarea("Tarea 2", "Descripción 2", 2)
        ]
        GestorArchivos.guardar_tareas(self.archivo_prueba, tareas)
        tareas_cargadas = GestorArchivos.cargar_tareas(self.archivo_prueba)
        self.assertEqual(len(tareas_cargadas), 2)
        self.assertEqual(tareas_cargadas[0].titulo, "Tarea 1")
        self.assertEqual(tareas_cargadas[1].prioridad, 2)

if __name__ == "__main__":
    unittest.main()