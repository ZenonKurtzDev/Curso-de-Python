#Faça um ogoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salário= float(input('Qual é o salário do funcionario R$'))
novo = salário + (salário * 5 /100)
print ('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário,novo))