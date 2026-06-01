# Ejercicio 1) 

edad=int(input("Indicanos tu edad : "))

if edad > 18 :
    print("Es mayor de edad")

# Ejercicio 2) 

nota=int(input("Indicanos tu nota : "))

if nota >= 6 : 
    print ("Aprobado")
elif nota < 6 : 
    print ("Desaprobado")

# Ejercicio 3) 

numero=int(input("Ingrese un numero par : "))

if numero % 2 == 0: 
    print ("Ha ingresado un numero par")
else:
    print ("Por favor, ingrese un número par")

# Ejercicio 4) 

edad=int(input("Indicanos tu edad :"))

if edad < 12 : 
    print ("Pertenece a la categoria : Niño")
elif edad >= 12 : 
    if edad < 18:
        print ("Pertenece a la categoria : Adolescente")
    elif edad < 30: 
        print ("Pertenece a la categroria : Adulto/Joven")
    else: 
        print ("Pertenece a la categoria : Adulto")


# Ejercicio 5) 

contraseña=input("Introduzca su contraseña :") 

longitud=len(contraseña)

if longitud >= 8 and longitud <= 14 :
    print("Ha ingresado una contraseña correcta")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6) 

consumo=int(input("Ingrese su consumo mensual de energia electrica en kWh : "))

if consumo < 150 :
    print("Consumo bajo")
elif consumo >= 150 and consumo <= 300:
    print("Consumo medio")
else :
    print ("Consumo alto")
    print ("Considere medidas de ahorro energético")

# Ejercicio 7) 

string_usuario=(input("Ingrese una palabra o frase : "))

ultimo=string_usuario[-1]

if ultimo in "aeiouAEIOU":
    nuevo_string = string_usuario + " !"
    print (nuevo_string)
else:
    print (string_usuario)

# Ejericio 8) 

nombre=input("Ingrese su nombre : ")

print ("Si quieres tu nombre en mayusculas, ingresa el numero 1.")
print ("Si quieres tu nombre en minusculas, ingresa el numero 2.")
print ("Si quieres tu nombre con la primer letra mayuscula, ingresa el numero 3.")

numero=int(input("Numero : ")) 

if numero==1 :
    print(nombre .upper())
elif numero==2 : 
    print(nombre .lower()) 
elif numero==3 :
    print(nombre .title())


# Ejercicio 9)

terremoto=float(input("Ingrese la magnitud de un terremoto dentro de la escala Richter : "))

if terremoto < 3 :
    print ("Categoria : Muy Leve (imperceptible)" )
elif terremoto >= 3 :
    if terremoto < 4 : 
        print ("Categoria : Leve (ligeramente perceptible)")
    elif terremoto < 5 : 
        print ("Categoria : Moderado (sentido por personas, pero generalmente no causa daños)")
    elif terremoto < 6 : 
        print ("Categoria : Fuerte (puede causar daños en estructuras débiles)")
    elif terremoto < 7 : 
        print ("Categoria : Muy Fuerte (puede causar daños significativos)")
    else: 
        print ("Categoria : Extremo (puede causar graves daños a gran escala)")



# Ejercicio 10) 

hemisferio=input("Indica en que hemisferio del mundo te encuentras (N / S): ") .lower()

mes=int(input("Indica el n° de mes en el que estamos: "))

dia=int(input("Indica que dia es hoy : "))

if hemisferio=="n": 
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20 ) :
        print ("Estamos en Invierno")
    elif (mes >= 3 and dia >= 21) or (mes <= 6 and dia <= 20 ) : 
        print ("Estamos en Primavera")
    elif (mes >= 6 and dia >= 21) or (mes <= 9 and dia <= 20 ) :
        print ("Estamos en Verano")
    elif (mes >= 9 and dia >= 21) or (mes <= 12 and dia <= 20 ) : 
        print ("Estamos en Otoño")
elif hemisferio=="s": 
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20 ) :
        print ("Estamos en Verano")
    elif (mes >= 3 and dia >= 21) or (mes <= 6 and dia <= 20 ) : 
        print ("Estamos en Otoño")
    elif (mes >= 6 and dia >= 21) or (mes <= 9 and dia <= 20 ) :
        print ("Estamos en Invierno")
    elif (mes >= 9 and dia >= 21) or (mes <= 12 and dia <= 20 ) : 
        print ("Estamos en Primavera")


