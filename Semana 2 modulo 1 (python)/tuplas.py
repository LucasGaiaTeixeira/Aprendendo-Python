from datetime import datetime
'''
#empacotamento
cadastro = "Lucas", 33, 12121999

print(type(cadastro), cadastro)
#------------------------------------------------------

#desempacotamento
nome, idade, datanasc = cadastro
print(nome)
print(idade)
print(datanasc)

#------------------------------------------
#substuindo valores ao todo

cadastro = cadastro[0], 24, cadastro[2]
print(cadastro)

---------------------------------------------------
'''

#desempacotamento part 2
cadastro = "Lucas", 33, 12121999, "Maceió", []

nome, idade, _,_,*restante = cadastro

cadastro[-1].append(datetime.today())

print(cadastro)


