'''
minha_lista = [1,2,47,2,3,235,6,2,3]

print(minha_lista, type(minha_lista))

minha_lista.append(10000)

print(minha_lista, type(minha_lista))

print(minha_lista[2])

lista_de_nomes = ['jujuba', 'leonardo', 'juliana', 'marcio', 'hermes', 'netinho', 'lucas', 'abner']
print(lista_de_nomes[3])

#print(lista_de_nomes[::-1])

print(lista_de_nomes[::-2])

---------------------------------------

#extend
carros = ['fiat uno', 'mercedes', 'bmw']
motoristas = ['abner', 'hermes', 'neto']
print(carros, motoristas)

carros.extend(motoristas)
print(carros)

-----------------------------------------

#index
carros = ['fiat uno', 'mercedes', 'bmw']
motoristas = ['abner', 'hermes', 'neto']

x = carros.index('bmw') 
print(x)


--------------------------------------


#insert
carros = ['fiat uno', 'mercedes', 'bmw']
motoristas = ['abner', 'hermes', 'neto']

motoristas.insert(2, 'lucas')
print(motoristas)


------------------------------------------


#pop
carros = ['fiat uno', 'mercedes', 'bmw']
motoristas = ['abner', 'hermes', 'neto']
carros.pop(2)
print(carros)


------------------------------------

#remove
carros = ['fiat uno', 'mercedes', 'bmw']
motoristas = ['abner', 'hermes', 'neto']
motoristas.remove('abner')
print(motoristas)

-----------------------------------


#reverse
carros = ['fiat uno', 'mercedes', 'bmw']
motoristas = ['abner', 'hermes', 'neto']
carros.reverse()
print(carros)

-------------------------------
'''


