# -*- coding: utf-8 -*-
#from math import pi
from math import cos
from math import pow

class DCTPDI:
    
    #DCT inversa, resulta no sinal analogico a partir do digital
    def IDct(self, X):
        pi = 3.14159265358979323846
        x = []
        N = len(X)
        ck = pow(1/2,1/2)
        
        for n in range(0, N):
            soma = 0
            for k in range(0,N):
                if (k>0): 
                    ck = 1
                else:
                    ck = pow(1/2, 1/2)
                soma += ck * X[k]*cos(((2*pi*k*n)/(2*N)) + ((k*pi)/(2*N)))
            x.append(pow(2/N, 1/2) * soma)
        return x
    
    #DCT, resulta no sinal digital a partir do analógico
    def Dct(self, x):
        pi = 3.14159265358979323846
        X = []
        N = len(x)
        ck = pow(1/2, 1/2)
        
        for k in range(0, N):
            if (k>0):
                ck = 1
            else:
                ck = pow(1/2, 1/2)
            soma = 0
            for n in range(0, N):
                soma += x[n] * cos(((2*pi*k*n)/(2*N) + ((k*pi)/(2*N))))
            X.append(round(pow(2/N, 1/2) * ck * soma, 4))
        return X
