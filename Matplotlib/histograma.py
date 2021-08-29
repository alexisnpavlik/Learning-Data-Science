import matplotlib.pyplot as plt

a=[22,55,62,55,62,55,62,55,62,55,45,55,55,5,55,55] #eje y
bins=[0,10,20,30,40,50,60,80,90] #logitud de eje  x

plt.hist(a, bins, histtype='bar',color='orange', rwidth=0.56)

plt.title('histograma') 
plt.show()