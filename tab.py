import pandas as pd
import matplotlib.pyplot as plt

from pandas.core.indexes import period

datos: pd.DataFrame = pd.DataFrame(data={
    'periodo': [
        125, 60, 40, 20, 15, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.6, 0.4, 0.2
    ],
    'ganancia': [
        0, -0.0084947, 0, -0.0084947, 0.025509239004851907, -
        0.03402899411467522, -0.07675357429685967, -0.1628384180631924, -0.2323259057692283,  -
        0.6796899462073474, -1.0549487207069406, -1.7119269530055705, -
        2.731100637935228, -4.363699693840845, -
        7.133262398736329, -12.485387202276959 , -16.73378730599772 , -20.025509239004855 , -25.390258884358335
    ]

}
)


def main():

    print(datos.head())

    frecuencias = 1 / datos.periodo

    plt.scatter(frecuencias, datos.ganancia, marker='x')

    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud (dB)')

    plt.xscale('log')
    plt.savefig('outputs/ganancias.jpg')


if __name__ == '__main__':
    main()
