import numpy as np
import matplotlib.pyplot as plt

# Creating a dataset
# Creando un conjunto de datos 
x = np.arange (-5, 5) 
print ("Los valores X en el conjunto de datos son: \ n", x) 
y = np.arange (-30, 30 , 6)


plt.plot(x, y,'o')
plt.xlabel (" valores X ") 
plt.ylabel (" valores Y ") 

plt.show()
# calculating value of coefficients in case of linear polynomial
z = np.polyfit(x, y, 1)
print("\ncoefficient value in case of linear polynomial:\n", z)

# calculating value of coefficient in case of quadratic polynomial
#z1 = np.polyfit(x, y, 2)
#print("\ncoefficient value in case of quadratic polynomial:\n", z1)

# calculating value of coefficient in case of cubic polynomial
#z2 = np.polyfit(x, y, 3)
#print("\ncoefficient value in case of cubic polynomial:\n", z2)