#Crie um algoritimo que leia um número e mostre a raiz quadrada e seu triplo

n =int(input('Digite um número'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dorbro de {} vale {}'.format(n, d))
print('O triplo de {} vale {}.\n A raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
