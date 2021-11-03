# 1
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
aux = [el for el in lista]

aux.sort()
lista_sortata_ascendent = aux
print(lista_sortata_ascendent)

aux.sort(reverse = True)
lista_sortata_descendent = aux
print(lista_sortata_descendent)

print(lista)

aux1 = [el for el in lista]
aux1.sort()
print("Numerle crescatoare sunt: {0}".format(aux1[1:len(aux1):2]))
print("Numerle descrescatoare sunt: {0}".format(aux1[:len(aux1):2]))
print("Multiplii de 3 sunt: {0}".format(aux1[2:len(aux1):3]))


