print('Olá, Mundo!')

nome=input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
s=int(n1)+int(n2)
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))    

a = input ('Digite algo: ')
print('O tipo primitivo desse valor é ' , type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())

nome=input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, o produto é {}, \n a divisão é {:.3f} '.format(s, m, d), end=' >>> ')
print('A divisão inteira é {} e a potência é {}'.format(di, e))


