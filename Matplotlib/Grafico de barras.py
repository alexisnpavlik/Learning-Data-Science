import matplotlib.pyplot as plt

x1=[0.25,1.25,2.25,3.25,4.25]
x2=[0.50,1.50,2.50,3.50,4.8]
y1=[0.25,1.25,2.25,3.6,4.8]
y2=[0.50,1.50,2.50,3,4.500]

plt.bar(x1, y1, label='datos 1', width=0.5,color='blue')
plt.bar(x2, y2, label='datos 2', width=0.5,color='red')

plt.title('Grafico de barras')
plt.legend()
plt.grid(True)
plt.show()