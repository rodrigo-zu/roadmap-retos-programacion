# Creación de mis varibles
a = 10
b = 5

print("*************** OPERADORES ***************")
print("*************** Operadores aritméticos ***************")
 
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b  # Se divide y se redondea hacia abajo
modulo = a % b  # <-- Lo que sobra de la división
exponenciacion = a ** b  

# Imprimir resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)
print("Módulo:", modulo)
print("Exponenciación:", exponenciacion)

print("--------------------------------------------------")

print("*************** Operadores de comparación ***************")

print("a:", a)
print("b:", b)  
# Operador de igualdad 
if a == b:
    print("a es igual a b")

# Operador de desigualdad   
if a != b:
    print("a es diferente de b")

# Operador mayor que
if a > b:
    print("a es mayor que b")

# Operador menor que
if a < b:
    print("a es menor que b")

# Operador mayor o igual que
if a >= b:
    print("a es mayor o igual que b")

# Operador menor o igual que
if a <= b:
    print("a es menor o igual que b")

print("--------------------------------------------------")   

print("*************** Operadores lógicos ***************")

# Operador AND
if a > 0 and b > 0:
    print("a y b son positivos")

# Operador OR (Or solo pide que se cumpla una de las condiciones)
if a > 0 or b < 0:
    print("Al menos uno de los números es positivo")

# Operador NOT (Pide que no sea verdadero)
if not a < 0:
    print("a no es negativo")

print("--------------------------------------------------")

print("*************** Operadores de asignación ***************")

# Lo que nos permiten los operadores de asignación es modificar el valor de una variable sin 
# tener que escribir toda la operación, por ejemplo:

# Variable a modificar con los operadores de asignación
c = 10

print(f'Valor inicial de c: {c}')
# Operador de asignación suma
c += 5 
print(f'Este es el de la suma: {c}')  # Esto es equivalente a c = c + 5

# Operador de asignación restante
c -= 3 
print(f'Este es el de la resta: {c}')  # Esto es equivalente a c = c - 3

# Operador de asignación multiplicación
c *= 2
print(f'Este es el de la multiplicación: {c}')  # Esto es equivalente a c = c * 2

#  Operador de asignación división
c /= 4
print(f'Este es el de la división: {c}')  # Esto es equivalente a c = c / 4

# Operador de asignación división entera
c //= 2
print(f'Este es el de la división entera: {c}')  # Esto es equivalente a c = c // 2   

#Operador de asignación módulo
c %= 3
print(f'Este es el del módulo: {c}')  # Esto es equivalente a c = c % 3

# Operador de asignación exponenciación
c **= 2
print(f'Este es el de la exponenciación: {c}')  # Esto es equivalente a c = c ** 2

print("--------------------------------------------------")

print("*************** Operadores de identidad ***************")
# De preferencia se usa con None, no con números, cadenas o listas en esos casos 
# es mejor usar el operador de comparación ==

# Se usan flotantes porque si usara enteros, el operador is me diría que son iguales, 
# pero en realidad no lo son, solo qu elos almacena en la misma dirección de memoria, 
# por eso es mejor usar flotantes en este caso

my_number = 1.0
my_new_number = 10

print(f'Valor de my_number: {my_number}')
print(f'Valor de my_new_number: {my_new_number}')

print(f'Así es con is: {my_number is my_new_number}')  
print(f'Así es con is not: {my_number is not my_new_number}')

print("--------------------------------------------------")

print("*************** Operadores de pertenencia ***************")
# Se usan para verificar si un elemento está o no en una secuencia (lista, 
# tupla, diccionario, conjunto o cadena de texto)
name = "Rodrigo"
print(f'¿"R" está en {name}? { "R" in name }')  # True
print(f'¿"R" no está en {name}? { "R" not in name }')  # False

print("--------------------------------------------------")

print("*************** Operadores de bit ***************")
# Se usan para realizar operaciones bit a bit sobre números enteros

# Variables a usar

x = 5  # En binario: 0101 
y = 3  # En binario: 0011 
print(f'Valor de x: {x} (en binario: {bin(x)})')
print(f'Valor de y: {y} (en binario: {bin(y)})')

# Operacion AND bit a bit (Compara cada bit de los números y devuelve 1 si ambos bits son 1,
# de lo contrario devuelve 0)
print(f'El resultado de x AND y: {x & y}')  # Resultado: 1 (en binario: 0001)

# Operacion OR bit a bit (Compara cada bit de los números y devuelve 1 si al menos uno de 
# los bits es 1, de lo contrario devuelve 0)
print(f'El resultado de x OR y: {x | y}')  # Resultado: 7 (en binario: 0111)

# Operacion XOR bit a bit (Compara cada bit de los números y devuelve 1 si los bits son 
# diferentes, de lo contrario devuelve 0)
print(f'El resultado de x XOR y: {x ^ y}')  # Resultado: 6 (en binario: 0110)

# Operacion NOT bit a bit (Invierte los bits del número, cambiando 1 por 0 y 0 por 1)
print(f'El resultado de NOT x: {~x}')  # Resultado: -6  

# Operacion de desplazamiento a la derecha (Desplaza los bits del número hacia la derecha, 
# eliminando los bits más a la derecha)
print(f'El resultado de x desplazado a la derecha: {x >> 1}')  # Resultado: 2 (en binario: 0010)

# Operacion de desplazamiento a la izquierda (Desplaza los bits del número hacia la izquierda, 
# agregando ceros a la derecha)
print(f'El resultado de x desplazado a la izquierda: {x << 1}')  # Resultado: 10 (en binario: 1010)

print("--------------------------------------------------")

print("*************** ESTRUCTURAS DE CONTROL ***************")

print("*************** Estructura condicionales ***************")

name = "Rodrigo"
if name == "Rodrigo":
    print("Tu nombre es Rodrigo")
elif name == "Juan":
    print("Tu nombre es Juan")
else:
    print("Hola desconocido")

print("--------------------------------------------------")
print("*************** Estructura de control iterativas ***************")

# Este es un ciclo for
for i in range(5):
    print(f'Iteración con un tipo for {i}')

# Este es un ciclo while

o = 0 

while o <= 5:
    print(f'Iteración con un tipo while {o}')
    o += 1

print("--------------------------------------------------")
print("*************** Estructura de control para manejo de excepciones ***************")

# Cuanto try y except se usan para manejar errores que puedan ocurrir durante la ejecución 
# de un programa y nuestro programa no se detenga, sino que pueda continuar ejecutándose a 
# pesar de los errores.
try:
    print(10/0)
except:
    print("Error: División por cero no permitida.")
# Finally se ejecuta siempre, sin importar si hubo o no una excepción. 
# Se utiliza para liberar recursos, cerrar archivos, etc.
finally:
    print("Ha finalizado el manejo de excepciones.")

print("--------------------------------------------------")
print()
print()
print("*************** Desafío del temario ***************")

# Almacenamos nuestros numeros
list_num = range(10, 56)  # Rango de números del 10 al 55 (inclusive)

# Ciclo for para recorrer la lista de números
for num in list_num:
    # COndiciones que se nos piden
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)  
