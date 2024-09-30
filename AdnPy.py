import numpy as np
import random

polinomioG = None
distancia_min = 10
distancia_max = 20

'''
    CORREGIR PROBLEMAS:
        - crear_poste genera postes fuera del rango (mal)
        - a veces aparece una cantidad de material negativo (no investigado)
'''


def crear_poste(individuo, indice):
    '''
        si es el primer poste 10 <= x[i+1] - x[i] <= 20
        si es el ultimo poste 10 <= x[i] - x[i-1] <= 20
        caso contrario se hacen ambas comparaciones
    '''
    nuevo = 0
    if(indice == 0):
        nuevo += np.random.uniform(0, individuo[indice+1]-distancia_min)
            
    elif(indice == 19):
        nuevo += individuo[indice-1] + np.random.uniform(distancia_min, distancia_max)
    else:
        nuevo += individuo[indice-1] + np.random.uniform(distancia_min, individuo[indice+1]-distancia_min)

    return nuevo

def crear_individuo():
    
    maximo = 300
    
    lista = np.zeros(20)
    posicion_x = np.random.uniform(0, distancia_max)
    lista[0] = posicion_x

    for i in range(1,20):
        posicion_x = posicion_x + np.random.uniform(distancia_min, distancia_max)
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

# se seleccionan los individuos que mejor se adaptan al problema
def seleccionar_aptos(poblacion):
    
    puntuacion = [(evaluar(i), i) for i in poblacion]
    puntuacion = [i[1] for i in sorted(puntuacion)]
    
    aptos = puntuacion[len(puntuacion) - seleccionar:]
    return aptos
    
# reproduce los individuos para generar hijos aptos
def reproduccion(poblacion, aptos):
    indice = 0
    padre = []
    # MIRAR ACA PORQUE PUEDE ROMPER LA RESTRICCION ENTRE 10 Y 20
    for i in range(len(poblacion)):
        indice = np.random.randint(1, 19)    
        padre = random.sample(aptos, 2)
        
        poblacion[i][:indice] = padre[0][:indice]
        poblacion[i][indice:] = padre[1][indice:]
    
    return poblacion

# recibe una poblacion ya reproducida para mutarla si ocurriese
def mutacion(poblacion):
    for i in range(len(poblacion)):
        if random.random() <= probabilidadMutacion:
            indice = np.random.randint(1, 19)
            nuevoPoste = crear_poste(poblacion[i], indice)
            print(f"<<--El nuevo poste es: {nuevoPoste}-->>")
            poblacion[i][indice] = nuevoPoste
    return poblacion

def run():
    global poblacion
    poblacion = crear_poblacion(individuos)
    
    for i in range(generaciones):
        """ print('___________')
        print('Generacion: ', i)
        print('Poblacion', poblacion)
        print() """
    aptos = seleccionar_aptos(poblacion)
    poblacion = reproduccion(poblacion, aptos)
    poblacion = mutacion(poblacion)

def main(polinomio):
    global generaciones
    generaciones = 100
    
    global probabilidadMutacion
    probabilidadMutacion = 0.02
    
    global seleccionar
    seleccionar = 10
    
    global individuos
    individuos = 50
    
    global polinomioG
    polinomioG = polinomio
    
    run()
    return poblacion
    
    
    
    

        