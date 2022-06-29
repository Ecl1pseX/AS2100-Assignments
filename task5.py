#!/usr/bin/env/python3.9
# Pranit Zope
# AE20B046
# Task 05 : Integrals using Quadrature
# Main file

import numpy as np
from matplotlib import pyplot as plt
import methods
import regression

Area=1  #we know that area under sine curve is one

total=[]
k=2
while(k<103):
    total.append(k)
    k=k+5

left=[]
right=[]
mid=[]
trapez=[]

for i in total:
    left.append(abs(Area-methods.leftep(i)))
    right.append(abs(Area-methods.rightep(i)))
    mid.append(abs(Area-methods.midpt(i)))
    trapez.append(abs(Area-methods.trapezoid(i)))

x=np.linspace(2,102,100)

plt.figure()
plt.grid(linestyle='--')


##############  Graph 1 : Absolute error for all methods #################

plt.scatter(total,left,label='Left-End Method',s=6)
b=regression.curve(total,left)[1]
a=10**regression.curve(total,left)[0]
plt.plot(x,a*(x**b),label='Left-End Method')

plt.scatter(total,right,label='Right-End Method',s=6)
b=regression.curve(total,right)[1]
a=10**regression.curve(total,right)[0]
plt.plot(x,a*(x**b),label='Right-End Method')

plt.scatter(total,mid,label='Mid-Point Method',s=6)
b=regression.curve(total,mid)[1]
a=10**regression.curve(total,mid)[0]
plt.plot(x,a*(x**b),label='Mid-Point Method')

plt.scatter(total,trapez,label='Trapezoid Method',s=6)
b=regression.curve(total,trapez)[1]
a=10**regression.curve(total,trapez)[0]
plt.plot(x,a*(x**b),label='Trapezoid Method')
plt.legend()
plt.show()
plt.savefig('Error4.png')
plt.clf()

##############  Graph 2 : Comparision of right and left method #################

plt.scatter(total,left,label='Left-End Method',s=6)
b=regression.curve(total,left)[1]
a=10**regression.curve(total,left)[0]
plt.plot(x,a*(x**b),label='Left-End Method')

plt.scatter(total,right,label='Right-End Method',s=6)
b=regression.curve(total,right)[1]
a=10**regression.curve(total,right)[0]
plt.plot(x,a*(x**b),label='Right-End Method')
plt.legend()
plt.show()
plt.savefig('ErrorRL.png')
plt.clf()

################

total_log=[]; t=2
while(t<103):
    total_log.append(np.log10(t))
    t=t+5

size=len(left)

leftlog=np.zeros(size)
rightlog=np.zeros(size)
midlog=np.zeros(size)
trapezlog=np.zeros(size)

for j in range(size):
    leftlog[j]=np.log10(left[j])
    rightlog[j]=np.log10(right[j])
    midlog[j]=np.log10(mid[j])
    trapezlog[j]=np.log10(trapez[j])



plt.grid(linestyle='--')

x=np.linspace(0,2.5,40)

##############  Graph 3 : Logarithms of all methods #################

plt.scatter(total_log,leftlog,label='Left-End Method',s=6)
m=regression.bfline(total_log,leftlog)[1]
c=regression.bfline(total_log,leftlog)[0]
plt.plot(x,m*x+c)

plt.scatter(total_log,rightlog,label='Right-End Method',s=6)
m=regression.bfline(total_log,rightlog)[1]
c=regression.bfline(total_log,rightlog)[0]
plt.plot(x,m*x+c)

plt.scatter(total_log,midlog,label='Mid-Point Method',s=6)
m=regression.bfline(total_log,midlog)[1]
c=regression.bfline(total_log,midlog)[0]
plt.plot(x,m*x+c)

plt.scatter(total_log,trapezlog,label='Trapeziod Method',s=6)
m=regression.bfline(total_log,trapezlog)[1]
c=regression.bfline(total_log,trapezlog)[0]
plt.plot(x,m*x+c)

plt.legend()
plt.show()
plt.savefig('Error4log.png')
plt.clf()


#####################

diff=np.zeros(size)
for i in range(size):
    diff[i]=(left[i]-right[i])

plt.grid(linestyle='--')
plt.plot(total,diff,label='Difference in the Left and Right end values.')
plt.legend()
plt.show()
plt.savefig('diff_rl.png')
plt.clf()

##############  Later graphs : plotting all methods  and their logarithms #################

def normalplot(data,lbl):
    plt.grid(linestyle='--')
    plt.ylim(-5,50)
    plt.scatter(total,data,label=lbl,s=6)
    b=regression.curve(total,data)[1]
    a=10**regression.curve(total,data)[0]
    plt.plot(x,a*(x**b),label=lbl)
    plt.legend()
    plt.show()
    plt.savefig(lbl+".png")
    plt.clf()


def logplot(data,lbl):
    plt.grid(linestyle='--')
    plt.scatter(total_log,data,label=lbl,s=6)
    m=regression.bfline(total_log,data)[1]
    c=regression.bfline(total_log,data)[0]
    plt.plot(x,m*x+c)
    plt.legend()
    plt.show()
    plt.savefig(lbl+".png")
    plt.clf()


normalplot(left,"Left-End Method")
normalplot(right,"Right-End Method")
normalplot(mid,"Mid-Point Method")
normalplot(trapez,"Trapezoid Method")

logplot(leftlog,"Left-End Method_log")
logplot(rightlog,"Right-End Method_log")
logplot(midlog,"Mid-Point Method_log")
logplot(trapezlog,"Trapezoid  Method_log")