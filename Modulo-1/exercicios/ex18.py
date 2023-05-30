#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno e cosseno e a tangente desse ângulo.

'''import math
ângulo = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo,seno))

cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {}tem o COCENO de {:.2f}'.format(ângulo,cosseno))

tangente= math.tan(math.radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo,tangente))'''

#Modo simplificado

from    math import radians,sin,cos,tan

ângulo = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo,seno))

cosseno = cos(radians(ângulo))
print('O ângulo de {}tem o COCENO de {:.2f}'.format(ângulo,cosseno))

tangente= tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo,tangente))
