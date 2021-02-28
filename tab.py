import pandas as pd
import matplotlib.pyplot as plt

from typing import NoReturn

from pandas.core.indexes import period


def main():

    datos: pd.DataFrame = pd.DataFrame(data={
        'periodo': [
            125, 60, 40, 20, 15, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.6, 0.4, 0.2
        ],
        'ganancia': [
            -0.00849, -0.00849, -0.00849, -0.0016997, -0.0016997, -0.0016997, -0.0016997, -0.0016997, -0.0016997, -
            0.025509, -0.03402, -0.076733, -0.17149, -0.7719, -
            2.146577, -6.2529, -9.93316, -13.468, -19.213
        ]

    }
    )

    print(datos.head())

    frecuencias = 1 / datos.periodo

    plt.scatter(frecuencias, datos.ganancia, marker='x')

    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud (dB)')

    plt.xscale('log')
    plt.savefig('outputs/ganancias.jpg')


if __name__ == '__main__':
    main()
