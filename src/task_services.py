from src.file_store import cargar_desde_archivo, guardar_en_archivo
from collections import defaultdict
from datetime import datetime
import calendar


def cargar_tareas():
    tareas = cargar_desde_archivo()
    return tareas

def guardar_tareas(tareas):
    guardar_en_archivo(tareas)

def agregar_tarea():
    titulo=input("titulo: ")
    descripcion= input("Ingrese descripciòn: ")
    fecha= input("Ingrese Fecha:dd/mm/aaaa ")
    terminada=False
    tareas= cargar_tareas()
    ids= [t["id"] for t in tareas]
    id=max(ids)+1

    tarea = {
          
        "id":id,
        "titulo":titulo,
        "fecha": fecha,
        "descripcion": descripcion,
        "terminada": terminada
    }
    tareas.append(tarea)
    guardar_tareas(tareas)
    print(f"Tarea '{tarea}' agregada.")

def ver_tareas():
    tareas=cargar_tareas()
    if not tareas:
        print("No hay tareas.")
        return
    print("Tareas actuales:")
    print(f"id\t titulo\t\t\t fecha\t\t\t terminada")
    for tarea in tareas: 
        id= tarea["id"]
        titulo= tarea["titulo"] 
        fecha= tarea["fecha"]
        terminada= tarea["terminada"]
        terminada="si" if terminada else "no"
        print(f"{id}\t {titulo}\t\t\t {fecha}\t\t\t {terminada}")

def eliminar_tarea():
    tareas=cargar_tareas()
    ids= [t["id"] for t in tareas]

    ver_tareas()
    if not tareas:
        return
    try:
        indice = int(input("Ingresa el número de la tarea a eliminar: "))
        if indice in ids: 
            tarea_eliminada=[ tarea for tarea in tareas if tarea["id"]==indice]
            tarea_eliminada=tarea_eliminada[0]

            tareas=[ tarea for tarea in tareas if tarea["id"]!=indice]

            
            guardar_tareas(tareas)
            print(f"Tarea '{tarea_eliminada}' eliminada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def marcar_tarea_terminada():
    ver_tareas()
    tareas = cargar_tareas()
    ids = [t["id"] for t in tareas]

    try:
        indice = int(input("Ingresa el id de la tarea: "))
    except ValueError:
        print("Por favor ingresa un número válido.")
        return

    if indice in ids:
        for tarea in tareas:
            if tarea["id"] == indice:
                if tarea.get("terminada", False):
                    print(f"La tarea con ID {indice} ya está marcada como terminada.")
                else:
                    tarea["terminada"] = True
                    guardar_tareas(tareas)
                    print(f"Tarea con ID {indice} marcada como terminada.")
                break
    else:
        print("ID no encontrado.")

def mostrar_calendario():
    tareas = cargar_tareas()
    if not tareas:
        print("No hay tareas registradas.")
        return

    hoy = datetime.today()

    año_input = input(f"Ingrese el año (Enter para {hoy.year}): ").strip()
    if año_input == "":
        año = hoy.year
    else:
        if not año_input.isdigit() or int(año_input) < 1:
            print("Año inválido.")
            return
        año = int(año_input)

    mes_input = input(f"Ingrese el mes (1-12):  ").strip()
    if mes_input == "":
        mes = hoy.month
    else:
        if not mes_input.isdigit() or not (1 <= int(mes_input) <= 12):
            print("Mes inválido.")
            return
        mes = int(mes_input)

    tareas_por_dia = defaultdict(list)
    for tarea in tareas:
        fecha_str = tarea.get("fecha")
        if fecha_str:
            for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
                try:
                    dt = datetime.strptime(fecha_str, fmt)
                    if dt.year == año and dt.month == mes:
                        tareas_por_dia[dt.day].append(tarea)
                    break
                except ValueError:
                    continue

    cal = calendar.monthcalendar(año, mes)

    print(f"\nCalendario {calendar.month_name[mes]} {año}\n")
    print("Lu  Ma  Mi  Ju  Vi  Sá  Do")

    for semana in cal:
        linea = ""
        for dia in semana:
            if dia == 0:
                linea += "    "
            else:
                marcador = "*" if dia in tareas_por_dia else " "
                linea += f"{dia:2d}{marcador}  "
        print(linea)

    print("\nTareas del mes:")
    for dia in sorted(tareas_por_dia):
        print(f"\n{dia}/{mes}/{año}:")
        for tarea in tareas_por_dia[dia]:
            estado = "terminada" if tarea.get("terminada") else "Sin terminar"
            print(f"  {estado} [{tarea['id']}] {tarea['titulo']} - {tarea['descripcion']}")

