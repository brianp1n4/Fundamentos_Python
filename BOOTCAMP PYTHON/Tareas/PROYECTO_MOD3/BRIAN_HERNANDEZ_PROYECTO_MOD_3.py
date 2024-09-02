# Se importan librerias a usar en codigo
import numpy as np
import matplotlib.pyplot as plt


def galton_machine(levels,num_marbles):
    '''
    Funcion para simular el proceso de la maquina de galton
    Parametros: 
    levels (int): Niveles de maquina de galton, veces que tomara desicion la canica al caer hasta el fondo
    num_marbles (int): Numero de canicas que ingresaran en la maquina de galton
    Resultado de retorno:
    count (numpy array): Arreglo que almacena el resultado de cada canica
    '''

    count = np.zeros(levels + 1)

    # Ciclo for para simular el resultado de la caida de cada canica tomando desicion 12 veces de forma aleatoria
    for i in range (num_marbles):
        pos = 0
        for j in range(levels):
            if np.random.rand() > 0.5:
                pos += 1
        count[pos] += 1
    return count

def grafica_resultados(count):
    '''
    Presentar un histograma con los resultados de la simulacion de la maquina de galton
    Parametros:
    count (numpy array): Arreglo que almacena el resultado de cada canica
    '''
    plt.figure(figsize=(10,6))
    bars = plt.bar(range(len(count)),count,color ='blue',edgecolor='black')

    # Agregar etiquetas de valor en cada barra
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height,
                f'{int(height)}', ha='center', va='bottom')

    plt.xlabel('Distribución de canicas')
    plt.ylabel('Número de canicas')
    plt.title('Simulación de Maquina de Galton')
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Agregar una cuadrícula en el eje y
    plt.show()

# Se asignan parametros del ejercicio solicitado, niveles de la maquina de galton y numero de canicas
levels = 12 
num_marbles = 3000 
# Ejecutar simulaciond de la Maquina de Galton
results = galton_machine(levels,num_marbles)
# Mostrar grafica de resultados
grafica_resultados(results)
