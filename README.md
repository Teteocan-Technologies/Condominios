# Gestor de Tareas

## Descripción funcional
El **Gestor de Tareas** es una aplicación basada en consola que permite a los usuarios gestionar sus tareas de manera eficiente. Las tareas se almacenan en formato JSON y tienen los siguientes atributos:
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
   ```
   git clone https://github.com/tu_usuario/gestor_tareas.git
   ```

2. **Navega al directorio del proyecto:**
   ```
   cd gestor_tareas
   ```

3. **Instala las dependencias:**
   Asegúrate de tener Python 3.10 o superior instalado. Luego, ejecuta:
   ```
   pip install -r requirements.txt
   ```

---

## Uso

1. **Ejecuta el archivo principal `main.py`:**
   ```
   python src/main.py
   ```

2. **Sigue las instrucciones en pantalla para:**
   - Crear una nueva tarea.
   - Listar tareas pendientes o completadas.
   - Editar una tarea existente.
   - Eliminar una tarea.
   - Marcar una tarea como completada.
   - Salir de la aplicación.

---

## Validaciones

- **Prioridad:** Solo se aceptan valores numéricos entre 1 (Alta), 2 (Media) y 3 (Baja).
- **Datos obligatorios:** El título y la descripción de la tarea no pueden estar vacíos.
- **Índices válidos:** Al seleccionar una tarea para editar, eliminar o completar, el índice debe estar dentro del rango de tareas disponibles.

---

## Ejemplo de Uso

### Crear una tarea
```
Menú de tareas de estudiante:
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
Menú de tareas de estudiante:
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
Menú de tareas de estudiante:
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

## Pruebas

Este proyecto incluye pruebas unitarias para garantizar el correcto funcionamiento de cada componente. Las pruebas están ubicadas en la carpeta `tests/`.

### Ejecutar todas las pruebas:
Desde el directorio raíz del proyecto, ejecuta:
```
python -m unittest discover tests
```

---

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request. Asegúrate de incluir pruebas para cualquier funcionalidad nueva.

---

## Licencia

Este proyecto está bajo la Licencia MIT.

---

## Créditos

Este proyecto fue desarrollado por:
- **Nombre del desarrollador:** Jorge Alejandro Chacón Zárate
- **Contacto:** jorgechaconzarate@gmail.com



