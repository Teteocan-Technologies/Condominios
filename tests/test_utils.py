import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import unittest
from unittest.mock import patch
from utils import solicitar_prioridad, solicitar_indice

class TestUtils(unittest.TestCase):
    @patch("builtins.input", side_effect=["1"])
    def test_solicitar_prioridad(self, mock_input):
        prioridad = solicitar_prioridad()
        self.assertEqual(prioridad, 1)

    @patch("builtins.input", side_effect=["3"])
    def test_solicitar_indice(self, mock_input):
        indice = solicitar_indice("Selecciona una tarea: ", 5)
        self.assertEqual(indice, 2)  # El índice es 0-based

if __name__ == "__main__":
    unittest.main()