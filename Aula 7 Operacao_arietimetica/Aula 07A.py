n1=int(input('Um valor'))
n2 =int(input('Outro valor'))
s = n1+n2 # Soma
m = n1*n2 #Multiplicação
d = n1/n2 #Divisão
di = n1//n2 #Divisão inteira
e = n1**n2 #Exponenciação
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s,m,d),end=' ') #end='' não quebra linha {:.3f} São 3 casas decimáis flutuantes
print('Divisão inteira {} e  a potência {}'.format(di,e))


