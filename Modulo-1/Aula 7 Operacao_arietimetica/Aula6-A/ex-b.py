a=input('Digite algo:') # a é um objeto
print('O tipo primitivo desse valor é ',type(a))
print('Só tem espaco', a.isspace())
print('Só tem números' ,a.isnumeric())
print('È alfabético',a.isalpha())
print('È alfanúmerico',a.isalnum())
print('Está em maiúsculo',a.isupper())
print('Está em minúsculo',a.islower())
print('Está capitalizada',a.istitle()) #Quer dizer que tem letras maiúsculas e minúsculas