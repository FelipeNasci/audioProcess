from DCT import DCT
from Image import Image
from Grafico import Grafico

dct = DCT()
img = Image()
grafico = Grafico()

#lena = um vetor [][]
lena = img.getImage('lena.bmp')
#img.showImage("Lena Original", lena)
dct.dctImg(lena)





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
