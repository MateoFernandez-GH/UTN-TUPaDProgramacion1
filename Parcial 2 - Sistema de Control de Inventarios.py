# ====FUNCIONES AUXILIARES======================================================================================================================================================

def normalizar_nombre(nombre):
    # Normaliza el nombre de la herramienta (elimina espacios en blanco y convierte a minúsculas)
    return nombre.strip().lower() 

# Función para buscar una herramienta en el inventario por su nombre (ya normalizado)
def buscar_herramienta(inventario, nombre): 
    nombre = normalizar_nombre(nombre) 
    for herramienta in inventario:
        # La comparación se hace con el nombre normalizado de la herramienta en el inventario
        if herramienta["herramienta"] == nombre: 
            # Si se encuentra la herramienta, se retorna el diccionario completo de esa herramienta (con su nombre y cantidad)
            return herramienta
    # Si no se encuentra la herramienta, se retorna None (lo que significaria que no existe en el inventario...)
    return None

# Función para redirigir al usuario hacia la función correspondiente según la respuesta del usuario : venta o ingreso de stock.
def pregunta(inventario): 
    print("\n===============================================")
    print("Actualización de stock (venta / ingreso)\n")
    
    # Antes de preguntar al usuario, verificamos que el inventario no esté vacío. Si lo está, indicamos al usuario que debe cargar productos primero.
    if not inventario: 
        print("Aun no tienes un inventario cargado. Selecciona la Opción n°1 para agregar los primeros productos")
        return
    
    print("¿ Necesitas vender mercadería, o agregar nuevo stock ? (Escribe 'vender' o 'agregar'): \n")
    
    # El bucle se repetirá hasta que el usuario ingrese una respuesta válida ('vender' o 'agregar'). Si la respuesta es válida, se llamará a la función 
    # correspondiente y se romperá el bucle. Si la respuesta no es válida, se mostrará un mensaje de error y se volverá a preguntar.
    while True:
        respuesta = normalizar_nombre(input("- "))

        match respuesta : 
            case "vender": 
                vender(inventario)
                break  # Los break se utilizan para salir de este bucle, evitando que se vuelva a preguntar después de ejecutar la función correspondiente.
            case "agregar": 
                agregar_stock(inventario)
                break
            case _:
                print("Opción no válida. Escribe 'vender' o 'agregar'.\n")
                continue
            


# ====FUNCIONES PRINCIPALES DEL PROGRAMA=========================================================================================================================================

# Es la funcion que se encarga de la carga inicial del inventario, permitiendo al usuario ingresar una cantidad de herramientas y sus respectivos stocks.
def carga_inicial(inventario):
    print("\n==============================================")
    print("Carga de herramientas iniciales\n")
    # Si el inventario ya tiene elementos, indicar al usuario que use la opción 5
    if inventario:
        print("El inventario ya se encuentra inicializado - pase a la Opción n°5 para agregar nuevos productos.\n")
        return

    while True:
        # Bloque try-except para validar que el usuario ingrese una cantidad válida de herramientas a cargar. Se verifica que la entrada no esté vacía 
        # y que sea un número entero no negativo.
        try:
            cantidad = input("Ingrese la cantidad de herramientas a cargar: ")
            if not cantidad: 
                raise ValueError("Error: No ingresaste la cantidad de herramientas. Vuelva a intentarlo...\n")
            elif int(cantidad) < 0:
                raise ValueError("Error: La cantidad no puede ser negativa. Vuelva a intentarlo...\n")
            break
            
        # Se capturan errores específicos de validación (ValueError) y se muestra un mensaje de error al usuario, permitiéndole volver a intentar. Asimismo 
        # se captura cualquier otro error inesperado.
        except ValueError as e:
            print(f"{e}")
            continue
        except Exception as e:
            print(f"Error inesperado: {e}")
            continue

    for carga in range(int(cantidad)):
        # Validar y obtener un nombre válido
        while True:
            # Solicitamos al usuario que ingrese el nombre de la herramienta, luego normalizamos el nombre para eliminar espacios y convertirlo a minúsculas.
            nombre = input(f"Ingrese el nombre de la herramienta n°{carga+1}: ")
            nombre = normalizar_nombre(nombre)
            # Validamos que el nombre no esté vacío y que no exista ya en el inventario. Si alguna de estas condiciones no se cumple, se muestra un mensaje de error 
            # y se vuelve a solicitar el nombre.
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
            # Validamos que el stock no esté vacío, que sea un número entero y que no sea negativo. Caso contrario, se muestran mensajes de error y se vuelve a solicitar 
            # el stock.
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
        # Si todas las validaciones 'pasaron', se agrega la herramienta al inventario como un diccionario con su nombre y cantidad.
        inventario.append({"herramienta": nombre, "cantidad": stock})
        print(f"La herramienta '{nombre}' ha sido agregada con {stock} unidades.\n")

# Función para mostrar el inventario actual. Si el inventario está vacío, se muestra un mensaje indicando que no hay productos cargados.
def mostrar_inventario(inventario):
    print("\n==============================================")
    print("Inventario:\n")

    if not inventario: 
        print("Aun no tienes un inventario cargado. Selecciona la Opción n°1 para agregar los primeros productos")
        return
    # Bucle for que recorre cada herramienta en el inventario y muestra su nombre y cantidad. Se formatea el print para que sea claro y legible.
    for herramienta in inventario:
        print(f"- {herramienta['herramienta']}: {herramienta['cantidad']} unidades\n")

# Funcion que consulta el stock de una herramienta específica. Se solicita al usuario que ingrese el nombre de la herramienta a consultar, se busca en el inventario 
# y se muestra su cantidad actual. 
def consultar_stock(inventario):
    print("\n==============================================")
    print("Consulta de stock\n")

    if not inventario: 
        print("Aun no tienes un inventario cargado. Selecciona la Opción n°1 para agregar los primeros productos")
        return
    
    nombre = input("Ingrese el nombre de la herramienta a consultar: ")

    herramienta = buscar_herramienta(inventario, nombre) # Reutilizamos esta funcion para la busqueda de la herramienta, y retornarla en caso de exito. 

    # Si la herramienta existe, se muestra su stock actual. Si no existe, se muestra un mensaje indicando que la herramienta no se encuentra en el inventario.
    if herramienta:
        print(f"\nStock de {herramienta['herramienta']}: {herramienta['cantidad']} unidades\n")
    else:
        print(f"\nLa herramienta '{nombre}' no se encuentra en el inventario.\n") 

# Funcion que muestra un reporte de aquelos productos agotados (con stock 0). Si el inventario está vacío, se muestra un mensaje indicando que no hay productos cargados. 
# Si no hay productos agotados, se muestra un mensaje indicando que todos los productos tienen stock disponible.
def agotados(inventario): 
    print("\n==============================================")
    print("Articulos agotados:\n")

    if not inventario: 
        print("Aun no tienes un inventario cargado. Selecciona la Opción n°1 para agregar los primeros productos")
        return
    
    no_agotado = False # Utilizamos una variable bandera para controlar si se encontraron o no productos agotados. Si al finalizar el bucle esta variable sigue siendo False, 
    # significa que no se encontraron productos agotados y se muestra el mensaje correspondiente.
    for herramienta in inventario:
        if herramienta['cantidad'] == 0 :
            print(f"La herramienta '{herramienta['herramienta']}' se encuentra agotada. ( Stock : {herramienta['cantidad']})\n")
            return herramienta['herramienta'] 
        else :
            if not no_agotado:
                print("No se encuentran productos agotados por el momento / Todos los productos tienen stock disponible.\n")
                no_agotado = True # Actualizacion de la bandera booleana, para evitar que se muestre el mensaje cada vez que el bucle itera sobre un producto con 
                # stock disponible.

# Función para agregar un nuevo producto al inventario. Se solicita al usuario que ingrese el nombre de la herramienta a agregar y su stock inicial.
def carga_nueva(inventario): 
    print("\n==============================================")
    print("Alta de nuevo producto:\n")


    if not inventario: 
        print("El inventario aun no se encuentra inicializado. Selecciona la Opción n°1 para agregar los primeros productos")
        return
    
    while True :
        nombre = input("Ingrese el nombre de la herramienta a ingresar: ")
        nombre = normalizar_nombre(nombre)

        # Bloque try/except utilizado para validar que el nombre no esté vacio, que la herramienta ya exista y pedir stock
        try:
            if buscar_herramienta(inventario, nombre):
                raise ValueError ("""Error: La herramienta indicada ya se encuentra en el inventario.
Para actualizar sus cantidades, pase a la Opcion n°6.""")
            if not nombre :
                raise ValueError ("Error: El nombre de la herramienta no puede estar vacío.\n")
            break
        except ValueError as e:
            print(f"{e}\n")
            continue
        except Exception as e:
            print(f"Error inesperado: {e}")
            continue 

    
    while True : 
        try: 
            stock = input("Ingrese el stock inicial: ").strip() # Utilizamos strip aqui para eliminar espacios en blanco al inicio o al final de la entrada del usuario.
            stock = int(stock)
            # si el stock es negativo, se lanza un error y se muestra un mensaje indicando que el stock no puede ser negativo. Si el stock es válido, se rompe el bucle 
            # y se continúa con la carga del nuevo producto.
            if stock < 0:
                print("Error: El stock no puede ser negativo.\n")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número válido para el stock.\n")
            continue
        except Exception as e:
            print(f"Error inesperado: {e}\n")
            return

    # Si todas las validaciones pasaron, agrega el nuevo producto al inventario
    inventario.append({"herramienta": nombre, "cantidad": stock})
    print(f"La herramienta '{nombre}' ha sido agregada exitosamente con {stock} unidades.\n")

# Funcion para realizar la sustraccion de stock desde el inventario en caso de venta, o la suma de stock en caso de ingreso. Se solicita al usuario que ingrese el nombre 
# de la herramienta a vender o agregar stock, se busca en el inventario y se actualiza su cantidad según corresponda.
def vender(inventario):
    print("\n===============================================")
    print("Venta de artículos:\n")
    
    if not inventario:
        print("El inventario está vacío. No hay productos para vender.\n")
        return
    
    # Pedir nombre de herramienta a vender
    while True: 
        try : 
            seleccion = normalizar_nombre(input("Ingrese el nombre de la herramienta a vender: "))

            # Usamos la funcion de busqueda para verificar que la herramienta exista en el inventario, y ademas para retornar el diccionario completo de la herramienta, lo 
            # que nos permitira acceder a su cantidad actual y realizar la sustraccion correspondiente. 
            herramienta = buscar_herramienta(inventario, seleccion)
            if not herramienta:
                raise ValueError("Error: La herramienta seleccionada no se encuentra en el inventario.\n")
            # Si la cantidad de la herramienta es 0, se lanza un error indicando que el artículo se encuentra sin stock (agotado), y se vuelve a solicitar el nombre 
            # de la herramienta a vender.
            if herramienta['cantidad'] == 0:
                raise ValueError("Error: El artículo seleccionado se encuentra sin stock (agotado).\n")
            break
        except ValueError as e:
            print(f"{e}")
            continue
        except Exception as e:
            print(f"Error inesperado: {e}\n")
            continue

    # Pedir cantidad a vender
    while True:
        # En este bloque try/except se valida que la cantidad ingresada sea un número entero válido y mayor a 0. Si la cantidad es válida, se realiza la sustracción del stock. 
        try : 
            cantidad = int(input("Ingrese la cantidad a vender: "))
            if cantidad <= 0:
                print("\nError: La cantidad a vender debe ser mayor a 0. Intente nuevamente.\n")
                continue
            
            # Realizamos la sustracción verificando que la cantidad no supere el stock actual. Si la cantidad a vender es mayor al stock actual, se muestra una advertencia.
            stock_actual = herramienta['cantidad']
            
            if cantidad > stock_actual:
                print(f"Advertencia: La cantidad a vender ({cantidad}) supera el stock actual ({stock_actual}). No se puede realizar la venta.\n")
                continue
            else:
                herramienta['cantidad'] -= cantidad
                print(f"Venta realizada. Se vendieron {cantidad} unidades.")
                print(f"\nStock actual de '{herramienta['herramienta']}': {herramienta['cantidad']} unidades.\n")
                break

        except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.\n")
            continue
        except Exception as e:
            print(f"Error inesperado: {e}\n")
            continue

def agregar_stock(inventario): 
    print("\n===============================================")
    print("Agregar stock al inventario :\n")

    if not inventario:
        print("El inventario no se ha creado aún. No hay productos para agregar.\n")
        return
    
    # Pedir el nombre de la herramienta a agregar 
    while True:
        try : 
            nombre = input("Indica el nombre del articulo al cual agregar stock : ")

            herramienta = buscar_herramienta(inventario, nombre)
            if not herramienta: 
                raise ValueError("El nombre ingresado no se corresponde con uno en el inventario.\n")
            break

        except ValueError as e : 
            print(f"{e}")
            continue
        except Exception as e:
            print(f"Error inesperado: {e}\n")
            continue

    # Pedimos la cantidad a agregar, validando que sea un número entero válido y no negativo. Si la cantidad es válida, se realiza la suma al stock actual de la herramienta.
    while True: 
        try : 
            cantidad = input("Indica la cantidad de productos a ingresar para actualizar el stock : ").strip()
            cantidad = int(cantidad)
            if cantidad < 0 : 
                print("Error: No puedes ingresar un numero negativo.\n")
                continue
            stock = herramienta['cantidad'] + cantidad 
            break
        except ValueError : 
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.\n")
            continue
        except Exception as e:
            print(f"Error inesperado: {e}\n")
            return
    
    print(f"""\nA la herramienta '{herramienta['herramienta']}' se le han agregado exitosamente {cantidad} unidades.
Stock Total : {stock}""")

# ====FUNCOINES ESTRUCTURALES DEL MENU===========================================================================================================================================

# Funcion que muestra las opciones del menú al usuario. Se llama en cada iteración del bucle principal para que el usuario pueda seleccionar una opción. 
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


# Función que ejecuta la opción seleccionada por el usuario. Se utiliza un bloque match-case para llamar a la función correspondiente según la opción ingresada. 
# Si la opción es válida, se ejecuta la función. Si la opción es "7", se muestra un mensaje de despedida y se retorna False para indicar que el programa debe finalizar. 
# Si la opción no es válida, se muestra un mensaje de error y se retorna True para continuar el programa.
def ejecutar_menu(opcion, inventario):
    
    match opcion.strip() :
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
            pregunta(inventario)
        case "7":
            print("Saliendo del programa. ¡Hasta luego!\n")
            # Retorna falso para indicar que el programa debe finalizar.
            return False  
        case _:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
    # Retorna verdadero para continuar el programa, con cualquier opción excepto la de salir.
    return True  

# Funcion principal del programa y su llamada...

def programa_principal():
    print("=============== PARCIAL N°2 ==================\n")
    print("Bienvenido al Sistema de Control de Inventarios\n")
    inventario = []

    while True : 
        # En cada iteración del bucle, se muestra el menú al usuario, se solicita una opción y se ejecuta la función correspondiente. Si el usuario selecciona la opción 
        # de salir, el programa finalizará.
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        continuar = ejecutar_menu(opcion, inventario)
        if not continuar:
            break


# Llamada a la función principal para iniciar el programa.
programa_principal()



