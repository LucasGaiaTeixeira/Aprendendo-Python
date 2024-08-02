'''
1. Crie uma função que, ao receber um número inteiro, retorna se um número é par ou ímpar.

Dicas:

– Utilize o comando int(input()) para obter o número inteiro de entrada.

– Passe o número para uma função por parâmetro.

– Calcule e retorne o resultado.

– Mostre na tela se o número é ‘Par’ ou ‘Impar’, usando o comando print().

– Extra: utilize **kwargs (Opcional)

ENTRADA	SAÍDA ESPERADA
2	        Par
9	       Impar
14	        Par
'''
#codigo:
#def par_ou_impar(**kwargs):
#    for numero in kwargs:
#        if(kwargs[numero] % 2) == 0:
#            print(numero, ":", kwargs[numero], "Par")
#        else:
#            print(numero, " : ", kwargs[numero], "Impar")   
#par_ou_impar(numero_1 = 1, numero_2 = 10, numero_3 = 87, numero_4 = 6)                  

#--------------------------------------------------------------------------------
'''
2. Crie uma função que recebe um número inteiro por parâmetro e então imprime na tela do número recebido até o zero.

Dicas:

– Utilize o comando int(input()) para obter o número inteiro de entrada.

– Passe o número para uma função por parâmetro.

– Mostre na tela do número recebido até o zero, usando o comando print().

– Extra: crie uma versão recursiva deste programa (Opcional)

ENTRADA	           SAÍDA ESPERADA
2	                    210
5	                   543210
'''
#codigo 
#def fatorial(numero):
#    total = 1
#    if(numero == 0 or numero == 1):
#        return 1
#    else:
#        for i in range(numero, 1, -1):
#            total = total * i
#       return total    

#def fatorial(numero):
#    if(numero == 0 or numero == 1):
#        return 1
#    else:
#        return numero * fatorial(numero -1)

#print(fatorial(5))

#--------------------------------------------------------------------------------------------
'''
3. Crie um programa com uma função que necessite de três parâmetros e então que retorne a sua soma.

Dicas:

– Utilize o comando int(input()) para obter os três números inteiros de entrada.

– Passe os três números para uma função por parâmetro.

– Calcule a soma e retorne o resultado.

– Mostre na tela a soma calculada, usando o comando print().

– Extra: utilize *args (Opcional)

ENTRADA	      SAÍDA ESPERADA
263	               11
9712	           28
231	                6
'''

#def numeros(*args):
#    total = 0
#    for i in args:
#        total += i  
#    return total

#print(numeros(5,3,4))


#---------------------------------------------------------------------------
'''
4. Crie um programa que seja capaz de obter e somar TODOS os números passados pelo usuário como entrada, permitindo somar qualquer quantidade de dados de entrada.

Dicas:

– Utilize uma estrutura de repetição para repetir a leitura de todos os números passados como entrada, até que encontre o valor ‘-1’.

– Ou seja, o número -1 será o critério de parada para a leitura dos dados de entrada.

– Utilize o comando int(input()) para obter todos os números inteiros de entrada.

– Calcule a soma de todos os números.

– Mostre na tela a soma calculada, usando o comando print().

– Extra: utilize Funções e *args (Opcional).

ENTRADA	          SAÍDA ESPERADA
27-1	                9
472191-1	           33
285134316-1	           51
'''

#def leitura(*args):
#    total = 0
#    for i in args:
#        while(i != -1):
#            total = total + i
#            break
        
#    return total

#print(leitura(2,8,5,1,3,4,3,1,-1))    


#------------------------------------------------------------------------------
'''
5. Faça um programa com uma função que necessite de um parâmetro. A função deve retornar “Positivo”, se seu o número for maior que zero, “Negativo” se o número for menor que zero, e “Zero” se o número for igual a zero.

Dicas:

– Utilize o comando int(input()) para obter o número inteiro de entrada.

– Implemente uma função que seja capaz de descobrir se um número é positivo, negativo ou zero, e retorne o resultado.

– Mostre na tela o resultado, usando o comando print().

ENTRADA	SAÍDA ESPERADA
2	      Positivo
-7	      Negativo
0	        Zero
'''

#def pos_ou_neg(*args):
#    for i in args:
#        if(i > 0):
#            print(f"{i} Positivo!")
#        else:
#            print(f"{i} Negativo!")

#pos_ou_neg(2,3,5,1,-4,-345,12,-4324,-14,123,-4,32143,-34,1)
#--------------------------------------------------------------------------------
'''
6. Escreva uma função que, dado o valor da conta de um restaurante e um percentual de taxa de serviço, calcule e exiba a gorjeta do garçom, considerando o percentual 
do valor da conta.

Dicas:

– Utilize o comando float(input()) para obter o valor da conta.

– Utilize o comando int(input()) para obter o valor da taxa de serviço.

– Implemente uma função que calcule a gorjeta do garçon, baseado no percentual do valor da conta definido.

– Mostre na tela o resultado com duas casas decimais, usando o comando print(f”{resultado:.2f}”).

– Lembrando que o cálculo de porcentagem é: valor*porcentagem/100.

ENTRADA	     SAÍDA ESPERADA
10015	         15.00
139.4512	     16.73
1529.3227	     412.92
'''


#def conta_restaurante():
#    conta = float(input("digite o valor de sua conta: "))
#    garcom = conta * 0.10
#    print(f"O Garçom recebe: {garcom:.2f} R$")
#conta_restaurante()   

#----------------------------------------------------------------------------------
'''
7. Crie uma função que permita contar o número de vezes que aparece uma determinada letra em uma frase. A letra desejada e a frase a ser verificada serão passadas por parâmetro para a função, que retornará a quantidade da letra na frase.

Dicas:

– Utilize o comando input() para obter a letra desejada.

– Utilize o comando input() para obter a frase desejada.

– Implemente uma função que conte a quantidade de vezes que a letra aparece na frase e retorne este valor.

– Mostre na tela o resultado obtido, usando o comando print().

ENTRADA	      SAÍDA ESPERADA
aaaaaaa	           6
pparalelepipedo	   3
nbanana	           2
'''

#def letras(palavra):
#    letra = 0
#    for i in palavra:
#        if(i == 'a'):
#            letra+=1    
#    print(letra)
#letras("nbanana")    
#--------------------------------------------------------------------------------------
'''
8. Crie uma função que receba duas palavras e retorne “True” caso a primeira palavra seja um prefixo da segunda, e “False” caso contrário.

Exemplo: ’programa’ é prefixo de “programador”, pois todas as letras de ‘programa’ correspondem às primeiras letras de “programador”.

Dicas:

– Utilize o comando input() para obter a palavra1.

– Utilize o comando input() para obter a palavra2.

– Implemente uma função que identifique se a palavra1 é prefixo da palavra 2, e retorne o resultado obtido.

– Mostre na tela o resultado, usando o comando print().

– Extra: utilize slicing para indexar as strings. (Opcional).

ENTRADA	             SAÍDA ESPERADA	              EXPLICAÇÃO
programaprogramador	     True	                     As 8 letras de programa são exatamente as 8 primeiras letras de programador, então é prefixo!
abcdabcdefghijk	         True	                     As 4 primeiras letras de “abcd” são exatamente as 4 primeiras letras de “abcdefghijk”, então é prefixo!
canabanana	             False	                     Embora 3 das 4 letras de “cana” sejam iguais as 4 primeiras letras de “banana”, era preciso que todas fossem iguais para ser prefixo. Ou seja, não é prefixo!
testatestemunha	         False	                     Embora 4 das 5 letras de “testa” sejam iguais as 5 primeiras letras de “testemunha”, era preciso que todas fossem iguais para ser prefixo. Ou seja, não é prefixo!
'''

#def prefixo():
#   palavra_1 = input("digite a primeira palavra: ")
#   prefixo = input("digite a segunda palavra: ")

#    if(palavra_1[:len(prefixo)] == prefixo):
#        print("Prefixo Correto")
#   else:
#        print("Prefixo Incorreto")    
#prefixo()        

#def sufixos():
#    palavra_1 = input("digite a primeira palavra: ")
#    sufixo = input("digite a segunda palavra: ")

#    if(palavra_1[-len(sufixo):] == sufixo):
#        print("Sufixo Correto!")
#    else:
#        print("Sufixo Incorreto!")
#sufixos()           