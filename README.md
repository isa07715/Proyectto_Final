
# Agregar documentación

## Estructura

```
PROYECTO_FINAL/
    |-- data
    |   |-- task.json
    |-- src
    |   |-- cli.py
    |   |-- file_store.py
    |   |-- task_services.py
    |-- README.md
    |-- .gitignore
    |-- requirements.txt
    |-- main.py
```

## Crear entoro virtual

```bash
python -m venv .venv
```
## Activar el entorno virtual

````bash
.venv/Scripts/activate # Windows

source .venv/bin/activate # Linux Mac
````


## Configurar git

```bash
git config --global user.name "AGREGAR USUARIO GIT"
git config --global user.email "AGREGAR EMAIL GIT"
```

verificar configuración

```bash
git config --list
```

## Crear repositorio git

```bash
git init
```

## Crear archivo `.gitignore`

Crear en la raiz un archivo con el nombre `.gitignore` y agregar los nombres de los documentos que no desee hacer seguimiento.

## Enlace de repositorio

```bash
git remote add origin <url del repositorio>
```

Verificar enlace de repositorio

```bash
git remote -v
```
## Hacer commit

```bash
git commit -m "ESCRIBIR MENSAJE"
```

## Enlazar ramas

```bash
git branch -M main
```

## Hacer el push al repositorio remoto

```bash
git push -u origin main
```

# Agenda Académica Digital

## Integrantes del Equipo
- Isabella González Muñoz  
- Manuela Mesa Bedoya  

## Descripción del Problema
En el entorno académico, especialmente en el universitario, los estudiantes suelen enfrentar dificultades para organizar trabajos, exámenes, exposiciones y otras actividades importantes. Estas dificultades pueden deberse a la falta de herramientas simples para la gestión del tiempo, o a que muchos estudiantes trabajan o tienen otras responsabilidades además del estudio, lo que genera olvidos, entregas tardías o incompletas y, en consecuencia, un bajo desempeño académico.

Aunque existen aplicaciones de calendario y organización, muchas requieren conexión a internet, creación de cuentas o resultan demasiado complejas para quienes solo necesitan una solución básica. Por esto, se identificó la necesidad de un software sencillo, funcional desde la consola, que permita a los estudiantes gestionar sus actividades escolares de forma rápida, clara y sin complicaciones técnicas.

## Objetivo del Software
El objetivo principal de este software es brindar a los estudiantes una herramienta práctica y sencilla para gestionar sus actividades académicas, como tareas, exámenes y trabajos. La aplicación permitirá registrar información importante como:

- Título de la actividad
- Fecha de entrega
- Breve descripción

Todo esto a través de una interfaz por consola fácil de usar. Al centralizar esta información, se busca fomentar una mejor organización personal, reducir el riesgo de olvidar fechas importantes y mejorar la productividad y el rendimiento académico.

## Funcionalidades Principales
- Agregar tareas con título, fecha de entrega y descripción.
- Ver todas las tareas registradas.
- Eliminar tareas específicas.
- Interfaz por menú en consola fácil de usar.

## Lenguaje de Programación Elegido
Se utilizó **Python**, ya que es un lenguaje con sintaxis clara y legible, ideal para enfocarse en la lógica del programa sin complicaciones. Además, es ampliamente usado en entornos educativos por su facilidad de aprendizaje.

## Alcance del Proyecto
Este proyecto incluye:
- Registro de tareas en tiempo real durante la ejecución.
- Visualización y eliminación de tareas.
- Funcionamiento completo desde la consola.

Este proyecto **no incluye**:
- Interfaz gráfica.
- Notificaciones automáticas o alertas.
- Guardado permanente en archivo o base de datos.