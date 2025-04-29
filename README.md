# Gestor de tareas

## Descripción funcional
El **Gestor de tareas** es una aplicación basada en consola que permite a los usuarios gestionar sus tareas de manera eficiente. Las tareas se almacenan en formato JSON y tienen los siguientes atributos:
- **Título**: Breve descripción de la tarea.
- **Descripción**: Detalles adicionales de la tarea.
- **Prioridad**: Nivel de importancia (1 = Alta, 2 = Media, 3 = Baja).
- **Estado**: Indica si la tarea está completada o pendiente.

### Funcionalidades principales:
- Agregar nuevas tareas con título, descripción y prioridad.
- Listar tareas pendientes y completadas, ordenadas por prioridad.
- Editar tareas existentes.
- Eliminar tareas.
- Marcar tareas como completadas.
- Almacenamiento persistente en archivos JSON.

---

## Instalación

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/jorgechacon559/Proyecto_individual.git
   ```

2. **Navega al directorio del proyecto:**
   ```bash
   cd gestor_tareas
   ```

3. **Instala las dependencias:**
   Asegúrate de tener Python 3.10 o superior instalado. 
   ```bash
   python --version
   ```

   Luego, ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación:**
   ```bash
   python src/main.py
   ```

---

## Estructura del proyecto

```
gestor_tareas/
├── datos/
│   ├── tareas_pendientes.json    # Archivo JSON para almacenar tareas pendientes
│   ├── tareas_completadas.json   # Archivo JSON para almacenar tareas completadas
├── src/
│   ├── main.py                   # Menú principal de la aplicación
│   ├── utils.py                  # Funciones auxiliares para validaciones
│   ├── gestor_tareas/
│   │   ├── __init__.py           # Inicializador del paquete
│   │   ├── gestor_archivos.py    # Funciones para manejar archivos JSON
│   │   ├── gestor_tareas.py      # Lógica de negocio para manejar tareas
│   │   ├── modelos.py            # Clase Tarea
├── tests/
│   ├── test_gestor_tareas.py     # Pruebas unitarias para gestor_tareas.py
│   ├── test_gestor_archivos.py   # Pruebas unitarias para gestor_archivos.py
│   ├── test_utils.py             # Pruebas unitarias para utils.py
│   ├── test_modelos.py           # Pruebas unitarias para modelos.py
├── README.md                     # Documentación del proyecto
├── requirements.txt              # Dependencias del proyecto
```

---

## Validaciones

- **Prioridad:** Solo se aceptan valores numéricos entre 1 (Alta), 2 (Media) y 3 (Baja).
- **Datos obligatorios:** El título y la descripción de la tarea no pueden estar vacíos.
- **Índices válidos:** Al seleccionar una tarea para editar, eliminar o completar, el índice debe estar dentro del rango de tareas disponibles.

### Ejemplo de validación fallida
- Si intentas ingresar una prioridad no válida, el programa mostrará un mensaje como este:
```
Ingresa la prioridad de la tarea (1 = Alta, 2 = Media, 3 = Baja): 5 Prioridad no válida. Por favor, ingresa un número entre 1 y 3.
```

---

## Ejemplo de uso

### Crear una tarea
```
Menú de tareas:
1. Agregar una tarea
2. Mostrar tareas pendientes
3. Editar una tarea
4. Eliminar una tarea
5. Completar una tarea
6. Mostrar tareas completadas
7. Salir
Selecciona una opción: 1
Ingresa el título de la tarea: Estudiar para el examen
Ingresa la descripción de la tarea: Repasar los temas de matemáticas y física
Ingresa la prioridad de la tarea (1 = Alta, 2 = Media, 3 = Baja): 1
Tarea agregada exitosamente.
```

### Listar tareas pendientes
```
Menú de tareas:
1. Agregar una tarea
2. Mostrar tareas pendientes
3. Editar una tarea
4. Eliminar una tarea
5. Completar una tarea
6. Mostrar tareas completadas
7. Salir
Selecciona una opción: 2

Tus tareas pendientes (1 en total) son:
1. [Alta] Estudiar para el examen: Repasar los temas de matemáticas y física (Pendiente)
```

### Completar una tarea
```
Menú de tareas:
1. Agregar una tarea
2. Mostrar tareas pendientes
3. Editar una tarea
4. Eliminar una tarea
5. Completar una tarea
6. Mostrar tareas completadas
7. Salir
Selecciona una opción: 5

Tus tareas pendientes (1 en total) son:
1. [Alta] Estudiar para el examen: Repasar los temas de matemáticas y física (Pendiente)
Ingresa el número de la tarea que deseas completar: 1
Tarea 'Estudiar para el examen' marcada como completada.
```

---

### Ejemplo de una tarea en JSON
```json
{
    "titulo": "Estudiar para el examen",
    "descripcion": "Repasar los temas de matemáticas y física",
    "prioridad": 1,
    "completada": false
}
```
---

## Pruebas

Este proyecto incluye pruebas unitarias para garantizar el correcto funcionamiento de cada componente. Las pruebas están ubicadas en la carpeta `tests/`.

Las pruebas unitarias verifican el correcto funcionamiento de los siguientes componentes:
- Gestión de tareas (agregar, editar, eliminar, completar).
- Validaciones de entrada del usuario.
- Manejo de archivos JSON.

### Ejecutar todas las pruebas:
Desde el directorio raíz del proyecto, ejecuta:
```
python -m unittest discover tests
```

---

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request, y asegúrate de incluir pruebas para cualquier funcionalidad nueva. Puedes consultar la guía oficial de GitHub para abrir un pull request aquí:
[Cómo abrir un pull request](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

---

## Licencia

Este proyecto está bajo la Licencia MIT.

---

## Créditos

Este proyecto fue desarrollado por:
- **Nombre del desarrollador:** Jorge Alejandro Chacón Zárate
- **Contacto:** jorgechaconzarate@gmail.com
- **GitHub:** [jorgechacon559](https://github.com/jorgechacon559)
