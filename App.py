import InterpolatePy as ipy
import matplotlib.pyplot as plt
import GraphicPy as gpy
import numpy as np
from scipy import interpolate

def p(COEFICIENTES,x): 
    N = COEFICIENTES.size
    res = 0
    for i in range(N):
        cx = x ** (((N-1) - i) % N)
        coef = (COEFICIENTES[i])
        res += coef * cx
    return res

# variables globales
DATOS_X = np.array([0.,50.,100.,150.,200.,250.,300.]) # distancia
DATOS_Y = np.array([10.,60.,55.,70.,40.,50.,30.]) # altura
# polinomios
polinomioA = None
polinomioB = None
tck = None
# ----------------------- #
# ---| EJERCICIO 1.a |--- #
# ----------------------- #
def inciso_1a():
    ## Generar matriz de Vandermonde con los puntos.
    #### INICIAR TIEMPO
    matriz = ipy.generarMatriz(DATOS_X, DATOS_Y)

    ### Encontrar la solucion de la matriz y guardar los coeficientes.
    ### Utilizar los coeficientes para construir el polinomio.
    coeficientes = ipy.buscarCoeficientes(matriz, DATOS_Y)
    #### FINALIZAR TIEMPO
    global polinomioA
    polinomioA = np.poly1d(coeficientes)
    print(polinomioA)


    abscisas = np.linspace(DATOS_X[0],DATOS_X[DATOS_X.size - 1], num=500)
    ordenadas = polinomioA(abscisas)

    print(polinomioA(50.), "mi polinomio: ", p(coeficientes, 50.))

    ### Graficar la curva encontrada.
    gpy.graficarInterpolacion(DATOS_X,DATOS_Y, abscisas, ordenadas)
    plt.show()

# ----------------------- #
# ---| EJERCICIO 1.b |--- #
# ----------------------- # 
def inciso_1b():
    ### calculo de los coeficientes utilizando diferencias divididadas.
    #### INICIAR TIEMPO
    global polinomioB
    coeficientes = ipy.calcularCoeficientesDiferenciasDivididas(DATOS_X, DATOS_Y)
    polinomioB = ipy.polinomio_newton(coeficientes, DATOS_X)
    #### FINALIZAR TIEMPO

    # calcular abscisas y ordenadas para graficar
    abscisas = np.linspace(DATOS_X[0],DATOS_X[DATOS_X.size - 1], num=500)
    ordenadas = polinomioB(abscisas)

    # graficar resultados
    gpy.graficarInterpolacion(DATOS_X,DATOS_Y, abscisas, ordenadas)
    plt.show()

# ----------------------- #
# ---| EJERCICIO 1.c |--- #
# ----------------------- # 
def inciso_1c():
    #### INICIAR TIEMPO
    global tck
    abscisas, ordenadas, tck = ipy.Spline(DATOS_X, DATOS_Y)
    #### FINALIZAR TIEMPO

    gpy.graficarInterpolacion(DATOS_X,DATOS_Y, abscisas, ordenadas)
    plt.show()

# ----------------------- #
# ---| EJERCICIO 1.e |--- #
# ----------------------- # 

def inciso_1e():
    print("A 75 metros: ", polinomioA(75.), " a 255 metros: ", polinomioA(255.))
    print("A 75 metros: ", interpolate.splev(75., tck, der=0),  " a 255 metros: ", interpolate.splev(255., tck, der=0))

# ----------------------- #
# ---| EJERCICIO 2.a |--- #
# ----------------------- # 

### Armar funcion a minimizar
### Generar vector X y vector Y


# ----------------------- #
# --------| FIN |-------- #
# ----------------------- # 
def main():
    # ejecutar inciso 1.a
    respuesta = input(f"Ejecutar inciso 1.a (s/n): ").strip().lower()
    if respuesta == 's':
        inciso_1a()
        
    # ejecutar inciso 1.b
    respuesta = input(f"Ejecutar inciso 1.b (s/n): ").strip().lower()
    if respuesta == 's':
        inciso_1b()
        
    # ejecutar inciso 1.c
    respuesta = input(f"Ejecutar inciso 1.c (s/n): ").strip().lower()
    if respuesta == 's':
        inciso_1c()
        
    # ejecutar inciso 1.e
    respuesta = input(f"Ejecutar inciso 1.e (s/n): ").strip().lower()
    if respuesta == 's':
        inciso_1e()
    
    # ejecutar inciso 2.a

if __name__ == "__main__":
    main()