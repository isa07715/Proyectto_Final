
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