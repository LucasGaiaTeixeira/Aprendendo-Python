def meu_nome():
    nome = input("digite seu nome: ")
    print(f"Olá {nome} bem vindo!")
    return False


#validação
def nomes(nome1, nome2):
    controle = False
    if(nome1 == "lucas" and nome2 == "natasha"):
        controle = True
    print(f"Olá {nome1} e {nome2} vocês são um lindo casal!!")
    return controle    

#*args

def soma_numeros(*args):
    total = 0
    for i in args:
        total = total + i
    return total    