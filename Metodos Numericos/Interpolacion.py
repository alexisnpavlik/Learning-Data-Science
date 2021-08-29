from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import pandas as pd

x=[390,400,410]
y=[1.548,1.63,1.51]

plt.plot(x,y, 'o')
plt.xlabel('x')
plt.ylabel('y')

p=lagrange(x,y)
print("El polinomio sera:")


print(p)
print("valor en x")
print(p(2))

plt.show()