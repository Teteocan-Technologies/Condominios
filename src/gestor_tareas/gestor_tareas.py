from gestor_tareas.modelos import Tarea
from gestor_tareas.gestor_archivos import GestorArchivos

class GestorTareas:
    """Clase para gestionar las tareas pendientes y completadas."""

    def __init__(self, archivo_pendientes: str, archivo_completadas: str):
        """
        Inicializa el gestor de tareas con los archivos correspondientes.

        Args:
            archivo_pendientes (str): Ruta del archivo JSON para las tareas pendientes.
            archivo_completadas (str): Ruta del archivo JSON para las tareas completadas.
        """
        self.archivo_pendientes = archivo_pendientes
        self.archivo_completadas = archivo_completadas

        # Cargar tareas pendientes y completadas desde los archivos
        self.tareas_pendientes = self._cargar_tareas(archivo_pendientes)
        self.tareas_completadas = self._cargar_tareas(archivo_completadas)

    def _cargar_tareas(self, archivo: str) -> list[Tarea]:
        """
        Carga las tareas desde un archivo JSON.

        Args:
            archivo (str): Ruta del archivo JSON.

        Returns:
            list[Tarea]: Lista de objetos Tarea cargados desde el archivo.
        """
        try:
            return GestorArchivos.cargar_tareas(archivo)
        except Exception as e:
            print(f"Error al cargar tareas desde {archivo}: {e}")
            return []

    def _guardar_tareas(self, archivo: str, tareas: list[Tarea]):
        """
        Guarda las tareas en un archivo JSON.

        Args:
            archivo (str): Ruta del archivo JSON.
            tareas (list[Tarea]): Lista de objetos Tarea a guardar.
        """
        try:
            GestorArchivos.guardar_tareas(archivo, tareas)
        except Exception as e:
            print(f"Error al guardar tareas en {archivo}: {e}")

    def agregar_tarea(self, titulo: str, descripcion: str, prioridad: int):
        """
        Agrega una nueva tarea pendiente.

        Args:
            titulo (str): Título de la tarea.
            descripcion (str): Descripción de la tarea.
            prioridad (int): Prioridad de la tarea (1 = Alta, 2 = Media, 3 = Baja).
        """
        tarea = Tarea(titulo, descripcion, prioridad)
        self.tareas_pendientes.append(tarea)
        self._guardar_tareas(self.archivo_pendientes, self.tareas_pendientes)
        print("\nTarea agregada exitosamente.")

    def listar_tareas(self, completadas: bool = False):
        """
        Lista las tareas pendientes o completadas, ordenadas por prioridad.

        Args:
            completadas (bool): Si es True, lista las tareas completadas; de lo contrario, las pendientes.
        """
        tareas = self.tareas_completadas if completadas else self.tareas_pendientes
        if not tareas:
            print("No hay tareas." if not completadas else "No hay tareas completadas.")
        else:
            tipo = "completadas" if completadas else "pendientes"
            print(f"\nTus tareas {tipo} ({len(tareas)} en total) son:")

            # Ordenar las tareas por prioridad (1 = Alta, 2 = Media, 3 = Baja)
            tareas_ordenadas = sorted(tareas, key=lambda t: t.prioridad)
            for i, tarea in enumerate(tareas_ordenadas, 1):
                print(f"{i}. {tarea}")

    def obtener_tarea(self, indice: int, lista: list[Tarea]) -> Tarea:
        """
        Obtiene una tarea de la lista si el índice es válido.

        Args:
            indice (int): Índice de la tarea en la lista.
            lista (list[Tarea]): Lista de tareas.

        Returns:
            Tarea: La tarea correspondiente al índice.

        Raises:
            IndexError: Si el índice no es válido.
        """
        if 0 <= indice < len(lista):
            return lista[indice]
        else:
            raise IndexError("Número de tarea no válido.")

    def editar_tarea(self, indice: int, titulo: str = None, descripcion: str = None, prioridad: int = None):
        """
        Edita una tarea pendiente.

        Args:
            indice (int): Índice de la tarea a editar.
            titulo (str): Nuevo título de la tarea (opcional).
            descripcion (str): Nueva descripción de la tarea (opcional).
            prioridad (int): Nueva prioridad de la tarea (opcional).
        """
        try:
            tarea = self.obtener_tarea(indice, self.tareas_pendientes)
            if titulo:
                tarea.titulo = titulo
            if descripcion:
                tarea.descripcion = descripcion
            if prioridad:
                tarea.prioridad = prioridad
            self._guardar_tareas(self.archivo_pendientes, self.tareas_pendientes)
            print("\nTarea editada exitosamente.")
        except IndexError as e:
            print(e)
        except (ValueError, TypeError):
            print("El índice debe ser un número entero válido.")

    def eliminar_tarea(self, indice: int):
        """
        Elimina una tarea pendiente.

        Args:
            indice (int): Índice de la tarea a eliminar.
        """
        try:
            tarea_eliminada = self.tareas_pendientes.pop(indice)
            self._guardar_tareas(self.archivo_pendientes, self.tareas_pendientes)
            print(f"\nTarea '{tarea_eliminada.titulo}' eliminada exitosamente.")
        except IndexError:
            print("Número de tarea no válido.")
        except (ValueError, TypeError):
            print("El índice debe ser un número entero válido.")

    def completar_tarea(self, indice: int):
        """
        Marca una tarea como completada.

        Args:
            indice (int): Índice de la tarea a completar.
        """
        try:
            tarea_completada = self.tareas_pendientes.pop(indice)
            tarea_completada.completada = True
            self.tareas_completadas.append(tarea_completada)
            self._guardar_tareas(self.archivo_pendientes, self.tareas_pendientes)
            self._guardar_tareas(self.archivo_completadas, self.tareas_completadas)
            print(f"\nTarea '{tarea_completada.titulo}' marcada como completada.")
        except IndexError:
            print("Número de tarea no válido.")
        except (ValueError, TypeError):
            print("El índice debe ser un número entero válido.")