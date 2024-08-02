'''
dicionario = {"numero":94_981245254}

print(dicionario["numero"])
#ou
print(dicionario)
-------------------------------------------
'''

dicionario = {"lucas":24, 
              "natasha":24, 
              "augusto":57, 
              "sileia":49, 
              "larissa":17,
              "ninguem":[]
              }

print(dicionario.get("lucas"))
print(dicionario.get("aquiles", 0.6))

print("-----------------------------------")

print(dicionario.items())
print("-----------------------------------")

print(list(dicionario.items()))
print("-----------------------------------")

print(dicionario.keys())
print("-----------------------------------")

print(dicionario.values())

dicionario2 = {1:'z', 2:'f', 4:'4'}

