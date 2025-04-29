class Tarea:
    """Clase que representa una tarea."""

    def __init__(self, titulo: str, descripcion: str, prioridad: int, completada: bool = False):
        """
        Inicializa una nueva tarea.

        Args:
            titulo (str): Título de la tarea.
            descripcion (str): Descripción detallada de la tarea.
            prioridad (int): Prioridad de la tarea (1 = Alta, 2 = Media, 3 = Baja).
            completada (bool): Estado de la tarea (True si está completada, False si está pendiente).
        """
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = completada

    def __str__(self):
        """
        Representación en cadena de la tarea.

        Returns:
            str: Una cadena que describe la tarea.
        """
        estado = "✔ Completada" if self.completada else "Pendiente"
        prioridades = {1: "Alta", 2: "Media", 3: "Baja"}
        return f"[{prioridades.get(self.prioridad, 'Desconocida')}] {self.titulo}: {self.descripcion} ({estado})"