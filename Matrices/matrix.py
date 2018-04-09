from time import time

min = 20
max = 51
retry = 10

tMeans = [0] * (max - min)
xAxis = range(min, max)

    for T in range(min, max):
        matriz1 = []
        matriz2 = []
        matriz3 = []

        for i in range(T):
            matriz1.append([])
            matriz2.append([])
            matriz3.append([])
            for j in range(T):
                matriz1[i].append(1)
                matriz2[i].append(2)
                matriz3[i].append(0)

        tMean = 0.0
        for _ in range(retry):
            t0 = time();
            for i in range(T):
                for j in range(T):
                    for k in range(T):
                        matriz3[i][j] += matriz1[i][k] * matriz2[k][j]
            tf = time();
            tt = (tf - t0);
            oper = ((T * T * T) + (T * T * (T - 1)))
            tMean += (tt / oper)

        tMeans[T - min] = (tMean / retry)


print("El tiempo promedio por instruccion es: ", ((sum(tMeans)) / (len(tMeans))))
