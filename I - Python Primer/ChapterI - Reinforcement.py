#Code Fragment 1.1

def ejemplo1():
    print "Calcula el promedio de tus calis"
    print "Ingresa todas tus calificaciones, una por linea"
    print "Ya que termines ingresa una linea en blanco"

    puntos={"A+":4.0, "A":4.0, "A-":3.67, "B+":3.33,"B":3.0,"B-":2.67,"C+":2.33,"C":2.0,"C-":1.67,"D+":1.33,"D":1.0,"F":0.0}

    num_clases=0
    puntos_totales=0

    done=False

    while not done:
        grade=input()
        grade=grade.upper()
        if grade == '':
            done = True
        elif grade not in puntos:
            print "Calificacion desconocida", grade
        else:
            num_clases+=1
            puntos_totales+=puntos[grade]
        if num_clases>0:
            print "Tu promedio es", puntos_totales/num_clases

#R-1.1

def is_multiple(n,m):
    """
    is_multiple returns True if n is a multiple of m or
    if m is a multiple of n.
    """
    if n % m == 0 or m % n == 0:
        return True
    else:
        return False

#R-1.2

def is_even(k):
    """
    is_even takes an integer value and returns True if k is
    even, False otherwise. Do not use multiplication, module or division
    """
    return True if (-1)**abs(k)==1 else False

#R-1.3

def minmax(data):
    """
    minmax(data) : Toma una secuencia de uno o mas numeros y regresa el mas 
    pequeno y el mas grande, en una tupla de tamano dos. No usar las funciones 
    min y max de python
    """
    arreglo=sorted(data)
    return (arreglo[0], arreglo[len(arreglo)-1])
    
#R-1.4

def suma_cuadrados(n):
    """
    Toma un entero positivo y regresa la suma de los cuadrados de todos los 
    enteros positivos menores a n.
    """
    if n<=0:
        return 0
    return (n-1)**2+suma_cuadrados(n-1)

#R-1.5

def suma_cuadrados_lista(n):
    """
    Realizar una suma de cuadrados utilizando comprension de listas
    """
    return sum([e**2 for e in range(n)])

#R-1.6

def suma_cuadrados_par(n):
    """
    Realizar una suma de cuadrados utilizando comprension de listas de los 
    numeros pares.
    """
    if n<=0:
        return 0
    if n%2==0:
        return n**2 + suma_cuadrados_par(n-1)
    else:
        return 0 + suma_cuadrados_par(n-1)

#R-1.7

def suma_cuadrados_par_lista(n):
    """
    Realizar una suma de cuadrados utilizando comprension de listas de los 
    numeros pares.
    """
    return sum([e**2 for e in range(n) if e%2==0])

#R-1.8

"""
Una string s tiene tamano n, y la expresion s[k] se usa para el indice -n<=k<0.
Cual es equivalente al indice j>=0 de tal manera que s[j] haga referencia al 
mismo elemento.

R:
    [0,1,2,3]
    [-4,-3,-2,-1]
s[k]==s[j+n]
"""

#R-1.9
"""
Parametros para range y obtener los valores 50, 60, 70, 80
"""

print range(50,81,10)

#R-1.10

"""
Parametros para range y obtener los valores 8,6,4,2,0,-2,-4,-6,-8
"""

print range(-8,9,2)[::-1]

#R-1.11

"""
Demuestra la comprension de listas para obtener la lista:
    [1,2,4,8,16,32,64,128,256]
"""

print [2**e for e in range(9)]

#R-1.12

"""
Python incluye una funcion llamada choice(data) que regresa un elemento al azar 
de una lista no vacia. El modulo random incluye una funcion mas basica llamada 
randrange, esta regresa un valor al azar del rango dado. Implementa tu propia 
version de la funcion choice.
"""

def my_choice(data):
    from random import randrange   
    return data[randrange(len(data))]

