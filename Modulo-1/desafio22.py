
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome....:')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro tem {}letras'.format(nome.find('')))

#Pode ser assim
separa=nome.split()
print('Seu primeiro nome é {}ele tem letras{}'.fomrmat(separa[0],len))