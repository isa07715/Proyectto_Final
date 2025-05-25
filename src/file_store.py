import json
import os

ARCHIVO_TAREAS = "data/tasks.json"

def cargar_desde_archivo():
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def guardar_en_archivo(tareas): 
    carpeta = os.path.dirname(ARCHIVO_TAREAS)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=4)

