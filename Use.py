from DCT import DCT
from DCTFelipe import DCTPDI
from Image import Image
from Grafico import Grafico

#dct = DCT()
dctFelipe = DCTPDI()
#img = Image()
#grafico = Grafico()

#lena = um vetor [][]
#lena = img.getImage('lena.bmp')
#img.showImage("Lena Original", lena)
#dct.dctImg(lena)

sDigital = [1.222, 1.22, 1.2, 1]
analogico = dctFelipe.IDct(sDigital)
voltaDigital = dctFelipe.Dct(analogico)
print(sDigital)
print(analogico)
print(voltaDigital)





'''

sDigital = [10, 5, 8.5, 2, 1, 1.5, 0, 0.1]     #   Sinal Digital
print('Sinal original')
print(sDigital)
#grafico.plotPonto(sDigital, "Sinal Original")

sAnalogico = dct.dct(sDigital)
print(sAnalogico)
#grafico.plotPonto(sAnalogico, "Sinal Analogico (DCT)")

sDigital = dct.dct(sAnalogico)
print(sDigital)
#grafico.plotPonto(sDigital, "Sinal Digital (IDCT)")

'''
