import VandermondePy as vpy
import matplotlib.pyplot as plt
import numpy as np

def p(COEFICIENTES,x): 
    N = COEFICIENTES.size
    res = 0
    for i in range(N):
        cx = x ** (((N-1) - i) % N)
        coef = (COEFICIENTES[i])
        res += coef * cx
    return res
# Distancia
DATOS_X = np.array([0,50,100,150,200,250,300])
# Altura
DATOS_Y = np.array([10,60,55,70,40,50,30])

# EJERCICIO 1
## Generar matriz de Vandermonde con los puntos.
matriz = vpy.generarMatriz(DATOS_X, DATOS_Y)
""" print(matriz) """
### Encontrar la solucion de la matriz y guardar los coeficientes.
### Utilizar los coeficientes para construir el polinomio.
coeficientes = vpy.buscarCoeficientes(matriz, DATOS_Y)
polinomio = np.poly1d(coeficientes)
print(polinomio)

rango_x = np.linspace(DATOS_X[0],DATOS_X[DATOS_X.size - 1], num=500)
print(polinomio([0,50]), "mi polinomio: ", p(coeficientes, 50))
### Graficar la curva encontrada.
plt.plot(DATOS_X,DATOS_Y, 'o', label='puntos originales')
plt.plot(rango_x,polinomio(rango_x), color='orange',label='polinomio P(x)')
plt.title('Ajuste de datos')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
