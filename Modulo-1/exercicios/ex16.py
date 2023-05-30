#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

'''from math import trunc
num =float(input('Digite um valor:'))
print('O Valor digitado foi {} e a sua portção interira é {}'.format(num,trunc(num)))'''

num = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))