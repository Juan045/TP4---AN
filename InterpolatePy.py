import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# Implementar generador de matriz
# a partir de los datos proporcionados
def generarMatriz(datos_x,datos_y):  
    N = datos_x.size
    
    matriz = np.zeros((N, N))
    for i in range(N):
        temp = np.zeros(N)
        for j in range(N):
            temp[j] = datos_x[i]**(((N-1) - j) % N)
        matriz[i,:] = temp

    return matriz



# Implementar solucionador de matriz
# retornar el vector resultante (coeficientes)
def buscarCoeficientes(matriz, datos_y):
    coeficientes = np.linalg.solve(matriz, datos_y)
    return coeficientes

# ------------------------------- #
# Funciones para el ejercicio 1.b
# ------------------------------- #
'''
    Funcion que permite calcular el polinomio de interpolacion de Newton
    recibiendo como parametros los coeficientes 'a' calculados
    y un vector x opcional
'''
# Crear el polinomio de Newton
def polinomio_newton(coeficientes, datos_x):
    def polinomio(x):
        resultado = coeficientes[0]
        terminos = np.ones_like(x)
        
        for i in range(1, len(coeficientes)):
            terminos *= (x - datos_x[i - 1])
            resultado += coeficientes[i] * terminos
        
        return resultado
    
    return polinomio

'''
    Inicializar matriz con las condiciones iniciales 
    para realizar las diferencias divididas
'''
def inicializarMatrizDiferenciasDivididas(N, datos_x, datos_y):
    matriz = np.zeros((N, N+1))
    matriz[:,0] = datos_x
    matriz[:,1] = datos_y
    
    return matriz

# busqueda de coeficientes utilizando diferencias divididas    
def calcularCoeficientesDiferenciasDivididas(datos_x, datos_y):
    # obtener la cantidad de datos
    N = datos_x.size
    
    # inicializar matriz de diferencias dividadas
    matriz = inicializarMatrizDiferenciasDivididas(N, datos_x, datos_y)
    
    # inicializar vector de coeficientes
    coeficientes = np.zeros(N)
    coeficientes[0] = datos_y[0] 
    calculados = 1 
            
    # calcular los coeficientes utilizando el metodo de las diferencias divididas
    for c in range(2, N + 1):
        for f in range(c - 1, N):
            matriz[f, c] = (matriz[f, c-1] - matriz[f - 1, c - 1]) / (matriz[f, 0] - matriz[f - c + 1, 0])
            if (f == c-1):
                coeficientes[calculados] = matriz[f, c]
                calculados += 1
        
    return coeficientes

# =============================== #

def Spline(datos_x, datos_y):
    tck = interpolate.splrep(datos_x, datos_y, s=0)
    
    x_nuevo = np.linspace(datos_x[0],datos_x[datos_x.size - 1], num=500)
    y_nuevo = interpolate.splev(x_nuevo, tck, der=0)
    
    return x_nuevo, y_nuevo, tck