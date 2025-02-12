# Forma comum de criar dicionários
pessoa = {"nome": "Ana", "idade": 31 , "cidade": "São Paulo"}

# Usando dict()
outra_pessoa = dict(nome="Carlos", idade=30, cidade="Rio de Janeiro")

# Dicionário vazio
vazio = {}

print(pessoa.get("nome", "Não informado"))
print(pessoa.get("altura", "Não informado"))

print("Pessoa: ", pessoa)

# Removendo uma chave específica

idade = pessoa.pop("idade")
print(idade)
print(pessoa)

# Removendo a última chave adicionada (Python 3.7 + )

ultima = pessoa.popitem()
print(ultima)

del pessoa["nome"]
print(pessoa)

# ---------------------------------------------------------------------------------------------------------------------

print("----------------------------------------------------------------------------------------------------------------")

pessoa = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}

# Iterando pelas chaves
for key in pessoa:
    print(key, ":", pessoa[key])

# Iterando pelas chaves e valores

for key, value in pessoa.items():
    print(f"{key}: {value}")

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
