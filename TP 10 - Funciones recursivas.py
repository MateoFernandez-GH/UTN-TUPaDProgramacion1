while True: 
    print("\n=================TRABAJO PRACTICO N° 10===================")
    print("==========================================================")
    seleccion = input("Selecciona el n° del ejercicio que requieres evaluar ( del 1 al 8 ): ")
    while not seleccion.isdigit() : 
        seleccion = input("Selecciona el n° del ejercicio que requieres evaluar ( del 1 al 8 ): ")
    
    match seleccion : 
        case "1" : 

            # Definimos la funcion recursiva para calcular el factorial de un numero dado.
            def factorial(x): 
                return 1 if x == 0 else x * factorial( x - 1 )  # Formato TERNARIO para acortar mucho la estructura del codigo, y mejorar la legibilidad del 
                # contenido de la funcion. 
            
            # Solicitamos al usuario un numero entero para calcular su factorial, y validamos que el valor ingresado sea correcto.
            x_seleccionado = input("\nIndica el numero desde el cual calcular los factoriales : ")
            while not x_seleccionado.isdigit(): 
                x_seleccionado = input("\nValor invalido. Indica un numero entero desde el cual calcular los factoriales : ")
            
            # Imprimimos los factoriales desde el numero 1, hasta el numero ingresado por el usuario.
            for i in range (1, int(x_seleccionado) + 1 ):
                print(f"El factorial n° {i} es : {factorial(i)}")

        case "2": 

            # Definimos la funcion recursiva para calcular el numero de Fibonacci en una posicion dada.
            def fibonacci(posicion) : 
                if posicion == 0 or posicion == 1 :
                    return posicion
                else : 
                    return fibonacci(posicion-1) + fibonacci(posicion-2)
    

            # Solicitamos al usuario un numero entero para calcular los numeros de Fibonacci, y validamos que el valor ingresado sea correcto.
            x_seleccionado = input("\nIndica la posicion numerica desde el cual calcular los numeros de Fibonacci :")
            while not x_seleccionado.isdigit():
                x_seleccionado = input("\nValor invalido. Indica la posicion numerica desde el cual calcular los numeros de Fibonacci :")

                
            # Imprimimos los numeros de Fibonacci desde la posicion 0, hasta la posicion ingresada por el usuario.
            for i in range (0, int(x_seleccionado) + 1 ):
                print(f"El numero de Fibonacci para la posicion {i} es : {fibonacci(i)}")
        

        case "3":
            
            # Definimos la funcion recursiva para calcular la potencia de una base dada, elevada a un exponente dado.
            def potencia(base, exponente):
                if exponente == 0:  # Caso base: cualquier número elevado a la potencia de 0 es 1, por lo tanto retorna 1. 
                    return 1
                else:
                    return base * potencia(base, exponente - 1) # Caso recursivo hasta llegar al caso base. 
                
            # Solicitamos al usuario un numero entero para la base, y otro numero entero para el exponente, y validamos que los valores ingresados sean correctos.

            base_seleccionada = input("\nIndica la base para calcular la potencia : ")
            while not base_seleccionada.isdigit():  
                base_seleccionada = input("\nValor invalido. Indica la base para calcular la potencia : ")
            exponente_seleccionado = input("\nIndica el exponente para calcular la potencia : ")
            while not exponente_seleccionado.isdigit():
                exponente_seleccionado = input("\nValor invalido. Indica el exponente para calcular la potencia : ")
            
            try : 
                # Imprimimos el resultado de la potencia calculada con la funcion recursiva.
                print(f"\nEl resultado de {base_seleccionada} elevado a la potencia de {exponente_seleccionado} es : {potencia(int(base_seleccionada), int(exponente_seleccionado))}")  
            except RecursionError: # Insertamos un bloque de excepcion para manejar errores de recursividad, en caso de que el exponente ingresado por el usuario sea demasiado grande para ser calculado con la funcion recursiva definida.
                print("\nError: El exponente ingresado es demasiado grande para ser calculado con recursividad. Por favor, ingresa un exponente más pequeño.")
            except Exception as e: # Caso de excepcion general para manejar cualqueir otro tipo de error. 
                print(f"\nError inesperado: {e}")
            finally : 
                print("\nGracias por utilizar el programa. Vuelve a ejecutarlo si necesita evaluar otros valores.")

        

        case "4":

            # Definimos la funcion recursiva que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto. 
            def binarios(decimal): 
                # Caso base: si el numero decimal es 1, su representacion en binario es "1"
                if decimal == 1:
                    return "1"  # Al ser el un caso base 'string', puede concatenarse con el resultado de la llamada recursiva, que 
                    # tambien es un string, sin necesidad de convertir los resultados y posibilitando la operacion. 
                
                # Caso recursivo: se divide el numero decimal entre 2, y se concatena el resultado 
                # de la llamada recursiva con el resto de la división (que es el siguiente dígito binario)
                return binarios(decimal // 2) + str(decimal % 2)

            # Solicitamos al usuario un numero entero positivo en base decimal para convertir a binario, y validamos que el valor ingresado sea correcto.
            try: 
                decimal_str = input("\nIndica el numero entero positivo en base decimal para convertir a binario : ")

                # Validamos que el numero ingresado sea un entero positivo, y si no lo es, solicitamos al usuario que ingrese un valor correcto.

                while int(decimal_str) <= 0:
                    print("\nError: Debes ingresar un número entero positivo.")
                    decimal_str = input("\nIndica el numero entero positivo en base decimal para convertir a binario : ")
                    decimal_int = int(decimal_str)
                
            
                resultado = binarios(decimal_int) # Guardamos en "resultadao" el valor de la representacion en binario del numero decimal ingresado por el usuario, calculada 
                # con la funcion recursiva definida.
                print(f"\nLa representacion en binario de {decimal_str} es : {resultado}")

            # Bloques Except para manejar errores de conversion de tipos, y cualquier otro tipo de error inesperado.
            except ValueError: 
                print("\nError: El valor ingresado no es un numero entero válido.")
                print("\nGracias por utilizar el programa. Vuelve a ejecutarlo si necesita evaluar otros valores.")
                
            except Exception as e:
                print(f"\nError inesperado: {e}")
                print("\nGracias por utilizar el programa. Vuelve a ejecutarlo si necesita evaluar otros valores.")

        case "5":
        
            def es_palindromo(palabra):
                # Caso base: si la palabra evaluada por la recursividad termina con 0 o 1 caracteres, entonces es un palíndromo
                if len(palabra) <= 1:
                    return True
                
                # Caso recursivo: comparamos el primer y último carácter de la palabra
                if palabra[0] == palabra[-1]:
                    # Si son iguales, llamamos recursivamente a la función con la subcadena que excluye esos caracteres
                    return es_palindromo(palabra[1:-1])
                else:
                    # Si no son iguales, no es un palíndromo y corta la recursion.
                    return False

            # Solicitamos al usuario una palabra para evaluar si es un palíndromo, y validamos que el valor ingresado sea correcto.
            palabra_usuario = input("\nIndica la palabra para evaluar si es un palíndromo : ")
            while not palabra_usuario.isalpha():
                palabra_usuario = input("\nValor invalido. Indica la palabra para evaluar si es un palíndromo : ")

            # En caso el llamado de la funcion recursiva retorne True, indicamos que la palabra ingresada por el usuario es un palíndromo, y en caso contrario, indicamos que no lo es.
            if es_palindromo(palabra_usuario):  
                print(f"\nLa palabra '{palabra_usuario}' es un palíndromo.")
            else:
                print(f"\nLa palabra '{palabra_usuario}' no es un palíndromo.")

        case "6":
            
            # Definimos una funcion que reciba un número entero positivo y devuelva la suma de sus dígitos utilizando recursividad.
            def suma_digitos(n):
                # Caso base: si el número llega a ser 0, cortamos las llamadas recursivas y retornamos 0, ya que la suma de los dígitos de 0 es 0.
                if n == 0:
                    return 0
                # Caso recursivo: sumamos el último dígito con la suma de los dígitos del número sin ese dígito
                return (n % 10) + suma_digitos(n // 10)
        
            # Solicitamos al usuario un numero entero positivo para calcular la suma de sus dígitos, y validamos que el valor ingresado sea correcto.
            numero_usuario = input("\nIndica un numero entero positivo para calcular la suma de sus dígitos : ")
            while not numero_usuario.isdigit() or int(numero_usuario) <= 0:
                numero_usuario = input("\nValor invalido. Indica un numero entero positivo para calcular la suma de sus dígitos : ")        
            
            # Imprimimos el resultado de la suma de los dígitos del numero ingresado por el usuario, calculada con la funcion recursiva definida, convirtiendo a enteros.
            resultado = suma_digitos(int(numero_usuario))
            print(f"\nLa suma de los dígitos de {numero_usuario} es: {resultado}")

        case "7":
            # Definimos una funcion que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide. 
            def contar_bloques(n):
                # Caso base: si el número de bloques en el nivel más bajo es 1, entonces la pirámide completa solo necesita 1 bloque.
                if n == 1:
                    return 1
                # Caso recursivo: sumamos el número de bloques en el nivel actual con la cantidad de bloques necesarios para construir la pirámide con un nivel menos.
                return n + contar_bloques(n - 1)
            
            # print(contar_bloques(10)) -- > Prueba de la funcion recursiva para evaluar el calculo del total de bloques.

            # Solicitamos al usuario el numero de bloques en el nivel mas bajo de la piramide, y validamos que el valor ingresado sea correcto.
            nivel_1 = input("\nIndica el numero de bloques en el nivel mas bajo de la piramide : ")
            while not nivel_1.isdigit() or int(nivel_1) <= 0:
                nivel_1 = input("\nValor invalido. Indica el numero de bloques en el nivel mas bajo de la piramide : ")

            # Guardamos el resultado de la llamada de la funcion recursiva en una variabe separada, convirtiendo el argumento a numero entero. 
            resultado = contar_bloques(int(nivel_1))
            print(f"\nEl total de bloques necesarios para construir la pirámide es de : {resultado}")

        case "8":
            # Definimos una funcion que reciba un número entero y un dígito, y devuelva la cantidad de veces que ese dígito aparece en el número utilizando recursividad.
            def  contar_digito(numero, digito): 
                # Convertimos numero y digito a string para permitir la comparación de los caracteres, y la operación de slicing en el llamado recursivo.
                numero = str(numero) 
                digito = str(digito)

                # Caso base: si cadena queda vacía, cortamos las llamadas recursivas y retornamos 0, ya que no hay dígitos para contar.
                if len(numero) == 0: 
                    return 0

                # Caso recursivo: comparamos solo el último dígito y sumamos el resultado recursivo para el resto del número.
                return (1 if numero[-1] == digito else 0) + contar_digito(numero[:-1], digito)
            
            # Solicitamos al usuario un numero entero para evaluar, y un digito para contar sus apariciones en el numero ingresado.
            numero_usuario = input("\nIndica un numero entero para evaluar : ")
            while not numero_usuario.isdigit():
                numero_usuario = input("\nValor invalido. Indica un numero entero para evaluar : ")
            digito_usuario = input("\nIndica un digito para contar sus apariciones en el numero ingresado : ")
            while not digito_usuario.isdigit() or len(digito_usuario) != 1:
                digito_usuario = input("\nValor invalido. Indica un digito para contar sus apariciones en el numero ingresado : ")
            
            # Imprimimos el resultado en la terminal.
            print(f"\nLas veces que el digito apararece en el numero, es de {contar_digito(int(numero_usuario), int(digito_usuario))} veces")
            

    