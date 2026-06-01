# Funciones auxiliares

def normalizar_nombre(nombre):
    return nombre.strip().lower() 

def buscar_herramienta():
    pass

# Funciones relativas a las opciones del menú

def carga_inicial(inventario):
    print("\n==============================================")
    print("Carga de herramientas iniciales")

    try:
        cantidad = int(input("Ingrese la cantidad de herramientas a cargar: "))
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
    except ValueError as e:
        print(f"Error: {e}")
        return
    except Exception as e:
        print(f"Error inesperado: {e}")
        return

    for _ in range(cantidad):
        nombre = normalizar_nombre(input("Ingrese el nombre de la herramienta: "))
        try:
            stock = int(input("Ingrese el stock inicial: "))
            if stock < 0:
                raise ValueError("El stock inicial no puede ser negativo.")
        except ValueError as e:
            print(f"Error: {e}")
            return
        inventario.append({"herramienta": nombre, "cantidad": stock})


def mostrar_inventario(inventario):
    print("\n==============================================")
    print("Inventario:")
    for herramienta in inventario:
        print(f"- {herramienta['herramienta']}: {herramienta['cantidad']} unidades\n")


def consultar_stock():
    pass

# Funciones estructurales del Menú  

def mostrar_menu():
    print("\n==============================================")
    print("Menú de opciones:")
    print("1. Carga de herramientas iniciales")
    print("2. Visualización de inventario")
    print("3. Consulta de stock")
    print("4. Reporte de agotados")
    print("5. Alta de nuevo producto")
    print("6. Actualizacion de stock (venta / ingreso)")
    print("7. Salir\n")

def ejecutar_menu(opcion, inventario):
    
    match opcion :
        case "1":
            carga_inicial(inventario)
        case "2":
            mostrar_inventario(inventario)
        case "3":
            consultar_stock()
        case "4":
            pass # Reporte de agotados
        case "5":
            pass # Alta de nuevo producto 
        case "6":
            pass # Actualización de stock - venta o ingreso
        case "7":
            print("Saliendo del programa. ¡Hasta luego!")
            # Retorna falso para indicar que el programa debe finalizar.
            return False  
        case _:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
    # Retorna verdadero para continuar el programa, con cualquier opción excepto la de salir.
    return True  

# Funcion principal del programa y su llamada.

def programa_principal():
    
    print("\n==============================================")
    print("Bienvenido al Sistema de Control de Inventarios\n")
    inventario = []

    while True : 
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if not ejecutar_menu(opcion, inventario):
            break



programa_principal()



