from sympy import sympify
from sympy import diff
import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy import *

'''
Funcion para calcular una aproximacion de una integral mediante el metodo del trapecio
Entradas: 
    f : la funcion a integrar en string   
    intervalo : tupla del intervalo de integracion
Salidas:
    I: aproximacion del resultado de la integracion
    er: cota de error de la aproximacion
'''

def trapecio(f, intervalo):
    try:
        x = symbols("x")
        f = sympify(f) #f como funcion simbolica
        fn = lambdify(x, f) # f como funcion numerica

        # Se establecen los valores iniciales
        a = intervalo[0]
        b = intervalo[1]
        h = b - a

        #Calculo de la aproximacion
        I = (fn(a)+fn(b))*h/2

        # Calculo del error
        df2 = diff(f, x, 2)  #Segunda derivada de f
        alpha_max = maximum(df2, x, Interval(a, b)) 
        er = float(((h**3)*alpha_max)/12)
        return [I, er]

    except:
        return [I, float('inf')]




'''
Funcion para calcular una aproximacion de una integral mediante el metodo de Simpson
Entradas: 
    f : la funcion a integrar en string   
    intervalo : tupla del intervalo de integracion
Salidas:
    I: aproximacion del resultado de la integracion
    er: cota de error de la aproximacion
'''
def simpson (f, intervalo):
    try:
        x = symbols("x")
        f = sympify(f) #f como funcion simbolica
        fn = lambdify(x, f) # f como funcion numerica

        # Se establecen los valores iniciales
        a = intervalo[0]
        b = intervalo[1]
        h = b - a

        #Calculo de la aproximacion
        I=((b-a)/6)*(fn(a)+4*fn((a+b)/2)+fn(b))

        # Calculo del error
        df4 = diff(f,x,4)  #Cuarta derivada de f
        alpha_max = maximum(df4, x, Interval(a, b)) 
        er = float(((h**5)*alpha_max)/2880)

        return [I, er]

    except:
        return [I, float('inf')]
    
"""
Esta función aproxima el valor de la integral de una función f(x), utilizando la Regla de Boole.

Sintaxis: boole(f,a,b)

Parámetros Iniciales: 
    f = representa a la función f(x) a integrar
    a = es el valor inicial del intervalo a integrar
    b = es el valor final del intervalo a integrar
            
Parámetros de Salida: 
    aprox = aproximación del valor de la integral de la función f
    cota_error = error máximo posible 
            
"""

def boole(f, intervalo):
    try:
        a = intervalo[0]
        b = intervalo[1]
        x = symbols("x")
        func = sympify(f)
        
        # Se calcula la aproximacion de la integral
        h = (b - a) / 4
        aprox = (2 * h / 45) * (7 * func.subs({'x': a}).evalf() + 32 * func.subs({'x': a + h}).evalf() + 12 * func.subs(
            {'x': a + 2 * h}).evalf() + 32 * func.subs({'x': a + 3 * h}).evalf() + 7 * func.subs({'x': b}).evalf())

        # Calculo del error
        # Se calcula la sexta derivada de f
        df6 = sp.diff(func, x, 6)
        alpha_max = maximum(df6, x, Interval(a, b)) 
        cota_error = float((8 / 945) * (h ** 7) * alpha_max)

        return [aprox, cota_error]

    except:
        return [aprox, float('inf')]





'''
Funcion para calcular una aproximacion de una integral mediante el metodo del trapecio
Entradas: 
    f: la funcion a integrar en string   
    intervalo: tupla del intervalo de integracion
    n: numero de puntos en que se divide el intervalo de integracion
Salidas:
    I: aproximacion del resultado de la integracion
    er: cota de error de la aproximacion
'''

def trapecioCompuesto(f, intervalo, n):
    try:
        # Se establecen los valores iniciales
        a = intervalo[0]
        b = intervalo[1]
        xv = np.linspace(a, b, num=n)
        I = 0
        er = 0
        # Se calcula la integracion
        for i in range(len(xv)-1):
            result = trapecio(f,(xv[i],xv[i+1]))
            I += result[0]
            er += result[1] 
        return [I, er]

    except:
        return [I, float('inf')]


'''
Funcion para calcular una aproximacion de una integral mediante el metodo de Simpson compuesto
Entradas: 
    f: la funcion a integrar en string   
    a = es el valor inicial del intervalo a integrar
    b = es el valor final del intervalo a integrar
    n: numero de puntos en que se divide el intervalo de integracion
Salidas:
    I: aproximacion del resultado de la integracion
    er: cota de error de la aproximacion
'''

def simpsonCompuesto(f,intervalo, n):
    try:
        a = intervalo[0]
        b = intervalo[1]
        # Se establecen los valores iniciales
        xv = np.linspace(a, b, num=n)
        
        I = 0
        er = 0
        # Se calcula la integracion
        for i in range(len(xv)-1):
            result = simpson(f,(xv[i],xv[i+1]))
            I += result[0]
            er += result[1] 
        return (I, er)

    except:
        return [I, float('inf')]


'''
Funcion para calcular una aproximacion de una integral por medio de cuadraturas Gaussianas
Entradas: 
    f: la funcion a integrar en string   
    a = es el valor inicial del intervalo a integrar
    b = es el valor final del intervalo a integrar
    n: numero de puntos en que se divide el intervalo de integracion
Salidas:
    I: aproximacion del resultado de la integracion
    er: cota de error de la aproximacion
'''

def gaussian(f, intervalo , n):
    try:
        # Se establecen los valores iniciales
        a = intervalo[0]
        b = intervalo[1]
        fx = sympify(f)
        [x, w] = np.polynomial.legendre.leggauss(n)

        values = [
            wi * fx.subs({'x': ((b - a) / 2) * xi + ((a + b) / 2)}).evalf()
            for (xi, wi) in zip(x, w)
        ]
        resultado = ((b - a) / 2) * sum(values)
        return [resultado, 'N/A']

    except:
        return [resultado, float('inf')]




