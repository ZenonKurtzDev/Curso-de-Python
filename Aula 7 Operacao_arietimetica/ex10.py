#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e 
#mostre quantos dolares ela pode comprar
real=float(input('Quantos reais você tem na carteira? R$'))
dolar= real  /5.50
print('Com R${:.2f} Você pode comprar U${:.2f}'.format(real, dolar))