import json
from gestor_tareas.modelos import Tarea

class GestorArchivos:
    """Clase para manejar la lectura y escritura de tareas en formato JSON."""

    @staticmethod
    def cargar_tareas(ruta_archivo: str) -> list[Tarea]:
        """
        Carga las tareas desde un archivo JSON.
        Si el archivo no existe, retorna una lista vacía.
        Maneja errores de lectura y formato.

        Args:
            ruta_archivo (str): Ruta del archivo JSON donde se almacenan las tareas.

        Returns:
            list[Tarea]: Lista de objetos Tarea cargados desde el archivo.
        """
        try:
            # Intentar abrir el archivo para lectura
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)  # Cargar el contenido del archivo JSON
                # Convertir cada entrada del JSON en una instancia de Tarea
                return [Tarea(**tarea) for tarea in datos]
        except FileNotFoundError:
            # Si el archivo no existe, retorna una lista vacía
            print(f"Archivo no encontrado: {ruta_archivo}")
            return []
        except json.JSONDecodeError as e:
            # Manejo de errores de formato JSON
            print(f"Error al leer el archivo JSON {ruta_archivo}: {e}")
            return []
        except IOError as e:
            # Manejo de otros errores de E/S (por ejemplo, permisos insuficientes)
            print(f"Error al leer el archivo {ruta_archivo}: {e}")
            return []

    @staticmethod
    def guardar_tareas(ruta_archivo: str, tareas: list[Tarea]):
        """
        Guarda las tareas en un archivo JSON.
        Sobrescribe el archivo con las tareas actuales.
        Maneja errores de escritura.

        Args:
            ruta_archivo (str): Ruta del archivo JSON donde se almacenarán las tareas.
            tareas (list[Tarea]): Lista de objetos Tarea a guardar.
        """
        try:
            # Intentar abrir el archivo para escritura
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                # Convertir cada tarea en un diccionario y guardar en formato JSON
                json.dump([tarea.__dict__ for tarea in tareas], archivo, ensure_ascii=False, indent=4)
        except IOError as e:
            # Manejo de errores de escritura (por ejemplo, disco lleno o permisos insuficientes)
            print(f"Error al escribir en el archivo {ruta_archivo}: {e}")