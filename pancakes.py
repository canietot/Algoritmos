import numpy as np

stepsToSolve = 100000000
worstCase = 0
worstArray = []
worstFlips = []
isPrintable = False
isMax = False


def printFlips(arr, flips, steps):
    global worstCase
    global worstArray
    global worstFlips
    global isPrintable
    global isMax

    if len(steps) > worstCase:
        worstCase = len(steps)
        worstArray = arr
        worstFlips = flips

    if isMax:
        if len(steps) == len(arr):
            for i in range(len(arr)):
                print(arr[i], end="")
            print("     ", end="")
            for i in range(len(steps)):
                print(steps[i], end="")
            print("     ", flips + 1)

    if isPrintable:
        for i in range(len(arr)):
            print(arr[i], end="")
        print("     ", end="")
        for i in range(len(steps)):
            print(steps[i], end="")
        print("     ", flips + 1)


def flips(arr, arrFlips, max, last, sortedArr, steps):
    global stepsToSolve
    if np.array_equal(sortedArr, arr):
        if arrFlips < stepsToSolve: stepsToSolve = arrFlips

    if arrFlips != max:
        for i in range(1, len(arr)):
            if i != last:
                temp1 = list(reversed(arr[0:i + 1]))
                temp2 = []
                if i < len(arr) - 1: temp2 = arr[i + 1:len(arr)]
                temp1.extend(temp2)
                tempSteps = steps[:]
                tempSteps.append(i)
                printFlips(temp1, arrFlips, tempSteps)
                flips(temp1, arrFlips + 1, max, i, sortedArr, tempSteps)

def fun(n, c):
    global isPrintable
    global isMax
    global worstCase
    global worstArray

    arr = range(n)
    sortedArr = sorted(arr)
    if c == 0:
        isPrintable = False
        isMax = False
        flips(arr, 0, len(arr), 0, sortedArr, [])
        print("Worst Case: ", worstCase, " Worst Flips: ", worstArray)
    if c == 1:
        isMax = True
        isPrintable = False
        flips(arr, 0, len(arr), 0, sortedArr, [])
        print("Worst Case: ", worstCase)
    if c == 2:
        isPrintable = True
        isMax = False
        flips(arr, 0, len(arr), 0, sortedArr, [])
        print("Worst Case: ", worstCase)

values = [int(x) for x in input().split()]
# arr = np.array(values)
# sortedArr = sorted(arr)
n, c = values[0], values[1]
fun(n, c)
# flips(arr,0,len(arr),0,sortedArr,[])
# print("Steps necesarry to solve: ",stepsToSolve)