#Escreva um program que pergunte a quantidade de km percorridos por um carro alugdo, e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,oo por dia e R$0,15 centavos o kilometro roddo

dias= int(input('Quantos dias alugado ?')) 
km= float(input('Quantos km rodados ?'))
pago= (dias *60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
