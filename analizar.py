import numpy as np
import matplotlib.pyplot as plt


FREC = '4'

if __name__ == '__main__':

    try:
        a = np.loadtxt(f'datos{FREC}.txt', skiprows = 3)  / 1023
    except OSError:
        a = np.loadtxt(f'datos/datos{FREC}.txt', skiprows = 3)[350:]  / 1023
    
    print(f'min: {a.min()}')
    print(f'max: {a.max()}')
    print(f'amplitud: {20 * np.log10(a.max()-a.min())} dB')
    
    plt.plot(np.arange(len(a)), a)
    plt.xlabel('Número de muestra')
    plt.ylabel('$A/A_0$')

    plt.savefig(f'outputs/{FREC}.png', transparent = True, dpi = 500)

    plt.show()
