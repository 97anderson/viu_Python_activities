"""
PYTHON 101, FUNTIONS
1. Escribe una función que reciba como entrada una *lista* con números y devuelva como resultado una *lista* con los cuadrados de los números contenidos en la lista de entrada.

2. Escribe una función que reciba números como entrada y devuelva la suma de los mismos. La función debe ser capaz de recibir una cantidad indeterminada de números. La función no debe recibir directamente ningún objeto complejo (lista, conjunto, etc.).

3. Escribe una función que reciba un string como entrada y devuelva el string al revés. Ejemplo: si el string de entrada es 'hola', el resultado será 'aloh'.

4. Escribe una función *lambda* que, al igual que la función desarrollada en el ejercicio anterior, invierta el string recibido como parámetro. Ejemplo: si el string de entrada es 'hola', el resultado será 'aloh'.

5. Escribe una función que compruebe si un número se encuentra dentro de un rango específico.

6. Escribe una función que reciba un número entero positivo como parámetro y devuelva una lista que contenga los 5 primeros múltiplos de dicho número. Por ejemplo, si la función recibe el número 3, devolverá la lista [3, 6, 9, 12, 15]. Si la función recibe un parámetro incorrecto (por ejemplo, un múmero menor o igual a cero), mostrará un mensaje de error por pantalla y devolverá una lista vacía.

7. Escribe una función que reciba una lista como parámetro y compruebe si la lista tiene duplicados. La función devolverá *True* si la lista tiene duplicados y *False* si no los tiene.

8. Escribe una función *lambda* que, al igual que la función desarrollada en el ejercicio anterior, reciba una lista como parámetro y compruebe si la lista tiene duplicados. La función devolverá *True* si la lista tiene duplicados y *False* si no los tiene.

9. Escribe una función que compruebe si un string dado es un palíndromo. Un palíndromo es una secuencia de caracteres que se lee igual de izquierda a derecha que de derecha a izquierda. Por ejemplo, la función devolverá *True* si recibe el string "reconocer" y *False* si recibe el string "python".
"""

#1. Escribe una función que reciba como entrada una *lista* con números y devuelva como resultado una *lista* con los cuadrados de los números contenidos en la lista de entrada.
print("EJERCICIO 1")
lista = [1,2,3,4,5]

def funcion_lista_cuadrados(lista):   
    lista_cuadrada = []
    for element in lista:
        lista_cuadrada.append(element ** 2)
    return lista_cuadrada
print(funcion_lista_cuadrados(lista))

#2. Escribe una función que reciba números como entrada y devuelva la suma de los mismos. La función debe ser capaz de recibir una cantidad indeterminada de números. La función no debe recibir directamente ningún objeto complejo (lista, conjunto, etc.).
print("EJERCICIO 2")
def funtion_sum(*number):
    sum = 0
    for element in number:
        sum += element
    return sum
print(funtion_sum(1,2,3,4,5,6,7,8))
    
#3. Escribe una función que reciba un string como entrada y devuelva el string al revés. Ejemplo: si el string de entrada es 'hola', el resultado será 'aloh'.
print("EJERCICIO 3")
def alreves(work):
    contador = len(work)
    word=""
    while contador > 0:
        word += work[contador-1]
        contador-=1
    return word

print(alreves("Hola"))

#4. Escribe una función *lambda* que, al igual que la función desarrollada en el ejercicio anterior, invierta el string recibido como parámetro. Ejemplo: si el string de entrada es 'hola', el resultado será 'aloh'.
print("EJERCICIO 4")
word = lambda key : key[::-1]
print(word("hola Mundo"))

#5. Escribe una función que compruebe si un número se encuentra dentro de un rango específico.
print("EJERCICIO 5")
def range(number, range):
    if number in range:
        print("El numero Se encuentra en el rango especificado")
    else:
        print("El numero No se encuentra en el rango especificado")
range(9,{1,2,3,4,5})

result = lambda numero, rango : f"El numero Se encuentra en el rango especificado" if numero in rango else f"El numero No se encuentra en el rango especificado"
print(result(5,[1,2,3,4,5]))


#6. Escribe una función que reciba un número entero positivo como parámetro y devuelva una lista que contenga los 5 primeros múltiplos de dicho número. Por ejemplo, si la función recibe el número 3, devolverá la lista [3, 6, 9, 12, 15]. Si la función recibe un parámetro incorrecto (por ejemplo, un múmero menor o igual a cero), mostrará un mensaje de error por pantalla y devolverá una lista vacía.
print("EJERCICIO 6")
def positive_number(number):
    lista=[]
    position=range(5)
    
    for element in position:
        lista.append(number * (element+1))
    return lista

print(positive_number(5))

# 7. Escribe una función que reciba una lista como parámetro y compruebe si la lista tiene duplicados. La función devolverá *True* si la lista tiene duplicados y *False* si no los tiene.
print("EJERCICIO 7")
def validar_duplicados(lista):
    converted = set(lista)
    return bool(len(converted)!=len(lista))

print(validar_duplicados([1,2,3,4,5,6,7,8]))
deploy=inttegrio
