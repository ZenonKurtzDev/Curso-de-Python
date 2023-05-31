n= (input('Qual é o seu nome ?')).strip()
if n =='Zenon':
    print('Logado no Sistema')
else:
    print('Usuário não cadastrado')
print('Seja bem Vindo ! {}'.format(n))



n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
m = (n1 +n2) /2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua nota foi boa!Parbéns')
else:
    print('Sua nota foi ruim! Estude MAIS')

