# Ejercicio 1) 

print("Hola Mundo!")

# Ejercicio 2)

nombre=input("Indica tu nombre : ")

print(f"Hola {nombre}!")

# Ejercicio 3)

nombre=input("Indica tu nombre : ")
apellido=input("Indica tu apellido: ")
edad=input("Indica tu edad :")
residencia=input("Indica tu lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4)

radio=float(input("Ingrese el radio del circulo :")) 

π=3.14
area=π*radio**2
perimetro=2*radio*π

print(f"El area del circulo es de {area}, y el perimetro es de {perimetro}.")

# Ejercicio 5

segundos=int(input("Ingrese una cantidad de segundos: "))

horas=segundos//60

print(f"Equivalen a {horas} horas")

# Ejercicio 6 

numero=int(input("Ingrese un numero : "))

print(f"{numero} x 1 = {numero*1}")
print(f"{numero} x 2 = {numero*2}")
print(f"{numero} x 3 = {numero*3}")
print(f"{numero} x 4 = {numero*4}")
print(f"{numero} x 5 = {numero*5}")
print(f"{numero} x 6 = {numero*6}")
print(f"{numero} x 7 = {numero*7}")
print(f"{numero} x 8 = {numero*8}")
print(f"{numero} x 9 = {numero*9}") 
print(f"{numero} x 10 = {numero*10}")

# Ejercicio 7) 

numero1=int(input("Ingrese un numero entero distinto del 0 :"))
numero2=int(input("Ingrese otro numero entero distinto del 0 :"))

suma=numero1+numero2
division=numero1/numero2
multiplicacion=numero1*numero2
resta=numero1-numero2

print(f"la suma entre ambos numeros es de {suma}.")
print(f"la division entre ambos numeros es de {division}.")
print(f"la multiplicacion entre ambos numeros es de {multiplicacion}.")
print(f"la resta entre ambos numeros es de {resta}.")

# Ejercicio 8) 

peso=float(input("Indique su peso :"))
altura=float(input("Indique su altura :"))

masa=peso/(altura)**2

print(f"su indice de masa corporal es de {masa} imc.")

# Ejercicio 9) 

temperatura=int(input("Indique una temperatura celsius : "))

farenheit=9/5*temperatura+32 

print(f"Su equivalente en grados farenheit es {farenheit} .")

# Ejercicio 10) 

numero1=int(input("Indique el 1er numero :"))
numero2=int(input("Indique el 2do numero :"))
numero3=int(input("Indique el 3er numero :"))

promedio=(numero1+numero2+numero3)/3

print(f"El promedio entre todos los numeros es de {promedio} .")