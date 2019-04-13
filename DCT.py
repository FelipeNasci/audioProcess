from math import cos
from math import pow
from math import pi
class DCT:

    x = None

    def dct(self, X):
        N = len(X)                              #   Numero de amostras
        self.x = [ [0] * N ] * N
        sinal = [0] * N

        for k in range (0, N):

            ck = pow(1/2, 1/2)
            if k > 0: ck = 1

            Ak = pow(2/N, 1/2) * ck * X[k]
            fk = k / (2 * N)
            phase = (k * pi) / (2 * N)

            for n in range(0, N):
                self.x[k][n] = round(Ak * cos(2 * pi * fk * n + phase), 4 ) #Arredonda em 4 casas decimais
                sinal[n] += self.x[k][n]
            print(self.x[k])
        return sinal

    #realiza a soma de todos os elementos do vetor
    def somaVetor(self, vetor):
        soma = 0
        for k in range(0, len(vetor)) :
            for n in range(0, len(vetor)):
                soma += self.x[k][n]
            print("{} -> {}".format(k, soma))
        return soma
