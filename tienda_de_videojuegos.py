import csv
def agregar_videojuego():
    titulo = input("Titulo: ")
    plataforma = input("Plataforma: ")
    precio = input("Precio: ")
    existencias = input("Existencias")
    
    with open("videojuegos.csv", "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([titulo, plataforma, precio, existencias])


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
    elif opcion == "2":
        print("Buscar videojuego")
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
