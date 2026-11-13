# Tenemos funciones definidas por el usuario las cuales son bloques de código que nos permiten reutilizar código
print('************ Función normal ************')
def greet ():
    print('Hola, python')

greet()

print()

# También tenemos funciones con retornos que van a ejecutar una lógica y van a acabar por devolver algo
print('************ Función con return ************')
def return_greet ():
    return 'Hola python'

greet = return_greet()
print(greet)

print()

# Las funciones con argumento son funciones a las que les podemos pasar un parámetro a la función 
print('************ Función con un argumento ************')
def arg_greet(name):
    print(f'Hola,  {name}!')

arg_greet('Rodri')

print()

# Las funciones con argumentos son funciones a las que les podemos pasar parámetros a la función 
print('************ Función con más de un argumento ************')
def args_greet(greet, name):
    print(f'{greet}, {name}!')

args_greet('Hi', 'Rodri')

print()

# Las funciones con argumentos predeterminados a las que les podemos pasar parámetros a la función 
print('************ Función  con un argumento por default ************')
def def_arg_greet(name='Python'): # <== Lo que hace este bloque de código aqui en python es que le da un nombre por default 
                                  # en caso de que nosotros no le estemos dando ese nombre como argumento   
    print(f'Hola, {name}!')

def_arg_greet() # < == Pddemos ejecutarlo con o sin argumento porque ya tiene uno por default

print()

# También nos permite especificarle cual linea de código corresponde a que argumento que le estemos dando
print('************ Función específicando el orden de nuestros argumentos ************')
def args_greet(greet, name):
    print(f'{greet}, {name}!')

args_greet(name ='Rodri', greet = 'Hi')

