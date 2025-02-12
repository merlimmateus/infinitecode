setPessoa = {"Nome"}

print(setPessoa)

# Forma correta de criar um set vazio
vazio_set = set()
print(type(vazio_set))  # <class 'set'>

setPessoa.add("Julia")

setPessoa.remove("Julia")

s1 = {1, 2, 3}
s2 = {3, 4, 5}

# União (tudo que está em s1 ou s2)
print(s1 | s2)  # {1, 2, 3, 4, 5}

# Interseção (elementos comuns)
print(s1 & s2)  # {3}

# Diferença (elementos de s1 que não estão em s2)
print(s1 - s2)  # {1, 2}

# Diferença Simétrica (elementos exclusivos de cada conjunto)
print(s1 ^ s2)  # {1, 2, 4, 5}

# Outras formas de declarar conjuntos

intersectionS1S2 = s1.intersection(s2)
unionS1S2 = s1.union(s2)
differenceS1S2 = s1.difference(s2)

numeros = {1, 2, 3, 4, 5}

print(3 in numeros)
print(10 in numeros)

original = {1, 2, 3}
copia = original.copy()

print(copia)

s = {1, 2, 3}
s.clear()
print(s)  # set()
