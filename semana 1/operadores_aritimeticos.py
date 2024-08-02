'''
#Operações aritimeticas
numero_1 = 10
numero_2 = 6

print('Soma: ', numero_1 + numero_2)
print('Subtração: ', numero_1 - numero_2)
print('Multiplicação: ', numero_1 * numero_2)
print('Exponensiação: ', numero_1 ** numero_2)
print('Divisão: ', numero_1 / numero_2)
print('Divisão exata: ', numero_1 // numero_2)
print('Resto da divisão: ', numero_1 % numero_2)


#Operadores Booleanos:
combinacoes = {
    (True ,True),
    (True, False),
    (False ,True),
    (False, False)
}

combinacao = {
    True, False
}

for a, b in combinacoes:
    print(f'{a} AND {b} ->  {a and b}')

for c, d in combinacoes:
    print(f'{c} OR {d} ->  {c or d}')

for e in combinacao:
    print(f' NOT {e} -> {not e}')

num = 1
num = float(num)    
print(num) #transformei de int para float


# Variaveis e tipos de dados:

a = b = c = 1
print(a)
print(b)
print(c)

d,e,f = 1,2,'lucas'
print(d)
print(e)
print(f)

'''
#Controle de fluxo
#if
idade = 35

if idade >= 18:
    print('maior de idade')
else:
    print('menor de idade')

velocidade = 80

if velocidade < 40:
    print('velocidade baixa')
elif velocidade <= 60:
    print('velociade moderada')
else:
    print('velocidade alta')