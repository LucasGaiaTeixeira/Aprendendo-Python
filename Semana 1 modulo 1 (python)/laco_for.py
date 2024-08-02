'''
#print(100 * ['ana', 'maria', 'nada'])
                    #ou
nomes = ['Ana', 'Maria', 'Nada']
for nome in nomes:
    print(nome)

print('--------------------------------')

for nome1 in nomes:
    print(nome1.upper())

print(list(range(10)))

        #ou

for lista in range(10,1,-1):
    print(lista)


nomes = ['bruno', 'jose']
idades = [40, 55]

#print(zip(nomes, idades))#retorna um objeto gerador

lista_de_tuplas = zip(nomes, idades)
#print(next(lista_de_tuplas))

#print(list(lista_de_tuplas)) # ira fazer que os valores do zip em tuplas sejam colocados dentro de uma lista [('bruno', 40), ('jose', 55)]

        #ou

for nome, idade in lista_de_tuplas:
    print('essa pessoa:', nome, 'tem essa idade: ', idade)
    
for indice, idade in enumerate(idades):
    if idade > 50:
        print(f'maior que 50, idade:{idade} e indice:{indice}')


        
        
        
list comprehension = aplicação com laço for que gera novas listas sendo o metodo com so uma linha
nomes = ['bruno', 'jose', 'amanda']

nomes_com_ate_5_caracteres = [nome for nome in nomes if len(nome) <= 5]
print(nomes_com_ate_5_caracteres)

        #ou
nomes_com_ate_5_caracteres = []
for nome in nomes:
    if len(nomes) <= 5:
        nomes_com_ate_5_caracteres.append(nome)    
print(nomes_com_ate_5_caracteres)

#print([nome.upper() for nome in nomes]) #criou uma lista percorrendo o nomes da lista
'''

for numero in range(100):
    if numero % 2 != 0:
        continue# usando desse continue assim que pegar nele o ciclo ira volar para o for e pegar outro numero, sem passar pelo resto do loop
    print(f'O numero {numero} é par')

    if numero == 20:
        print('Ops... ja verefiquei muitos numeros pares')
        break    