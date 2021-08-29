import matplotlib.pyplot as plt

dormir=[1,2,3,4]
comer=[2,3,4,5]
trabajar=[1,2,3,7]

etiquetado=['dormir','comer','trabajar']
colores=['red','green','blue']
divisors=[1,7,2]

plt.pie(divisors,colors=colores, labels=etiquetado)

plt.title('Grafico de torta')
plt.show()