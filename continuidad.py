from sympy import *
from sympy import Interval, Symbol, pi
from sympy.calculus.util import continuous_domain

'''
Funcion para verificar la continuidad de una funcion en un intervalo
Entradas:
    f: funcion por verificar
    intervalo: tupla que indica el intervalo en el que se verificara la continuidad
Salida:
    result: true si la funcion es continua en el intervalo
            false si no lo es
'''

def esContinua(f, intervalo):
    x = symbols("x")
    fn = sympify(f) #f como funcion simbolica
    intvl = Interval(intervalo[0], intervalo[1])

    # Se verifica el intervalo en el que f es continua en el intervalo de 
    # integracion deseado
    I1 = continuous_domain(fn, x, intvl)

    # Se verifica si son el mismo intervalo
    result = intvl == I1

    return result
    

# Ejemplo Numerico
funcion = "tan(x)"
intervalo = (0,pi)
resultado = esContinua(funcion, intervalo)
print(resultado)