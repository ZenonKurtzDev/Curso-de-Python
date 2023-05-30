from random import shuffle 

n1 =(input('Primeito aluno:'))
n2 = (input('Segundo aluno:'))
n3 = (input('Terceiro aluno:'))
n4 = (input('Quarto aluno:'))
lista= [n1,n2,n3,n4]
escolido=  (lista)
shuffle(lista)
print('A ordem de apresentaoção será ')
print(lista)