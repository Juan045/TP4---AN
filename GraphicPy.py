import matplotlib.pyplot as plt

def graficarInterpolacion(datos_x, datos_y, abscisa, ordenadas):
    plt.plot(datos_x,datos_y, 'o', label='puntos originales')
    plt.plot(abscisa, ordenadas, color='orange',label='polinomio P(x)')
    plt.title('Ajuste de datos')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)