def pyBonacci(num_meses, num_parejas):

    resultados = [0] * (num_meses + 1)

    if num_meses < 0:
        raise ValueError('El numero de meses es <0 ')
    elif num_parejas < 1:
        raise ValueError('El numero de parejas es <1')
    elif num_meses == 0:
        resultados[0] = 0
    elif num_meses == 1:
        resultados[1] = 1
    else:
        resultados[num_meses] = pyBonacci(num_meses - 1, num_parejas) + pyBonacci(num_meses - 2, num_parejas) * num_parejas

    return resultados[num_meses]


class Fibonacci(object):
    def __init__(self):
        pass

    def compute(self, n, k):
        return pyBonacci(n, k)
