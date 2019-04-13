from DCT import DCT
from Grafico import Grafico

dct = DCT()
grafico = Grafico()

#sDigital = [10, 5, 8.5, 2, 1, 1.5, 0, 0.1]     #   Sinal Digital
sDigital = [10, 5, 8.5]     #   Sinal Digital
print('Sinal original')
print(sDigital)

print('Aplicando DCT - Obtendo **   Sinal Analógico **')
sAnalogico = dct.dct(sDigital)
print(sAnalogico)

print('Aplicando DCT - Obtendo **   Sinal Digital **')
sDigital = dct.dct(sAnalogico)
print(sDigital)
