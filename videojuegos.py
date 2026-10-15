import csv
import os

inventario = {}
def cargar_datos_desde_csv():
    nombre_archivo = "videojuegos.csv"
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                titulo = fila['Titulo']
                inventario[titulo] = {
                    'plataforma': fila['Plataforma'],
                    'precio': float(fila['Precio']),       
                    'existencias': int(fila['Existencias'])
                }                        
    else:
        print("El archivo CSV todavía no tiene datos")

def menu():
    print("=========================")
    print("    TIENDA DE VIDEOJUEGOS")
    print("=========================")
    print("1. Mostrar catálogo")
    print("2. Buscar videojuego")
    print("3. Agregar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")
    print("=========================")
    return input("Selecciona una opción: ")

def mostrar_catalogo():
    print("\n--- Catálogo de Videojuegos ---")
    if not inventario:
        print("No hay videojuegos en el catálogo.")
        return
    print(f"{'Titulo':<30} {'Plataforma':<15} {'Precio':<10} {'Existencias':<10}")
    print("-" * 70)
    for titulo, datos in inventario.items():
        print(f"{titulo:<30} {datos['plataforma']:<15} {datos['precio']:<10.2f} {datos['existencias']:<10}")

def agregar_videojuego():
    titulo = input("Ingrese el título del videojuego: ")
    plataforma = input("Ingrese la plataforma: ")
    precio = float(input("Ingrese el precio: "))
    existencias = int(input("Ingrese la cantidad de existencias: "))
    
    # Guardamos los datos en el inventario
    inventario[titulo] = {
        'plataforma': plataforma,
        'precio': precio,
        'existencias': existencias
    }
    
    # Guardamos los datos en el archivo CSV
    guardar_en_csv(titulo, plataforma, precio, existencias)

def guardar_en_csv(titulo, plataforma, precio, existencias):
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

cargar_datos_desde_csv()

while True:     
    opcion = menu()
    if opcion == "1":
        print("Mostrar catálogo")
        mostrar_catalogo()
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