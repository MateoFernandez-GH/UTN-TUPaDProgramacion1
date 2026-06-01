while True:  

    
    ejercicios = int(input("Hola ! Indica con un numero del 1 al 5 el ejercicio que quiera evaluar : "))      #Solicitamos al docente que ingrese el digito correspondiente al ejercicio a evaluar.
    while not ejercicios.is_integer() :             # Evaluamos si el dato ingresado es en efecto un digito u otro tipo de caracter.
        print("No has ingresado un numero de ejercicio valido.") 
        ejercicios = int(input("Indica con un numero del 1 al 5 el ejercicio que quiera evaluar :"))  # Volvemos a solicitarlo en caso negativo.


    match ejercicios:  # Estructura match case para vincular el digito ingresado por el docente, con la ejecucion de su correspondiente ejercicio. 

        case 1 : # Ejericio 1 
            while True :
                # Solicitudes de nombre de ususairo con mecanismo de validacion.
                nombre=input("Ingrese su nombre : ")                    
                while not nombre: 
                    print(f"Error. Ingrese un nombre valido.")
                    nombre=input()

                while not nombre.isalpha(): 
                    print(f"Error. Ingrese un nombre valido.")
                    nombre=input()

                # Se le solicita al usuario que ingrese la cantidad de productos.
                cantidad=input("Ingrese la cantidad de productos comprados : ")

                # Mecansimo de validacion para que los datos ingresados no sean ni caracteres alfabeticos o simbolos, o un 0.
                while not cantidad.isdigit() or cantidad == "0": 
                    print("Has ingresado una cantidad incorrecta. Vuelve a ingresar la cantidad de productos.")
                    cantidad=input()

                # Se nombran las variables acumulativas, que luego nos van a proporcionar los datos a mostrar en los resultados.
                tot_con_descuentos = 0
                tot_sin_descuentos = 0
                ahorro = 0 
                texto_x_productos = ""    # Utilizamos un "string acumulador" ya que no vimos aun las listas. 
                for producto in range (1,int(cantidad)+1):  # Ciclo for que itera solicitudes de precios e informacion sobre descuentos por cada uno de ellos.
                    print(f"Ingrese el precio del producto n° {producto} :")
                    precio=input()


                    while not precio.isdigit():
                        print(f"ERROR. Ingrese un precio valido para el producto n° {producto} :")
                        precio=input()                
                    print(f"Indicar si el producto n° {producto} tiene descuento : (s/n)")
                    descuento=input()
                    while (not descuento.lower() == "s" )and (not descuento.lower() == "n"):
                        print(f"ERROR : Volver a indicar si el producto n° {producto} tiene descuento : (s/n)")
                        descuento=input()

                    # Ajustamos los tipos de datos para que puedan ser evaluadas en todas las operaciones necesarias, en pos de reflejarlas en los resultados.
                    precio_entero = float(precio)
                    tot_sin_descuentos += precio_entero
                    tot_con_descuentos = tot_sin_descuentos - float(tot_con_descuentos * 0.10) 
                    ahorro = float(tot_sin_descuentos - tot_con_descuentos) 

                
                    

                    
                    # Se agrega cadena de texto formateada para el final de cada iteracion/producto, para que muestre la informacion ingresada guardada en variable string 'texto_x_productos'.    
                    texto_x_productos += (f"Producto n° {producto} - Precio: {precio} Descuento (S/N) : {descuento})\n") 
            
                cantidad_entero = int(cantidad)
                promedioxproducto = (tot_con_descuentos / cantidad_entero)
                
                # Resultados de terminal.    
                print(f"""
Cliente : {nombre}
Cantidad de productos : {cantidad}
{texto_x_productos}

Total sin descuentos : ${tot_sin_descuentos:.2f}
Total con descuentos : ${tot_con_descuentos:.2f}
Ahorro : ${ahorro:.2f}
Promedio por producto : ${promedioxproducto:.2f}

                """)
                break
            False # Volvemos falsa toda la estructura del ejercicio para que, una vez el usuario llegado a su punto final, cierre sin mas y el archivo pase a preguntar por el siguiente ejercicio.  


        case 2 : 
            USUARIO_CORRECTO = "alumno"  # Constante del ejercicio
            clave_correcta = "python123" # Variable que puede ser cambiada 
            ejercicio2 = True
            while ejercicio2 is True : 


                menu = False 

                # Solicitar credenciales 
                for intentos_us in range (3): 
                    usuario = input(f"intento {intentos_us+1}/3 -  Usuario : ") # Mostramos el numero de intento validado por cada tipo de credencial
                    if usuario == USUARIO_CORRECTO : 
                        break # Si el nombre de usuario es el correcto, salir del loop y proseguir con la solicitud de password.
                    else : 
                        print ("Credencial invalida.")
                        if intentos_us == 2 : 
                            print("Cuenta bloqueada\n")
                            ejercicio2 = False # Cambiamos el estado del ejercicio a Falso, para simular un 'bloqueo' de sistema en cuanto las credenciales sean erroneas hasta la ultima iteracion. 

                if not ejercicio2 is False : # Si el ejercicio sigue valido ( usuario valido ) / Proseguir.
                    for intentos_pass in range (3) :  # Mismo procedimiento de validacion con password.
                        print(f"intento {intentos_pass+1}/3 -  Clave : ")
                        contraseña = input()
                        if contraseña == clave_correcta and usuario == USUARIO_CORRECTO:
                            menu = True
                            print("Acceso concedido\n")

                            break
                        else : 
                            print ("Credencial invalida.")
                            if intentos_pass == 2 : 
                                print("Cuenta bloqueada\n")
                                ejercicio2 = False 

                # Mostrar Menu en caso de autenticacion 
                
                while menu is True : 

                    print("""\n MENU PRINCIPAL \n
1) Estado  2) Cambiar Clave  3) Mensaje  4) Salir """)
                    eleccion_menu = input("Opcion : ")

                    while not eleccion_menu.isdigit(): # Mecanismo de validacion para evitar que el dato autenticado solamente pueda ser un digito. 
                        print("Error. Ingrese un numero valido.")
                        eleccion_menu = input("Opcion : ")

                    match eleccion_menu : # Utilizacion de match case para la seleccion de opciones dentro del menu de la cuenta.
                        case "1" : 
                            print ("Estado : Inscripto")
                        case "2" : 
                            print ("Ingresa una nueva clave. Debe tener minimo 6 caracteres. ")
                            nueva_clave = input("Nueva clave : ")
                            if len(nueva_clave) < 6 : 
                                print ("Error: mínimo 6 caracteres.")
                            else : 
                                clave_correcta = nueva_clave
                                print ("La clave se actualizó correctamente.")
                        case "3" : 
                            print ("\nEl éxito consiste en ir de fracaso en fracaso sin perder el entusiasmo.")
                        case "4" : 
                            break 
                        case _ : 
                            print ("Error: opción fuera de rango")
                print("\n")


                
        case 3 : 
            ejercicio3 = True

            while ejercicio3 is True : 
                
                # Se solicitan los datos del operador del ejercicio, validando su tipo de dato. 
                nombre_operador = input("Nombre del operador : ")
                while not nombre_operador.isalpha() : 
                    print("El nombre ingresado es incorrecto. Vuelve a intentarlo.")
                    nombre_operador = input("Nombre del operador : ")
                
                # asignar variables para cada turno del dia Lunes y sus espacios vacios para asignar su turno
                lunes1 = ""
                lunes2 = ""
                lunes3 = ""
                lunes4 = ""
                # asignar variables para cada turno del dia Martes y sus espacios vacios para asignar su turno
                martes1 = "" 
                martes2 = ""
                martes3 = ""


                menu = True
                while menu is True : # Seteamos el valor de esta variable en un bucle while como True, para que pueda devolvernos las opciones luego de cada opcion tomada.
                    print("""\n MENU PRINCIPAL \n
1) Reservar Turno  
2) Cancelar turno 
3) Ver agenda del dia
4) Ver resumen general
5) Cerrar Sistema """)
                    seleccion = input("\nSeleccona una opcion : ")

                    match seleccion : 
                        case "1" : # Reserva de turnos 
                            print("Elege un día en el cual reservar un turno (1=Lunes, 2=Martes)")
                            dia_reserva = input()
                            while not dia_reserva.isdigit(): 
                                print("El valor ingresado no es valido.")
                                print("Elege un día en el cual reservar un turno (1=Lunes, 2=Martes)")
                                dia_reserva = input()

                            paciente = input("Ingrese el nombre del paciente : ")
                            while not paciente.isalpha() : 
                                print("El valor ingresado no es valido.")
                                paciente = input("Ingrese el nombre del paciente : ")

                            paciente_repetido = False # Variable booleana para evaluar si el paciente ya tiene un turno asignado en el dia que desea reservar.
                            turno = None # Inicializar turno para detectar si se asignó correctamente
                            if dia_reserva == "1": # Evaluaremos si por cada dia de reserva, ese paciente ya tiene su turno asignado, y en caso contrario, asignarle el turno.
                                
                                # Estructura if-elif-else para determinar si un paciente ya poseiaa o no un turno asignado, por cada dia / 1-Lunes, 2-Martes. 
                                if paciente == lunes1 : 
                                    print("Este paciente ya tiene su turno agendado")
                                    paciente_repetido = True
                                elif not lunes1 :
                                    lunes1 = paciente
                                    turno = "1"
                                elif paciente == lunes2 : 
                                    print("Este paciente ya tiene su turno agendado")
                                    paciente_repetido = True
                                elif not lunes2 : 
                                    lunes2 = paciente
                                    turno = "2"
                                elif paciente == lunes3:
                                    print("Este paciente ya tiene su turno agendado")
                                    paciente_repetido = True
                                elif not lunes3 :
                                    lunes3 = paciente 
                                    turno = "3"
                                elif paciente == lunes4:
                                    print("Este paciente ya tiene su turno agendado")
                                    paciente_repetido = True
                                elif not lunes4 :
                                    lunes4 = paciente 
                                    turno = "4"

                            elif dia_reserva == "2":
                                if paciente == martes1 : 
                                    print("Este paciente ya tiene su turno agendado")
                                    paciente_repetido = True
                                elif not martes1 :
                                    martes1 = paciente
                                    turno = "1"
                                elif paciente == martes2 : 
                                    print("Este paciente ya tiene su turno agendado")
                                    paciente_repetido = True
                                elif not martes2 : 
                                    martes2 = paciente
                                    turno = "2"
                                elif paciente == martes3:
                                    print("Este paciente ya tiene su turno agendado")
                                    paciente_repetido = True
                                elif not martes3 :
                                    martes3 = paciente 
                                    turno = "3"

                            # Asignamos los digitos correspondientes a cada dia a un string conteniendo el texto del dia, para ser utilizado en prints/inputs. 
                            if dia_reserva == "1" : 
                                dia = "Lunes" 
                            elif dia_reserva == "2": 
                                dia = "Martes"  
                            
                            # Verificar si se asignó un turno correctamente
                            if turno is not None and not paciente_repetido :
                                print(f"\nSe ha asignado el turno n° {turno} para el paciente {paciente}, el dia {dia}")
                            elif turno is None:
                                print(f"\nError: No hay turnos disponibles para el día {dia}. Todos los turnos están ocupados.")

                        case "2" : # Cancelacion de Turnos
                            cacelacion = input("Indica el dia del que necesitas cancelar turno (1=Lunes, 2=Martes) : ") # Solicita al operador seleccionar el dia del turno a cancelar.
                            paciente = input("Ingrese el nombre del paciente : ") # Solicita al operador seleccionar el nombre del paciente que cancela el turno.
                            while not paciente.isalpha() : 
                                print("El valor ingresado no es valido.")
                                paciente = input("Ingrese el nombre del paciente : ")

                            if dia_reserva == "1": # Evaluaremos si por cada dia de reserva, existe turno asignado a ese paciente, y en caso afirmativo, cancelaremos el turno.
                                if paciente == lunes1 : 
                                    lunes1 = "" 
                                    print(f"\nSe ha cancelado el turno del paciente {paciente} del dia Lunes.")
                                elif paciente == lunes2 : 
                                    lunes2 = ""
                                    print(f"\nSe ha cancelado el turno del paciente {paciente} del dia Lunes.")
                                elif paciente == lunes3 : 
                                    lunes3 = ""
                                    print(f"\nSe ha cancelado el turno del paciente {paciente} del dia Lunes.")
                                elif paciente == lunes4 : 
                                    lunes4 = ""
                                    print(f"\nSe ha cancelado el turno del paciente {paciente} del dia Lunes.")

                            elif dia_reserva == "2": 
                                if paciente == martes1 : 
                                    martes1 = ""
                                    print(f"\nSe ha cancelado el turno del paciente {paciente} del dia Martes.")
                                elif paciente == martes2 : 
                                    martes2 = ""
                                    print(f"\nSe ha cancelado el turno del paciente {paciente} del dia Martes.")
                                elif paciente == martes3 :
                                    martes3 = "" 
                                    print(f"\nSe ha cancelado el turno del paciente {paciente} del dia Martes.")

                        case "3" : # Ver agenda del dia 
                            print("Elige el dia para ver su agenda (1=Lunes, 2=Martes) : ")
                            dia_reserva = input("Ingrese el numero del dia : ")
                            while not dia_reserva.isdigit() : 
                                print("El valor ingresado no es valido.")
                                dia_reserva = input("Ingrese el numero del dia : ")
                            
                            while dia_reserva.isdigit() : 
                                if dia_reserva == "1" : 

                                    print("Dia 1 (Lunes) :")
                                    if lunes1 == "":
                                        print("Turno 1 : vacio ")
                                    else : 
                                        print(f"Turno 1 : {lunes1}")

                                    if lunes2 == "":
                                        print("Turno 2 : vacio ")
                                    else : 
                                        print(f"Turno 2 : {lunes2}")

                                    if lunes3 == "":
                                        print("Turno 3 : vacio ")
                                    else : 
                                        print(f"Turno 3 : {lunes3}")

                                    if lunes4 == "":
                                        print("Turno 4 : vacio ")
                                    else : 
                                        print(f"Turno 4 : {lunes4}")
                                    break
                            
                                elif dia_reserva == "2" :
                                    print("\nDia 2 (Martes) :")
                                    if martes1 == "":
                                        print("Turno 1 : vacio ")
                                    else : 
                                        print(f"Turno 1 : {martes1}")

                                    if martes2 == "":
                                        print("Turno 2 : vacio ")
                                    else : 
                                        print(f"Turno 2 : {martes2}")

                                    if martes3 == "":
                                        print("Turno 3 : vacio ")
                                    else : 
                                        print(f"Turno 3 : {martes3}")
                                    break
                                else : 
                                    print("\nEl valor ingresado no es valido.")
                                    break 

                        case "4": # Resumen general de turnos
                            print("RESUMEN GENERAL DE TURNOS\n")

                            sum_turnolunes = 0 
                            sum_turnomartes = 0 

                            if lunes1 == "":
                                print("Turno 1 del dia lunes : Disponible ")
                            else : 
                                print("Turno 1 del dia lunes : Ocupado ")
                                sum_turnolunes += 1

                            if lunes2 == "":
                                print("Turno 2 del dia lunes : Disponible ")
                            else : 
                                print("Turno 2 del dia lunes : Ocupado ")
                                sum_turnolunes += 1

                            if lunes3 == "":
                                print("Turno 3 del dia lunes : Disponible ")
                            else : 
                                print("Turno 3 del dia lunes : Ocupado ")
                                sum_turnolunes += 1

                            if lunes4 == "":
                                print("Turno 4 del dia lunes : Disponible ")
                            else : 
                                print("Turno 4 del dia lunes : Ocupado ")
                                sum_turnolunes += 1

                            if martes1 == "":
                                print("Turno 1 del dia martes : Disponible ")
                            else : 
                                print("Turno 1 del dia martes : Ocupado ")
                                sum_turnomartes += 1

                            if martes2 == "":
                                print("Turno 2 del dia martes : Disponible ")
                            else : 
                                print("Turno 2 del dia martes : Ocupado ")
                                sum_turnomartes += 1

                            if martes3 == "":
                                print("Turno 3 del dia martes : Disponible ")
                            else : 
                                print("Turno 3 del dia martes : Ocupado ")
                                sum_turnomartes += 1


                            if sum_turnolunes > sum_turnomartes : 
                                print(f"\nEl dia con mas turnos asignados es el Lunes, con {sum_turnolunes} turno/s.")
                            elif sum_turnomartes > sum_turnolunes : 
                                print(f"\nEl dia con mas turnos asignados es el Martes, con {sum_turnomartes} turno/s.")
                            else:
                                print("\nninguno de los dias tiene mas turnos que el otro.")

                        case "5": 
                            break
                        case _ : 
                            print("Has ingresado una opcion no valida. Vuelve a intentarlo.")
                print("\n")
                ejercicio3 = False



            
        case 4 : 
            ejercicio4 = True
            while ejercicio4 : 
                
                energia = 100
                tiempo = 12
                cerraduras_abiertas = 0 
                alarma = False
                codigo_parcial = ""
                
                nombre_agente = input("\nIndique su nombre : ")
                while not nombre_agente.isalpha() :
                    print("Nombre de Agente invalido. Ingrese otro : ")
                    nombre_agente = input()
                print(f"BIENVENIDO Agente {nombre_agente}.\n")

                conteo_antispam = 0
                
                while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3: 
                    
                        print(f"\nESTADO : Cerraduras faltantes : {3-cerraduras_abiertas} - Energia : {energia} - Tiempo : {tiempo}.")
                        print("""\n     MENU DE ACCIONES 
--------------------------
                        
        selecciona una de las siguientes acciones : 
        1) Forzar cerradura
        2) Hackear panel
        3) Descansar   
                            """) 
                        seleccion = input()
                        while not seleccion.isdigit():
                            print("""No has seleccionado una opcion correcta.\n
        selecciona una de las siguientes acciones : 
        1) Forzar cerradura
        2) Hackear panel
        3) Descansar                          
                            """)
                            seleccion = input()
                        match seleccion : 
                            
                            case "1" : 

                                conteo_antispam += 1
                                energia -= 20
                                tiempo -= 2
                                
                                if conteo_antispam > 3 : 
                                    print("No puedes volver a forzar la cerradura... Prueba de otra manera.")
                                elif conteo_antispam == 3 :
                                    print("Forzaste de manera seguida... La cerradura se trabó y perdiste tiempo valioso. La alarma se ha activado !")
                                    alarma = True
    
                                elif energia < 40 and not alarma: 
                                    print ("Existe el riesgo de activar la Alarma...")

                                    sol_numero = input("Ingresa un numero del 1 al 3 :")
                                    while not sol_numero.isdigit() : 
                                        sol_numero = input("Dato invalido. Ingresa un numero del 1 al 3 :")
                                        
                                    numero_int = int(sol_numero)

                                    while numero_int < 1 or numero_int > 3 : 
                                        sol_numero = input("Dato invalido. Ingresa un numero del 1 al 3 :")
                                        numero_int = int(sol_numero)
                                    
                                    if numero_int == 3 :                                                   
                                        print("ATENCION - La alarma se ha activado!")
                                        alarma = True
                                    else : 
                                        print("Numero correcto. Continúa con tu misión.")
                                    
                                else:
                                    if not alarma: 
                                        cerraduras_abiertas += 1
                                        print(f"\nCerradura abierta ! ")
                                    elif alarma : 
                                        cerraduras_abiertas += 1
                                        print(f"\nCerradura abierta ! ")

                                
                            case "2" :
                                energia -= 10
                                tiempo -= 3
                                conteo_antispam = 0 

                                for caracteres in range (4): 
                                    codigo = input("Ingrese una letra : ")
                                    while not codigo.isalpha() or len(codigo) > 1 or codigo =="": 
                                        codigo = input("Dato incorrecto. Debes ingresar  1 letra :")
                                    
                                    codigo_parcial += codigo 

                                    if len(codigo_parcial) >= 8 : 
                                        cerraduras_abiertas += 1
                                        print(f"\nCerradura abierta ! ")
                                        break

                                    
                            case "3" : 
                                print("Tomate un descanso...")
                                conteo_antispam = 0 

                                energia += 15

                                if energia > 100 : 
                                    energia = 100 

                                tiempo -= 1 

                                if alarma : 
                                    energia -= 10 
                                
                            
                            case _ : 
                                print("Numero invalido. Vuelva a seleccionar una opcion valida.\n")
                    

                        if energia <= 0 or tiempo <= 0 : 
                            print(f"\nHas agotado tus recursos... Tu energia es {energia} y te queda {tiempo} de tiempo. El sistema se bloqueó. DERROTA !\n")
                            break
                        elif alarma == True and tiempo <= 3 and cerraduras_abiertas < 3: 
                            print(f"\nLa alarma está activa y el tiempo es de {tiempo}...El sistema se bloqueó. DERROTA !\n")
                            break
                        elif cerraduras_abiertas == 3 : 
                            print("Acabas de abrir todas las cerraduras. VICTORIA !\n")
                            break

                ejercicio4 = False
                    
                



        case 5: 
            ejercicio5 = True
            while ejercicio5 : 
        
                vida_gladiador = 100
                vida_enemigo = 100
                pociones_de_vida = 3 
                dañobase_ataque_pesado = 15
                dañobase_enemigo = 12
                turno_gladiador = True

                print("\n--- BIENVENIDO A LA ARENA ---\n")
                nombre_gladiador = input("Nombre del Gladiadr : ")
                while not nombre_gladiador.isalpha(): 
                    nombre_gladiador = input("Error: Solo se permiten letras. Indique su nombre : ")
                while nombre_gladiador == "": 
                    nombre_gladiador = input("Error: No se permiten espacios vacios. Indique su nombre : ")

                primer_turno = True  

                while vida_gladiador > 0 and vida_enemigo > 0 :


                    
                    for turno in range (1):

                        if primer_turno : 
                            print("=== INICIO DEL COMBATE ===")
                            primer_turno = False
                        else : 
                            print("=== NUEVO TURNO === ")
                        print(f"""-------------------------------------\n{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_de_vida}\n""")
                    
                        print("""Indica el digito de uno de estas tres opciones ( del 1 al 3 ): 

1. Ataque pesado
2. Ráfaga veloz
3. Curar\n""")
                        seleccion = input() 
                        while not seleccion.isdigit() : 
                            seleccion = input("ERROR : El valor ingresado es incorrecto. Ingresa un digito del 1 al 3 : ") 
                        while int(seleccion) != 1 and int(seleccion) != 2 and int(seleccion) != 3: 
                            seleccion = input("ERROR : El valor está fuera de rango. Ingresa un digito del 1 al 3 : ")     
                        daño_final = 0
                        match seleccion :
                            case "1" : 
                                if vida_enemigo < 20 : 
                                    daño_final = dañobase_ataque_pesado * 1.5
                                    vida_enemigo -= daño_final
                                    print("Realizaste un 'Golpe Critico'!")
                                    print(f"Atacaste al Enemigo por {daño_final} puntos de daño !")
                                else : 
                                    vida_enemigo -= dañobase_ataque_pesado 
                                    print(f"Atacaste al Enemigo por {dañobase_ataque_pesado} puntos de daño !")    

                            case "2" :                                    
                                print("Inicias una rafaga de golpes !")
                                for rafaga in range (3):
                                    vida_enemigo -= 5   
                                    print(f"Golpe conectado por 5 de daño")

                            case "3" : 
                                if pociones_de_vida > 0 : 
                                    vida_gladiador += 30 
                                    pociones_de_vida -= 1
                                    print(f"Has utilizado 1 pocion para curarte ! Te quedan {pociones_de_vida} pociones.")
                                elif pociones_de_vida == 0 : 
                                    print("No quedan mas pociones !\n")
                    
                    # Turno enemigo de ataque 
                    if vida_enemigo > 0 : 
                        vida_gladiador -= dañobase_enemigo
                        print (f"\n¡El enemigo contraataca por 12 puntos! \n")
                    else:
                        continue
                                    
                #Evaluacion final
                if vida_gladiador > 0 :
                    print(f"""\n¡VICTORIA! {nombre_gladiador} ha ganado la batalla !\n
----------------------------------------------""")    
                elif vida_gladiador <= 0 : 
                    print(f"""\nDERROTA. Has caído en combate.
----------------------------------------------""")

                ejercicio5 = False
                                
        case _: 
            print("No has ingresado un numero de ejercicio valido.")
            ejercicios = int(input("Indica con un numero del 1 al 5 el ejercicio que quiera evaluar :"))
    


            



