from DCT import DCT
from Image import Image
from Grafico import Grafico

dct = DCT()
img = Image()
#grafico = Grafico()

sDigital = [10, 5, 8.5, 2, 1, 1.5, 0, 0.1]     #   Sinal Digital
print('Sinal original')
print(sDigital)

sAnalogico = dct.idct(sDigital)
print(sAnalogico)

sDigital = dct.dct(sAnalogico)
print(sDigital)