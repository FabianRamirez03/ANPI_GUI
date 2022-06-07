from sympy import sympify
from sympy import diff
import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import *


def trapecio():
    return ["trapecio", 152]  # [Aproximacion, error]


def simpson():
    return ["simpson", 158]


def boole(f, a, b):
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

    func = sympify(f)

    primeraDerivada = diff(func)
    segundaDerivada = diff(primeraDerivada)
    terceraDerivada = diff(segundaDerivada)
    cuartaDerivada = diff(terceraDerivada)
    quintaDerivada = diff(cuartaDerivada)
    sextaDerivada = diff(quintaDerivada)

    h = (b - a) / 4
    aprox = (2 * h / 45) * (7 * func.subs({'x': a}).evalf() + 32 * func.subs({'x': a + h}).evalf() + 12 * func.subs(
        {'x': a + 2 * h}).evalf() + 32 * func.subs({'x': a + 3 * h}).evalf() + 7 * func.subs({'x': b}).evalf())

    eps = a;
    for i in range(a, b):
        if abs(sextaDerivada.subs({'x': i})) > abs(sextaDerivada.subs({'x': eps})):
            eps = i

    cota_error = ((8 / 945) * (h ** 7) * abs(sextaDerivada.subs({'x': eps}))).evalf()

    return [aprox, cota_error]


def trapecioCompuesto():
    return ["trapecioCompuesto", 255]


def simpsonCompuesto(f, a, b, m):
    func = sympify(f)
    primeraDerivada = diff(func)
    segundaDerivada = diff(primeraDerivada)
    terceraDerivada = diff(segundaDerivada)
    cuartaDerivada = diff(terceraDerivada)
    aprox = 0
    h = (b - a) / (m - 1)
    i = 1
    x = [];
    x.append(a)
    while i < m:
        x.append(a + (i * h));
        i += 1;
    i = 1
    sumaPar = 0
    sumaImpar = 0
    cantVars = len(x) - 1

    while i < cantVars:
        if i % 2 == 0:
            sumaPar += (func.subs({'x': x[i]})).evalf()
            i += 1
        else:
            sumaImpar += (func.subs({'x': x[i]})).evalf()
            i += 1
    aprox = ((h / 3) * (func.subs({'x': a}) + 2 * sumaPar + 4 * sumaImpar + func.subs({'x': b})))

    epsilon = a;
    for i in range(a, b):
        if abs(cuartaDerivada.subs({'x': i})) > abs(cuartaDerivada.subs({'x': epsilon})):
            epsilon = i
    error = ((((b - a) * (h ** 4)) / 180) * abs(cuartaDerivada.subs({'x': epsilon}))).evalf()
    return [aprox, error]


def gaussian(f, a, b, n):
    fx = sympify(f)
    [x, w] = np.polynomial.legendre.leggauss(n)

    values = [
        wi * fx.subs({'x': ((b - a) / 2) * xi + ((a + b) / 2)}).evalf()
        for (xi, wi) in zip(x, w)
    ]
    resultado = ((b - a) / 2) * sum(values)
    return [resultado, 'N/A']
