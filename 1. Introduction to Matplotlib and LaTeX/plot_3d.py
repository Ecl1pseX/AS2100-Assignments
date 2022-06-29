#!/usr/local/bin/python3.9
# AS2101 Task 1 : Pythin PLot and Report Making
# Pranit Zope AE20B064

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

def funct(x,y):
    return np.sin(2*x**2+3*y**2) 


plt.figure()
plt.title('y = sin(x$^2$+3y$^2$)')
ax=plt.axes(projection='3d')
x=np.linspace(-1,2,100)
y=np.linspace(-1,2,100)

X,Y =np.meshgrid(x,y)
Z=funct(X,Y)

ax.plot_surface(X,Y,Z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('z = x$^2$ + y$^2$')
plt.savefig('3dgraph.png')
plt.show()

