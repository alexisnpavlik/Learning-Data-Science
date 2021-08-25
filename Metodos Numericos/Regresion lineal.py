import numpy as np
import matplotlib.pyplot as plt

def estimate_b0_b1(x,y):
    assert len(x)==len(y), "Tamaño de los datos incorrectos"
    n=np.size(x)

#Sacamos el promedios de X e Y
    m_x, m_y=np.mean(x), np.mean(y)

#Sumatoria de X e Y y sumatoria de XX
    sumatoria_xy= np.sum((x-m_x)*(y-m_y))
    sumatoria_xx=np.sum(x*(x-m_x))

#coenfientes de regresion
    b1=sumatoria_xy/sumatoria_xx
    b0=m_y - b1*m_x
    return (b0,b1)

#Graficacion
def plot_regression(x,y,b):
    plt.scatter(x,y,color="g",marker="o",s=30)
    y_pred=b[0]+b[1]*x
    plt.plot(x,y_pred,color="b")

#Etiquetado
    plt.xlabel("x-independiente")
    plt.xlabel("Y-dependiente")
    plt.show()




def run():
#Dataset
    x=np.array([1,2,3,4,5])
    y=np.array([2,3,5,6,5])

    b= estimate_b0_b1(x,y)
    print(f"Los valores de b0 = {b[0]}, b1 = {b[1]}")
    plot_regression(x,y,b)


if __name__=='__main__':
    run()
