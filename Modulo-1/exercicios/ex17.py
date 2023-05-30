#Faça um programa que leia o comprimento do cateto retângular, calcule e mostre o comprimento da hipotenusa

'''cateto_oposto = float(input('Comprimento do cateto opsoto'))
cateto_adjacente = float (input('Comprimento do cateto adjacente'))
hiportenusa= (cateto_adjacente **2+ cateto_adjacente ** 2) ** (1/2)
print('A hipotenusa vai medir {}'.format(hiportenusa))'''

#Importando a hipotenusa
from math import hypot
co=float(input('Comprimento do cateto oposto:'))
ca=float(input('Comprimento do cateto adjacente:'))
hi= hypot(co, ca)
print( 'A hipotenusa vai medir {:.2f}'.format(hi))