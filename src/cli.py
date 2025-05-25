from src.task_services import agregar_tarea, ver_tareas, eliminar_tarea, marcar_tarea_terminada, mostrar_calendario



def ejecutar():

    while True:
        print("AGENDA ACADÉMICA")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Ver calendario con tareas")
        print("5. Marcar tarea ")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            eliminar_tarea()
        elif opcion == "4":
            mostrar_calendario()
        elif opcion == "5":
            marcar_tarea_terminada()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
