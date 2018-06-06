import numpy as np

stepsToSolve = 100000000
worstCase = 0
worstArray = []
worstFlips = []
isPrintable = False
isMax = False

np.set_printoptions(precision=0)


def printFlips(arr, flips, steps, max):
    global worstCase
    global worstArray
    global worstFlips
    global isPrintable
    global isMax

    if len(steps) / (2 * len(arr)) > worstCase:
        worstCase = len(steps)
        worstArray = arr
        worstFlips = flips

    if isMax:
        if len(steps) / (2 * len(arr)) == worstCase:
            for i in range(len(arr)):
                print(arr[i], end="")
            print("     ", end="")
            print(steps, end=" ")
            print("     ", flips + 1)

    if isPrintable:
        for i in range(len(arr)):
            print(arr[i], end="")
        print("     ", end="")
        print(steps, end=" ")
        print("     ", flips + 1)


def flips(arr, arrFlips, max, firstSpatula, secondSpatula, sortedArr, steps):
    global stepsToSolve
    if np.array_equal(sortedArr, arr):
        if arrFlips < stepsToSolve: stepsToSolve = arrFlips

    if arrFlips != max:
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if j != secondSpatula:
                    temp1 = list(reversed(arr[i:j + 1]))
                    temp2, temp3 = [], []
                    if j < len(arr) - 1: temp2 = arr[j + 1:len(arr)]
                    temp1.extend(temp2)
                    temp1 = np.array(temp1)
                    if i > 0:
                        temp3 = arr[0:i]
                        temp1 = np.concatenate((temp3, temp1))
                    tempSteps = np.append(steps, [int(i), int(j)])
                    printFlips(temp1, arrFlips, tempSteps, max)
                    flips(temp1, arrFlips + 1, max, i, j, sortedArr, tempSteps)


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
        flips(arr, 0, len(arr), -1, -1, sortedArr, [[]])
        print("Worst Case: ", worstCase, end=" Worst Flips: ")
        for i in range(len(worstArray)):
            print(worstArray[i], end=" ")
    if c == 1:
        isMax = True
        isPrintable = False
        flips(arr, 0, len(arr), -1, -1, sortedArr, [[]])
        print("Worst Case: ", worstCase)
    if c == 2:
        isPrintable = True
        isMax = False
        flips(arr, 0, len(arr), -1, -1, sortedArr, [[]])
        print("Worst Case: ", worstCase)


values = [int(x) for x in input().split()]
# arr = np.array(values)
# sortedArr = sorted(arr)
n, c = values[0], values[1]
fun(n, c)
# flips(arr,0,len(arr),0,sortedArr,[])
# print("Steps necesarry to solve: ",stepsToSolve)