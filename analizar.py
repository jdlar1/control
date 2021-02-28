import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    a = np.loadtxt('datos.txt', skiprows = 3)[500:1000]  / 1023

    print(f'min: {a.min()}')
    print(f'max: {a.max()}')
    print(f'amplitud: {20 * np.log10(a.max()-a.min())} dB')
    
    plt.plot(np.arange(len(a)), a)
    plt.xlabel('Muestra')
    plt.ylabel('$A/A_0$')

    plt.savefig('outputs/0_2.jpg')

    plt.show()
