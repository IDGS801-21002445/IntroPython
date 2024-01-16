'''
Las Tuplas son Inmutables
'''

tupla = ("uno", "dos", "tres")
print(tupla)

tuplas_varios_datos = (12, True, 23.5, "Gato", 12 + 4j)
print(tuplas_varios_datos)

tuplas_con_tuplas = (1, 2, 3, 4, (1, 2, 3))
print(tuplas_con_tuplas)

print(tuplas_varios_datos[3])
print(tuplas_varios_datos[-2])
print(tuplas_varios_datos[0:2])

a, b, c = tupla
print(a)
print(b)
print(c)

tupla_nueva = tupla + tuplas_varios_datos
print(tupla_nueva)