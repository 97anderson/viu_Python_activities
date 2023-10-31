"""
PYTHON 101, DATA TYPES

1. Escribe un programa que muestre por pantalla la concatenación de un número y una cadena de caracteres. Para obtener esta concatenación puedes usar uno de los operadores explicados en este tema. Ejemplo: dado el número 3 y la cadena 'abc', el programa mostrará la cadena '3abc'.

2. Escribe un programa que muestre por pantalla un valor booleano que indique si un número entero *N* está contenido en un intervalo semiabierto *[a,b)*, el cual establece una cota inferior *a* (inclusive) y una cota superior *b* (exclusive) para *N*.

3. Escribe un programa que, dado dos strings *S1* y *S2* y dos números enteros *N1* y *N2*, determine si el substring que en *S1* se extiende desde la posición *N1* a la *N2* (ambos inclusive) está contenido en *S2*.

4. Dada una *lista* con elementos duplicados, escribir un programa que muestre una nueva *lista* con el mismo contenido que la primera pero sin elementos duplicados.

5. Escribe un programa que, dada una *lista* de strings *L*, un string *s* perteneciente a *L* y un string *t*, reemplace *s* por *t* en *L*. El programa debe mostrar la lista resultante por pantalla.

6. Escribe un programa que defina una *tupla* con elementos numéricos, reemplace el valor del último por un valor diferente y muestre la *tupla* por pantalla. Recuerda que las *tuplas* son inmutables. Tendrás que usar objetos intermedios.

7. Dada la lista [1,2,3,4,5,6,7,8] escribe un programa que, a partir de esta lista, obtenga la lista [8,6,4,2] y la muestre por pantalla.

8. Escribe un programa que, dada una tupla y un índice válido *i*, elimine el elemento de la tupla que se encuentra en la posición *i*. Para este ejercicio sólo puedes usar objetos de tipo tupla. No puedes convetir la *tupla* a una *lista*, por ejemplo.

9. Escribe un programa que obtenga la mediana de una *lista* de números. Recuerda que la mediana *M* de una lista de números *L* es el número que cumple la siguiente propiedad: la mitad de los números de *L* son superiores a *M* y la otra mitad son inferiores. Cuando el número de elementos de *L* es par, se puede considerar que hay dos medianas. No obstante, en este ejercicio consideraremos que únicamente existe una mediana.
"""

# 1. Escribe un programa que muestre por pantalla la concatenación de un número y una cadena de caracteres. Para obtener esta concatenación puedes usar uno de los operadores explicados en este tema. Ejemplo: dado el número 3 y la cadena 'abc', el programa mostrará la cadena '3abc'.
input("EJERCICIO #1")
numero = 1
cadena = "Esto es una cadena de texto, con valor: "
input(cadena + str(numero))

# 2. Escribe un programa que muestre por pantalla un valor booleano que indique si un número entero *N* está contenido en un intervalo semiabierto *[a,b)*, el cual establece una cota inferior *a* (inclusive) y una cota superior *b* (exclusive) para *N*.
input("EJERCICIO #2")
N = 9
a = 0
b = 10
print(a <= N and N < b)


# 3. Escribe un programa que, dado dos strings *S1* y *S2* y dos números enteros *N1* y *N2*, determine si el substring que en *S1* se extiende desde la posición *N1* a la *N2* (ambos inclusive) está contenido en *S2*.
input("EJERCICIO #3")
S1 = "Hola Mundo" 
S2 = "Hola Mundo en Python"
N1 = 0
N2 = 9

print("S1 esta contenido en S2: ")
print(S1[N1:N2+1] in S2)


#4. Dada una *lista* con elementos duplicados, escribir un programa que muestre una nueva *lista* con el mismo contenido que la primera pero sin elementos duplicados.
input("EJERCICIO #4")
lista = [1,1,2,3,4,5,5,6,7,8,1]
print(list(set(lista)))

#5. Escribe un programa que, dada una *lista* de strings *L*, un string *s* perteneciente a *L* y un string *t*, reemplace *s* por *t* en *L*. El programa debe mostrar la lista resultante por pantalla.
input("EJERCICIO #5")
s = "BMW"
t = "Toyota"
L = ["Mazda",s, "audi", "Ferrari",t]
L[L.index(s)] = t
print(L)

#6. Escribe un programa que defina una *tupla* con elementos numéricos, reemplace el valor del último por un valor diferente y muestre la *tupla* por pantalla. Recuerda que las *tuplas* son inmutables. Tendrás que usar objetos intermedios.
input("EJERCICIO #6")
tupla = (1,2,3,4,5,6,7,8)
tupla_new = (9,)
tupla += tupla_new
print(tupla)
