# Trabajaremos con una lista de tareas

tareas = []  # Creamos una lista de tareas vacía

# Inicio de la función agregar tarea
def agregar_tarea(tareas, tarea):
    tareas.append(tarea)
    print("Se ha agregado la tarea:", tarea)
    mostrar_tareas(tareas) 

# Fin de la función agregar tarea

# Inicio de la función eliminar tarea
def eliminar_tarea(tareas, tarea):
    if tarea in tareas:
        tareas.remove(tarea)
        print("Se ha eliminado la tarea:", tarea)
    else:
        print("La tarea:", tarea, "no se encuentra en la lista.")
    mostrar_tareas(tareas) 

# Fin de la función eliminar tarea

# Inicio de la función buscar tarea
def buscar_tarea(tareas, tarea):
    if tarea in tareas:
        print("La tarea:", tarea, "se encuentra en la lista.")
    else:
        print("La tarea:", tarea, "no está en la lista.")

# Fin de la función buscar tarea

# Inicio de la función ordenar tareas
def ordenar_tareas(tareas):
    tareas.sort()
    print("La lista de tareas ordenada es:")
    mostrar_tareas(tareas)  

# Fin de la función ordenar tareas

# Inicio de la función mostrar tareas
def mostrar_tareas(tareas):
    print("La lista actual de tareas es:", tareas)

# Fin de la función mostrar tareas

# Programa principal
agregar_tarea(tareas, "Lavar la ropa")
agregar_tarea(tareas, "Comprar alimentos")
agregar_tarea(tareas, "Estudiar Python")
buscar_tarea(tareas, "Comprar alimentos")
buscar_tarea(tareas, "Leer libro")
eliminar_tarea(tareas, "Comprar alimentos")
eliminar_tarea(tareas, "Cocinar")
ordenar_tareas(tareas)
