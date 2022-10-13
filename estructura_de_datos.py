#ESTRUCTURA DE DATOS 
#-----------------------------------------------------------------------------------------------------
# El tipo de dato lista tiene algunos métodos más. Aquí están todos los métodos de los objetos lista:
#-----------------------------------------------------------------------------------------------------

#----------------------------------EJEMPLOUSANDO LA MAYORIAS DE LISTAS-------------------------------------
#5.1. Más sobre listas
carros = ['ferrari', 'toyota', 'niza', 'lamborgini', 'mclaren', 'Chevrolet ',' Porsche']
x = carros.count('toyota') #se utiliza para encontrar cuantas veces  esta el carro en la lista
z = carros.count('ferrari')
print(x)
print(z)
# #-----------------------------------------------------------------------------------------------------------
c = carros.index('mclaren')
i = carros.index('mclaren', 1)  # este carro va estar en la posicion 1 de la lista
print(c)
print(i)
#-----------------------------------------------------------------------------------------------------------
carros.reverse() # invierte los elmentos de la lista
print(carros)
#-----------------------------------------------------------------------------------------------------------
carros.append('suzuki') # es para gregar un nuevo valor o item a la lista
print(carros)
#-----------------------------------------------------------------------------------------------------------
carros.sort(reverse=True) # ordena los Elementos de la lista segun uno quiera
carros
print(carros)
#-----------------------------------------------------------------------------------------------------------
carros.pop(3) #elimina el valor de la posicion marcada dentro de la lista
print(carros)
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#5.1.1. Usando listas como pilas
#vamos a utilizar en este caso el de agregar que es append y el de eliminar que es pop
montaña = [3, 4, 5]
montaña.append(6)
montaña.append(7)
print(montaña)
#-----------------------------------------------------------------------------------------------------------
montaña.pop(4)
print(montaña)
montaña.pop(3)
print(montaña)
#-----------------------------------------------------------------------------------------------------------


# 5.1.2. Usando listas como colas}
# las listas tambien se puede usar com una especie de cola entonces la didea es que ahora se borren y agreguen items al comienzo de la fila y no al final para eso se utiliza el  collections.deque.
from collections import deque
nombre = deque(["Eric", "Juan", "dana"])
nombre.append("jose")           # primer agregado 
nombre.append("sara")           # segundo agregado
nombre.popleft()
'primer nombre de la lista'     # se va el primeor que llego a la lista
nombre.popleft()                # se va el segundo que llogo a lista 
'segundo nombre de la lista'
print(nombre)                   # como quedaria con los dos que se fueron y los dos que entraron 
#-----------------------------------------------------------------------------------------------------------


# 5.1.3. Comprensión de listas
# en este vamos aver maneras de crear listas pero sitisfaciendo unas condiciones ya predertiminada
squares = []
for x in range(10):
    squares.append(x**2)
    print(squares)
# tambien se puede escribir de esta manera
squares = list(map(lambda x: x**2, range(10)))
print(squares)
# tambien puedes hacerlo de esta manera
squares = [x**2 for x in range(10)]
#-----------------------------------------------------------------------------------------------------------

# tambien hay otra lista que consiste en el uso de los  for o if 
combs = []
for x in [1,2,6]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
            print(combs)
#-----------------------------------------------------------------------------------------------------------


# 5.1.4. Listas por comprensión anidadas
#La expresión inicial de una comprensión de listas puede ser cualquier expresión arbitraria, incluyendo otra comprensión de listas.
matrix = [
[1, 2, 3, 4],
[9, 10, 11, 12],
]
[[row[i] for row in matrix] for i in range(4)]
print(matrix)
#toda va dentro del for o bueno es como en lo que se basa mas bien 
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
transposed
print(transposed)
#-----------------------------------------------------------------------------------------------------------


# 5.2. La instrucción
# Hay una manera de quitar un ítem de una lista dado su índice en lugar de su valor y en este caso se usa el del en ves del pop() que lo que hace es retornar un valor o quitarlo de la lista 
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[0:4:6]
print(a)
#-----------------------------------------------------------------------------------------------------------


# 5.3. Tuplas y secuencias
# ya vimos las las listas y las cadenas o filas tiens cosas en comun con sus operacion de seccionado, ahoara vamos a pasar a otro dato de tipo secuencia estándar: la tupla.
#exactamente la tupla consiste de un número de valores separados por comas, por ejemplo:
t = 'hola', 'como', 'estas!'
t[1]
print(t)
#-----------------------------------------------------------------------------------------------------------
# las tuplas tambien se pueden combinar vamso a usar la de arriba:
u = t, (1, 2, 3, 4, 5)
print(u)
#-----------------------------------------------------------------------------------------------------------
# Pero ellas pueden contener objetos mutables.
v = ([1, 2, 3], [3, 2, 1])
print(v)
#-----------------------------------------------------------------------------------------------------------
# como ya vimos, las tuplas se encierran entre parentesis, para que se han correctas, pero tambien se podria utlizar sin corchetes pero los parentesisi son necesarios.
# en la tuplas no se puede murtar nada pero es posible que contengan objetos o items mutables.
# A pesar de que las tuplas puedan parecerse a las listas, frecuentemente se utilizan en distintas situaciones y para distintos propósitos
entidad = ('wiii')
singleton = 'hola profe, como estas',  
len(entidad)
len(singleton)
print(entidad)
print(singleton)
#-----------------------------------------------------------------------------------------------------------


# 5.4 Conjuntos
# python tambien tiene un tipo de dato combrado 'COJUNTOS',conjunto es una colección no ordenada y sin elementos repetidos.
#en este caso todo lo duplicado se trasforma o elimina y un acracteristicas d elos cojuntos es que soportan operaciones matematicas  

# para crear cojuntos en este caso se utiliza la funcion set()
apellidos = {'navarro', 'salazar', 'gomez', 'velandia', 'gutierrez', 'chacon','salazar'}
print(apellidos) # mostrar que se han eliminado los duplicados

# demostracion de operaciones
a = set('esternocleidomastoideo')
b = set('dimicular')
print(a)
print(a-b)
print(a & b)
print(a ^ b)
# los cojuntos es similar a la comprecion de 

# 5.5 Diccionarios
# en python hay otro tipo de dato nombrado 'DICCIONARIO', los diccionarios sebsan en otro lenguaje que no son secuencias si no que usan las memorias y arreglos asociativos y se in dexan atravez de claves y es necesario que las claves se han unicas y entonces las operaciones principales sobre un diccionario son guardar un valor con una clave y extraer ese valor dada la clave.
# "Ejecutando list(d) en un diccionario retornará una lista con todas las claves usadas en el diccionario, en el orden de inserción (si deseas que esté ordenada simplemente usa sorted(d) en su lugar). Para comprobar si una clave está en el diccionario usa la palabra clave in."
telefono = {'juan': 409823455, 'pedro': 413978562}
telefono['guido'] = 412745687
telefono['juan']
del telefono['pedro']
telefono['irv'] = 412745789
list(telefono)
sorted(telefono)
'guido' in telefono
'juan' not in telefono
print(telefono)
# es posible crear una secuencia de diccionario con un dic() hagamos un ejemplo 
dict([('juan', 409823459), ('pedro',413978562), ('irv', 412745789)])
#-----------------------------------------------------------------------------------------------------------



# 5.6. Técnicas de iteración

# Cuando realizamos iteraciones con los diccionarios podemos obtener la clave y su valor, haciendo uso de:
# (items()), como vemos en el ejemplo:\n''')

four = {'v': 'BUENAS', 'n': 'CITY'}
for v, n in four.items():
  print(v, n)

print(
  '1 ejemplo'
)

for a, b in enumerate(['banano', 'manzana', 'fesa']):
  print(a, b)

print(
  '2 ejemplo'
)

primero = ['helado', 'torticas', 'pansito bueno']
segundo = ['Sí', 'No', 'No lo he probado']
for a, b in zip(primero, segundo):
  print('Te gusta el {0}?. A mí ¿?_ {1}.'.format(a, b))
#Lo que estamos haciendo es agignarler unas palabras especificas en unos lugares específicos y a estas palabras les damos unas codiciones con el ciclo (for) para que se repita las veces que necesitemos (iteraciones) y así cada una se combina dependiendo de como queramos.

print(
  '3 ejemplo'
)

for i in reversed(range(2, 20, 2)):
  print(i)
#Entonces solo generamos un ciclo que contara desde el (2) hasta el (20) llendo de 2 en 2, acompañado con la función (reversed).

print(
  '4 ejemplo'
)

five = [
  '1','2','3','4','5','6','7','8',
]
for i in sorted(five):
  print(i)

print(
  '5 ejemplo'
)

five = [
  '9','10','11','12','13','14','15','16',
]
for i in sorted(set(five)):
    print(i)


#-----------------------------------------------------------------------------------------------------------
# 5.7. Más acerca de condiciones
# Acerca de Condiciones 
# Las condiciones como while o if generalmente utilizan 
# cualquier tipo de operador no solamente comparaciones.
# Uno de ello son los operadores de comparacion in y not in
# que determinan si un valor esta o no esta dentro del contenedor.
# Tambien existen los operadores is y is not que compara si dos objetos son realmente
# el mismo objeto, tambien cabe destacar que todos los operadores de comparacion tienen
# la misma prioridad, pero es menor que la de los operadores numericos
num1= 5
num2= 8

print(num1 < num2)
print(num1==num2)
print(num1>=num2)
print(num2 != num1)

x = 6
y = x>5 and x<7 
z = x>5 or x<7 
o = not x>5

print(y)
print(z)
print(o)
#-----------------------------------------------------------------------------------------------------------


# 5.8. Comparando secuencias y otros tipos
# Una secuencia se puede comparar con otros objetos del mismo tipo de secuencia. El orden léxico se utiliza para la comparación.
# ya despues se comporan los dos primeros elementos y se determina el resultado de de ese comparacion de elementos y ay despues de hacerlo se intenta llegar el final de una matriz

#-----------------------------------------------------------------------------------------------------------
# PROFE LA VERDAD NO PUDE ENTENDER EL EJEMPLO DE SECUENCIAS 
#-----------------------------------------------------------------------------------------------------------

