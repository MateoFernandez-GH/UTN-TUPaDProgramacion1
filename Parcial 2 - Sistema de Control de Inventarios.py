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
    print("Carga de herramientas iniciales\n")
    # Si el inventario ya tiene elementos, indicar al usuario que use la opción 5
    if inventario:
        print("El inventario ya se encuentra inicializado - pase a la Opción n°5 para agregar nuevos productos.\n")
        return

    while True:
        try:
            cantidad = input("Ingrese la cantidad de herramientas a cargar: ")
            if not cantidad: 
                raise ValueError("Error: No ingresaste la cantidad de herramientas. Vuelva a intentarlo...\n")
            elif int(cantidad) < 0:
                raise ValueError("Error: La cantidad no puede ser negativa. Vuelva a intentarlo...\n")
            break
            
        except ValueError as e:
            print(f"{e}")
            continue
        except Exception as e:
            print(f"Error inesperado: {e}")
            continue

    for carga in range(int(cantidad)):
        # Validar y obtener un nombre válido
        while True:
            nombre_raw = input(f"Ingrese el nombre de la herramienta n°{carga+1}: ")
            nombre = normalizar_nombre(nombre_raw)
            if not nombre:
                print("Error: El nombre de la herramienta no puede estar vacío. Vuelva a intentarlo.\n")
                continue
            if buscar_herramienta(inventario, nombre):
                print("Error: Este producto ya se encuentra cargado en el inventario. Ingrese otro nombre.\n")
                continue
            break

        # Validar y obtener un stock válido
        while True:
            stock = input("Ingrese el stock inicial: ")
            if not stock:
                print("Error: No ingresaste la cantidad de herramientas. Vuelva a intentarlo.\n")
                continue
            try:
                stock = int(stock)
                if stock < 0:
                    print("Error: El stock inicial no puede ser negativo. Vuelva a intentarlo.\n")
                    continue
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido para el stock. Vuelva a intentarlo.\n")
                continue

        inventario.append({"herramienta": nombre, "cantidad": stock})
        print(f"La herramienta '{nombre}' ha sido agregada con {stock} unidades.\n")


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

    if inventario : 
        print("\nNo se encuentran articulos agotados por el momento...\n")
    for herramienta in inventario:
        if herramienta['cantidad'] == 0 :
            print(f"La herramienta '{herramienta['herramienta']}' se encuentra agotada. ( Stock : {herramienta['cantidad']})")


def carga_nueva(inventario): 
    print("\n==============================================")
    print("Alta de nuevo producto:\n")

    nombre = input("Ingrese el nombre de la herramienta a ingresar: ")
    nombre = normalizar_nombre(nombre)


    # Validar que la herramienta no exista ya en el inventario
    
        

    # Validar que el nombre no esté vacio, que la herramienta no exista y pedir stock
    try:
        if buscar_herramienta(inventario, nombre):
            raise ValueError ("Error: La herramienta indicada ya se encuentra en el inventario.\n")
        if not nombre :
            raise ValueError ("Error: El nombre de la herramienta no puede estar vacío.\n")
        
        stock = int(input("Ingrese el stock inicial: "))
        if stock < 0:
            raise ValueError ("Error: El stock no puede ser negativo.\n")

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



