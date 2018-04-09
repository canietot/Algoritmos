import numpy as np
from time import time
import matplotlib.pyplot as plt

min = 20
max = 51
retry = 10

tMeans = [0.0] * (max - min)

for T in range(min, max):
    # Creacion de la matriz de 1s y 2s
    matriz1 = np.ones((T, T))
    matriz2 = np.ones((T, T)) * 2
    matriz3 = np.zeros((T, T))

    # Multiplicacion de matrices
    tMean = 0.0
    oper = ((T * T * T) + (T * T * (T - 1)))
    for _ in range(retry):
        t0 = time()
        matriz3 = matriz1 * matriz2
        tf = time()
        tt = (tf - t0)
        tMean += (tt / oper)

    # Tiempo promedio i
    tMeans[T - min] = (tMean / retry)

# Tiempo promedio total
tMean = ((sum(tMeans)) / (len(tMeans)))

print(tMeans)
print("El tiempo promedio por instruccion es: ", tMean)
