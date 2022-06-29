# Pranit Zope
# AE20B046
# AS2101 : Assignment 03

import numpy as np
import matplotlib.pyplot as plt

# importing necessary libraries


arr=np.zeros(1001)  # arr will be our array that will have the least prime factor for each number,i.e arr[n] = least prime factor of n

for i in range(1001):
    arr[i]=i
# we first give each element of the array its own value

for i in range(2,1001):
    if(arr[i]==i):
        j=i*i
        while(j<1001):
            if(arr[j]==j):
                arr[j]=i
            j=j+i
# here, we check if our assumption was correct, if not, we correct it and so on, finally we get the array of the least prime factors of numbers


def primefactor(n):
    """A function to return all the prime factors of a given number 'n'.

    Args:
        n (int): The number of which prime factors you want

    Returns:
        factors [array]: An array consisting of all the prime factors of the number
    """

    factors=[]            
    while(n!=1):
        factors.append(arr[int(n)])
        n=n//arr[int(n)]
    return factors



pfct=[] # pfct is an array which will store the prime factors of any number in the form of another array
# eg ; pfct[12]=[2,2,3]

pfct.append(0)
pfct.append(0)
# since 0 and 1 have no prime factors, we will simply write 0 in their place


for i in range(2,1001):
    pfct.append(primefactor(i))
# and pfct = [0],[1],[2],[3],[2,2],[5],[2,3] and so on

for i in range(2,1001):
    print("Prime factors of",i,"are",end=" ")
    for x in pfct[i]:
        print(x,end=",")
    print("\n")
# We print the prime factors of all numbers

pfreq=np.zeros(1001) # pfreq will be the array that contains the frequency of each prime number,  that his how many times it occurs in the prime factorisation of all numbers

for i in range(2,1001):
    for j in pfct[i]:
        pfreq[int(j)]=pfreq[int(j)]+1

A=[]
for i in range(2,1001):
    if(arr[i]==i):
        A.append(int(i))

B=[]
for i in A:
    B.append(int(pfreq[i]))

# We make 2 arrays and store the values of primes and thier frequencies for further use

for i in range(0,len(A)):
    print("Frequency of",A[i],"is:",B[i])

def plot(start,end):
    """A function to plot the frequency distribution plot of prime numbers between a "start" value and "end" value.

    Args:
        start (int): The value at which the plotting needs to begin.
        end (int): The value at which the plotting needs to end.
    """
    x=[]
    for i in A:
        if(i>=start and i<=end):
            x.append(int(i))
        

    y=[]
    for i in x:
        y.append(int(pfreq[i]))
    
    plt.figure()
    plt.grid(linestyle='--')
    plt.title("Frequency distribution of prime numbers form "+str(start)+" to "+str(end))
    plt.xlabel('X (Prime Numbers)')
    plt.ylabel('Y (Frequency)')

    plt.bar(x,y,color='blue',width=3)

    plt.savefig("fig_"+str(start)+"_"+str(end)+".png")
    plt.clf()

# finally, we will plot the required plots
plot(2,1000)
plot(2,200)
plot(201,1000)


