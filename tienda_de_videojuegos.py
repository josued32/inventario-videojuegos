import os
import csv

def agregar_videojuego():
    print("\n--- Agregar Videojuego ---")
    titulo = input("Título: ")
    plataforma = input("Plataforma: ")
    precio = input("Precio: ")
    existencias = input("Existencias: ") # Añadidos dos puntos y espacio
    
    # Verificamos si el archivo ya existe antes de abrirlo
    nombre_archivo = "videojuegos.csv"
    archivo_existe = os.path.exists(nombre_archivo)
    
    # Abrimos el archivo en modo append ('a')
    with open(nombre_archivo, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        
        # Si el archivo NO existe, escribimos la cabecera primero
        if not archivo_existe:
            escritor.writerow(["Titulo", "Plataforma", "Precio", "Existencias"])
            
        # Escribimos los datos ingresados por el usuario
        escritor.writerow([titulo, plataforma, precio, existencias])
        
    print("¡Videojuego guardado en el archivo exitosamente!")

def mostrar_catalogo():
    print("\n--- Catálogo de Videojuegos ---")
    nombre_archivo = "videojuegos.csv"
    
    # Verificamos si el archivo existe antes de intentar leerlo
    if not os.path.exists(nombre_archivo):
        print("No hay videojuegos en el catálogo.")
        return
    
    with open(nombre_archivo, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        encabezados = next(lector, None)  # Leemos la primera fila como encabezados
        
        if encabezados:
            print(f"{encabezados[0]:<30} {encabezados[1]:<15} {encabezados[2]:<10} {encabezados[3]:<10}")
            print("-" * 70)
        
        for fila in lector:
            print(f"{fila[0]:<30} {fila[1]:<15} {fila[2]:<10} {fila[3]:<10}")

def buscar_videojuego():
    print("\n--- Buscar Videojuego ---")
    nombre_archivo = "videojuegos.csv"
    
    # Verificamos si el archivo existe antes de buscar
    if not os.path.exists(nombre_archivo):
        print("No hay un catálogo registrado para realizar búsquedas.")
        return

    juego_buscado = input("Introduce el título del videojuego a buscar: ").strip().lower()
    coincidencias = []

    with open(nombre_archivo, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        encabezados = next(lector, None)
        
        for fila in lector:
            if juego_buscado in fila[0].lower():
                coincidencias.append(fila)

        if coincidencias:
            print(f"\nSe encontraron {len(coincidencias)} resultado(s):")
            if encabezados:
                print(f"{encabezados[0]:<30} {encabezados[1]:<15} {encabezados[2]:<10} {encabezados[3]:<10}")
                print("-" * 70)
            for fila in coincidencias:
                print(f"{fila[0]:<30} {fila[1]:<15} {fila[2]:<10} {fila[3]:<10}")
        else:
            print(f"No se encontró ningún videojuego que coincida con '{termino_busqueda}'.")

while True:
    print("=========================")
    print("    TIENDA DE VIDEOJUEGOS")
    print("=========================")
    print("1. Mostrar catálogo")
    print("2. Buscar videojuego")
    print("3. Agregar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")
    print("=========================")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("Mostrar catálogo")
        mostrar_catalogo()
    elif opcion == "2":
        print("Buscar videojuego")
        buscar_videojuego()
    elif opcion == "3":
        print("Agregar videojuego")
        agregar_videojuego()
    elif opcion == "4":
        print("Eliminar videojuego")
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida")
