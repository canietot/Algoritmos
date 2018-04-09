import matplotlib.pyplot as plt
import time
def fibonacci1(n):
    t0 = time.clock()
    if n==0 :
        return 0
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    tf =time.clock()
    return (tf-t0)


def printTime(start, end, jump, retry):
    times = [0.0] * ((end - start) / jump)
    axisx = (range(start, end, jump))

    for i in range(start, end, jump):
        tMean = 0.0
        for _ in range(retry):
            tMean += fibonacci1(i)
        times[(i - start) / jump] = (tMean / retry)

    plt.plot(axisx, times);
    plt.xlabel('N')
    plt.ylabel('Tiempo')
    plt.title('Tiempo de ejecucion de la funcion Fibonacci en funcion de N');

printTime(0,1500,1,20)

printTime(0,100000,1000,10)
