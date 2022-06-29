#!/usr/local/bin/python3.9
# AS2101 Task 1 : Pythin PLot and Report Making
# Pranit Zope AE20B064

from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(-1.5,2.5,100)



#### CODE FOR 2D Graph ####

#  Our functionn is y=x^3-x^2-2x, i.e y=(x-2)(x)(x+1)
y=x**3-x**2-2*x

plt.figure()
plt.plot(x, y)
plt.title('y = x$^3$-x$^2$-2x')
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.grid(linestyle='--')
plt.savefig('2dgraph.png')
plt.show()



