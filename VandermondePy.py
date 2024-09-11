import numpy as np
# Implementar generador de matriz
# a partir de los datos proporcionados
def generarMatriz(datos_x,datos_y):
    if (datos_x.size != datos_y.size):
        return print("Exception: ERROR, el tamaño de los vectores brindados son distintos")
    else:
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