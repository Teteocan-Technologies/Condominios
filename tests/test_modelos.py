import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from gestor_tareas.modelos import Tarea

class TestTarea(unittest.TestCase):
    def test_crear_tarea(self):
        tarea = Tarea("Título", "Descripción", 1)
        self.assertEqual(tarea.titulo, "Título")
        self.assertEqual(tarea.descripcion, "Descripción")
        self.assertEqual(tarea.prioridad, 1)
        self.assertFalse(tarea.completada)

    def test_str_tarea(self):
        tarea = Tarea("Título", "Descripción", 1, completada=True)
        self.assertIn("✔ Completada", str(tarea))
        self.assertIn("[Alta]", str(tarea))

if __name__ == "__main__":
    unittest.main()