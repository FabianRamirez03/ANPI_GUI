import parte1_p2 as metodos

# Ejemplo numerico: metodo del trapecio
funcion = "exp(x)*x"
intervalo = (1,3)
resultado = metodos.trapecio(funcion, intervalo)
print("________________________ \n")
print("Aproximación por el método del trapecio de la integral de:")
print("Función: "+funcion+" en el intervalo: ["+str(intervalo[0])+", "+str(intervalo[1])+"]")
print("Aproximación: "+str(resultado[0])+", error: "+str(resultado[1]))
print("________________________ \n")

# Ejemplo numerico: metodo del trapecio compuesto
funcion = "exp(x)*x"
intervalo = (1,3)
puntos = 100
resultado = metodos.trapecioCompuesto(funcion, intervalo, puntos)
print("________________________ \n")
print("Aproximación por el método del trapecio compuesto con "+str(puntos)+" puntos de la integral de:")
print("Función: "+funcion+" en el intervalo: ["+str(intervalo[0])+", "+str(intervalo[1])+"]")
print("Aproximación: "+str(resultado[0])+", error: "+str(resultado[1]))
print("________________________ \n")


# Ejemplo numerico: metodo de Simpson
funcion = "exp(x)*x"
intervalo = (1,3)
resultado = metodos.simpson(funcion, intervalo)
print("________________________ \n")
print("Aproximación por el método de Simpson de la integral de:")
print("Función: "+funcion+" en el intervalo: ["+str(intervalo[0])+", "+str(intervalo[1])+"]")
print("Aproximación: "+str(resultado[0])+", error: "+str(resultado[1]))
print("________________________ \n")


# Ejemplo numerico: metodo de Simpson compuesto
funcion = "exp(x)*x"
intervalo = (1,3)
puntos = 100
resultado = metodos.simpsonCompuesto(funcion, intervalo, puntos)
print("________________________ \n")
print("Aproximación por el método del Simpson compuesto con "+str(puntos)+" puntos de la integral de:")
print("Función: "+funcion+" en el intervalo: ["+str(intervalo[0])+", "+str(intervalo[1])+"]")
print("Aproximación: "+str(resultado[0])+", error: "+str(resultado[1]))
print("________________________ \n")



# Ejemplo numerico: metodo de Boole
funcion = "exp(x)*x"
intervalo = (1,3)
resultado = metodos.boole(funcion, intervalo)
print("________________________ \n")
print("Aproximación por el método de Boole de la integral de:")
print("Función: "+funcion+" en el intervalo: ["+str(intervalo[0])+", "+str(intervalo[1])+"]")
print("Aproximación: "+str(resultado[0])+", error: "+str(resultado[1]))
print("________________________ \n")

# Ejemplo numerico: metodo de Gaussian
funcion = "exp(x)*x"
intervalo = (1,3)
puntos = 100
resultado = metodos.gaussian(funcion, intervalo,puntos)
print("________________________ \n")
print("Aproximación por el método de cuadraturas Gaussianas con "+str(puntos)+" puntos de la integral de:")
print("Función: "+funcion+" en el intervalo: ["+str(intervalo[0])+", "+str(intervalo[1])+"]")
print("Aproximación: "+str(resultado[0])+", error: "+str(resultado[1]))
print("________________________ \n")

