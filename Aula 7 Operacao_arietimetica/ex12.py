#Faça um ogoritimo que leia o preço deum produto e mostre seu novo preço com 5% de desconto

preço=float(input('Qual é o preso do produto R$'))
novo=preço -(preço * 5 /100)
print('O produto que custa R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))