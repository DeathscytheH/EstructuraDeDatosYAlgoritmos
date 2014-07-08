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