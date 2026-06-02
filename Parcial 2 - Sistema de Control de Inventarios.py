# Funciones auxiliares

def normalizar_nombre(nombre):
    return nombre.strip().lower() 

def buscar_herramienta(inventario, nombre):
    nombre = normalizar_nombre(nombre)
    for herramienta in inventario:
        if herramienta["herramienta"] == nombre:
            return herramienta
    return None

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

    for carga in range(cantidad):
        nombre = normalizar_nombre(input(f"Ingrese el nombre de la herramienta n°{carga+1} : "))
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
    print("Inventario:\n")
    for herramienta in inventario:
        print(f"- {herramienta['herramienta']}: {herramienta['cantidad']} unidades\n")


def consultar_stock(inventario):
    print("\n==============================================")
    print("Consulta de stock\n")
    nombre = input("Ingrese el nombre de la herramienta a consultar: ")
    herramienta = buscar_herramienta(inventario, nombre)
    if herramienta:
        print(f"\nStock de {herramienta['herramienta']}: {herramienta['cantidad']} unidades\n")
    else:
        print(f"\nLa herramienta '{nombre}' no se encuentra en el inventario.\n") 

def agotados(inventario): 
    print("\n==============================================")
    print("Articulos agotados:\n")

    for herramienta in inventario:
        if herramienta['cantidad'] == 0 :
            print(f"La herramienta '{herramienta['herramienta']}' se encuentra agotada.")


def carga_nueva(inventario): 
    print("\n==============================================")
    print("Alta de nuevo producto:\n")

    nombre = input("Ingrese el nombre de la herramienta a ingresar: ")
    nombre = normalizar_nombre(nombre)

    # Validar que el nombre no esté vacío
    if not nombre:
        print("Error: El nombre de la herramienta no puede estar vacío.\n")
        return

    # Validar que la herramienta no exista ya en el inventario
    if buscar_herramienta(inventario, nombre):
        print(f"Error: La herramienta '{nombre}' ya se encuentra en el inventario.\n")
        return

    # Pedir stock
    try:
        stock = int(input("Ingrese el stock inicial: "))
        if stock < 0:
            print("Error: El stock no puede ser negativo.\n")
            return
    except ValueError:
        print("Error: Debe ingresar un número válido para el stock.\n")
        return
    except Exception as e:
        print(f"Error inesperado: {e}\n")
        return

    # Si todas las validaciones pasaron, agregar a inventario
    inventario.append({"herramienta": nombre, "cantidad": stock})
    print(f"La herramienta '{nombre}' ha sido agregada exitosamente con {stock} unidades.\n")




# Funciones estructurales del Menú  

def mostrar_menu():
    print("==============================================\n")
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
            consultar_stock(inventario)
        case "4":
            agotados(inventario)
        case "5":
            carga_nueva(inventario) 
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
    print("=============== PARCIAL N°2 ==================\n")
    print("Bienvenido al Sistema de Control de Inventarios\n")
    inventario = []

    while True : 
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if not ejecutar_menu(opcion, inventario):
            break



programa_principal()



