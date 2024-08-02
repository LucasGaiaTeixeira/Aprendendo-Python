'''
Um freelancer está com dificuldade para calcular qual valor cobrar por um projeto que está
 estimado em 80 horas. Após pensar e revisitar o preço de alguns projetos que cobrou no passado,
   ele montou a seguinte 
   fórmula: valor inicial + quantidade de horas estimadas * valor da hora + 15% do valor calculado. 
   rie um programa que faça essa conta para o freelancer. Considere que o valor inicial sempre será R$ 1000,00 
   e o valor da hora cobrada é de R$ 20,45. A aplicação deve imprimir o valor calculado pelo projeto considerando duas casas 
   decimais na formatação do valor. Dica: Preste atenção na ordem que as operações da fórmula devem ser realizadas.
'''

#codigo
#horas 80h, 
#formula: valor inicial + quantidade de horas estimadas * valor da hora + 15% do valor calculado
#valor incial 1000h
#valor da hora: 20.45

valor_inicial = 1000
horas = 80
valor_da_hora = 20.45

total = valor_inicial + (horas * valor_da_hora) + (0.15 * (horas * valor_da_hora))
print(f"{total:.2f}")


'''
Uma nave espacial recebe as pessoas com uma mensagem de boas vindas de acordo com o nome que elas forneceram ao fazer o 
cadastro na recepção. Crie uma aplicação que imprima a mensagem de boas vindas de acordo com os nomes na 
lista: nomes = [“Elysson“, “Giulia“, “Willian“, “Gileno“], 
com a seguinte mensagem: “Olá, NOME_PESSOA! Seja bem vindo à nave Imperial dos Siths.”. 
Crie um programa que faça a interpolação da string de boas vindas, substituindo o NOME_PESSOA pelo nome lido na lista e 
imprimindo a frase de boas vindas com o nome substituído.
'''

nomes = ["Elysson", "Giulia", "Willian", "Gileno"]

for NOME_PESSOA in nomes:
    print(f"Olá, {NOME_PESSOA}! Seja bem vindo à nave imperial dos siths.")