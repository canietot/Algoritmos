import random
def insertionsort(A):
    #we start loop at second element (index 1) since the first item is already sorted
    look=0
    swap=0
    for j in range(1,len(A)):
        key = A[j] #The next item we are going to insert into the sorted section of the array
        i = j-1 #the last item we are going to compare to
        look = look+1
        #now we keep moving the key back as long as it is smaller than the last item in the array
        while (i > -1) and key < A[i]: #if i == -1 means that this key belongs at the start
            A[i+1]=A[i] #move the last object compared one step ahead to make room for key
            swap= swap +1
            i=i-1 #observe the next item for next time.
        #okay i is not greater than key means key belongs at i+1
        A[i+1] = key
    print ("swaps"),swap ,("looks"), look
    return A
    
n= input()
s= random.sample(range(100), n)
s = list (s)
x= list (permutations(s, n))
f=n
fac=1
while f > 0:
    fac= fac*f
    f= f-1
for i in range (0,fac):
    print x[i]
    t = list (x[i])
    insertionsort(t)
    print(t)
    print ("\n")   
