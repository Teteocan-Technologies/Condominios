from gestor_tareas.gestor_tareas import GestorTareas
from utils import solicitar_prioridad, solicitar_indice

def main():
    # Inicializa el gestor de tareas con los archivos correspondientes
    gestor = GestorTareas("datos/tareas_pendientes.json", "datos/tareas_completadas.json")

    while True:
        print(
            "\nMenú de tareas:\n"
            "1. Agregar una tarea\n"
            "2. Mostrar tareas pendientes\n"
            "3. Editar una tarea\n"
            "4. Eliminar una tarea\n"
            "5. Completar una tarea\n"
            "6. Mostrar tareas completadas\n"
            "7. Salir"
        )
        opcion = input("Selecciona una opción: ").strip()

        match opcion:
            case "1":
                titulo = input("Ingresa el título de la tarea: ").strip()
                descripcion = input("Ingresa la descripción de la tarea: ").strip()
                prioridad = solicitar_prioridad()
                gestor.agregar_tarea(titulo, descripcion, prioridad)

            case "2":
                gestor.listar_tareas()

            case "3":
                gestor.listar_tareas()
                if gestor.tareas_pendientes:
                    indice = solicitar_indice("Ingresa el número de la tarea que deseas editar: ", len(gestor.tareas_pendientes))
                    titulo = input("Nuevo título (deja vacío para no cambiar): ").strip()
                    descripcion = input("Nueva descripción (deja vacío para no cambiar): ").strip()
                    prioridad = solicitar_prioridad()
                    gestor.editar_tarea(indice, titulo or None, descripcion or None, prioridad)

            case "4":
                gestor.listar_tareas()
                if gestor.tareas_pendientes:
                    indice = solicitar_indice("Ingresa el número de la tarea que deseas eliminar: ", len(gestor.tareas_pendientes))
                    gestor.eliminar_tarea(indice)

            case "5":
                gestor.listar_tareas()
                if gestor.tareas_pendientes:
                    indice = solicitar_indice("Ingresa el número de la tarea que deseas completar: ", len(gestor.tareas_pendientes))
                    gestor.completar_tarea(indice)

            case "6":
                gestor.listar_tareas(completadas=True)

            case "7":
                print("\nSaliendo del programa...")
                break

            case _:
                print("Opción ingresada no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()