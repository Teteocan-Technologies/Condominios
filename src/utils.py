def solicitar_prioridad() -> int:
    """
    Solicita al usuario una prioridad válida (1, 2 o 3).

    Returns:
        int: La prioridad ingresada por el usuario.
    """
    while True:
        try:
            prioridad = int(input("Ingresa la prioridad de la tarea (1 = Alta, 2 = Media, 3 = Baja): ").strip())
            if prioridad in [1, 2, 3]:
                return prioridad
            else:
                print("Por favor, ingresa un número válido (1, 2 o 3).")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")

def solicitar_indice(mensaje: str, total_tareas: int) -> int:
    """
    Solicita al usuario un índice válido para seleccionar una tarea.

    Args:
        mensaje (str): Mensaje que se mostrará al usuario.
        total_tareas (int): Número total de tareas disponibles.

    Returns:
        int: El índice ingresado por el usuario.
    """
    while True:
        try:
            indice = int(input(mensaje).strip()) - 1
            if 0 <= indice < total_tareas:
                return indice
            else:
                print(f"Por favor, ingresa un número entre 1 y {total_tareas}.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")