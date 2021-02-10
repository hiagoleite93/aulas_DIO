# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))

a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or resto_a == 0:
    print('Um dos números é par')
elif resto_a == 0 and resto_b == 0:
    print('Todos os números são pares')
else:
    print('Nenhum dos números são pares')