from math import cos
from math import pow
from math import pi
class DCT:

    def dct(self, X):
        N = len(X)                              #   Numero de amostras
        x = [ [0] * N ] * N
        sinal = [0] * N

        for k in range(0, N):

            ck = 1
            if k == 0: ck = pow(1/2, 1/2)

            Ak = pow(2/N, 1/2)
            fk = k / (2 * N)
            phase = (k * pi) / (2 * N)

            for n in range(0, N):
                x[k][n] = X[n] * cos(2 * pi * fk * n + phase) #Arredonda em 4 casas decimais
                sinal[k] += Ak * ck * x[k][n]
        return sinal


    def idct(self, X):
        N = len(X)                              #   Numero de amostras
        x = [ [0] * N ] * N
        sinal = [0] * N

        for k in range(0, N):

            ck = 1
            if k == 0: ck = pow(1/2, 1/2)

            Ak = pow(2/N, 1/2) * ck
            fk = k / (2 * N)
            phase = (k * pi) / (2 * N)

            for n in range(0, N):
                x[k][n] = X[k] * cos(2 * pi * fk * n + phase) #Arredonda em 4 casas decimais
                sinal[n] += Ak * x[k][n]
        return sinal

    #realiza a soma de todos os elementos do vetor
    def somaVetor(self, vetor):
        soma = 0
        for k in range(0, len(vetor)) :
            for n in range(0, len(vetor)):
                soma += self.x[k][n]
            print("{} -> {}".format(k, soma))
        return
