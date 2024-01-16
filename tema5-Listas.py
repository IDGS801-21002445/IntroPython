'''
Una lista de elementos se crea con corchetes []
'''

lista1 = ["Armando", 33, 9, 5, True, "Jose", 20.8]
print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])
print(lista1[0 : 3])
print(lista1[3:])

lista1.append("Rivera")
print(lista1)

lista1.insert(2, "Nadia")
print(lista1)

lista1.extend(["uno", 1.1, False])
print(lista1)

lista1.remove(33)
print(lista1)

lista1.pop()
print(lista1)

lista2 = ["tres", "cuatro"]
lista3 = lista2 + lista1
print(lista3)

print(lista2 * 4)

lista4 = [2, 5, 1, 4, 3]
print(lista4)

lista4.sort()
print(lista4)

del lista4[0]
print(lista4)