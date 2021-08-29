import matplotlib.pyplot as plt

a=[1,2,3,4,5,6,7,8]
b=[1,2,3,4,5,6,7,8]

plt.plot(a, b ,color='green', label='linea rara',linewidth=2)

plt.title('Mi primer grafico')
plt.xlabel('Eje x')
plt.ylabel('Eje y')

plt.grid()

plt.legend()
plt.show()

