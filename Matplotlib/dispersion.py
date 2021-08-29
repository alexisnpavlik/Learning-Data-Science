import matplotlib.pyplot as plt

x1=[0.25,1.25,2.25,3.25,4.25]
x2=[0.50,1.50,2.50,3.50,4.8]
y1=[0.25,1.25,2.25,3.6,4.8]
y2=[0.50,1.50,2.50,3,4.500]

plt.scatter(y1, y2 ,label='Datos 1', color='red')
plt.scatter(y2, y1,label='Datos2',color='blue')

plt.title('Grafico de dispersion')
plt.legend()
plt.show()