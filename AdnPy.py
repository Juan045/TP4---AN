import numpy as np
import random

polinomioG = None
distancia_min = 10
distancia_max = 20

def crear_individuo():
    
    maximo = 300
    
    lista = np.zeros(20)
    generador_aleatorio = np.random.default_rng()
    posicion_x = generador_aleatorio.uniform(0, distancia_max)
    lista[0] = posicion_x

    for i in range(1,20):
        posicion_x = posicion_x + generador_aleatorio.uniform(distancia_min, distancia_max)
        lista[i] = posicion_x

    return lista

def crear_poblacion(tam):

    poblacion = []
    for i in range(tam):
        
        individuo = crear_individuo()
        while individuo[19] > 300:
            individuo = crear_individuo()

        poblacion.append(individuo)

    return poblacion
    
# evaluar que tan apto es un individuo para la resolucion del problema
def evaluar(individuo):
    y = polinomioG(individuo)
    score = sum(y)
    return score


def verificar_limites(hijo):
    for i in range(1, len(hijo) - 1):
        if hijo[i] - hijo[i-1] < 10:
            hijo[i] = hijo[i-1] + 10
        elif hijo[i] - hijo[i-1] > 20:
            hijo[i] = hijo[i-1] + 20
        
        if hijo[i] + 10 > hijo[i + 1]:
            hijo[i + 1] = hijo[i] + 10
        elif hijo[i] + 20 < hijo[i + 1]:
            hijo[i + 1] = hijo[i] + 20
    return hijo

def cruce(parent1, parent2):
    point = np.random.randint(1, len(parent1) - 1)
    hijo = np.concatenate((parent1[:point], parent2[point:]))
    return verificar_limites(hijo)


def seleccionar_aptos(poblacion):
    puntuacion = [(evaluar(i), i) for i in poblacion]
    puntuacion = [i[1] for i in sorted(puntuacion)]

    aptos = puntuacion[len(puntuacion) - seleccionar:]
    return aptos


def mutacion(individual, mutation_rate=0.1):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = np.random.randint(10, 21)
    return verificar_limites(individual)

def reproducir(poblacion):
    nueva_poblacion = []
    aptos = seleccionar_aptos(poblacion)
    for _ in range(individuos // 2):
        padre1, padre2 = random.sample(aptos, 2)
        hijo = cruce(padre1, padre2)
        hijo = mutacion(hijo, probabilidadMutacion)
        nueva_poblacion.append(hijo)
    return nueva_poblacion


def run():
    global poblacion
    poblacion = crear_poblacion(individuos)
    poblacion_mat = [(sum(polinomioG(i)), i) for i in poblacion]
    poblacion_mat = sorted(poblacion_mat,key=lambda x: x[0])
    for i in range(generaciones):
        poblacion_temp = reproducir(poblacion) 
        poblacion_temp_mat = [(sum(polinomioG(i)), i) for i in poblacion_temp]
        poblacion_temp_mat = sorted(poblacion_temp_mat, key=lambda x: x[0])
        if poblacion_temp_mat[0][0] < poblacion_mat[0][0]:
            poblacion = poblacion_temp
            poblacion_mat = poblacion_temp_mat 


def main(polinomio):
    global generaciones
    generaciones = 100
    
    global probabilidadMutacion
    probabilidadMutacion = 0.01

    global seleccionar
    seleccionar = 50
    
    global individuos
    individuos = 100
    
    global polinomioG
    polinomioG = polinomio
    
    run()

    return poblacion
    
