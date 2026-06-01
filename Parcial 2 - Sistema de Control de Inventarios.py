# Funciones auxiliares

def normalizar_nombre():
    pass

def buscar_herramienta():
    pass

# Funciones relativas a las opciones del menú

def carga_inicial():
    pass

def mostrar_inventario():
    pass

def consultar_stock():
    pass

# Funciones estructurales del Menú  

def mostrar_menu():
    pass

def ejecutar_menu(opcion, inventario):
    
    match opcion :
        case "1":
            carga_inicial()
        case "2":
            mostrar_inventario()
        case "3":
            consultar_stock()
        case "4":
            pass # Reporte de agotados
        case "5":
            pass # Alta de nuevo producto 
        case "6":
            pass # Modificación de stock - venta o ingreso
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



