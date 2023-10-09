# listas armazenam de maniera sequencial qualquer tipo de objeto
# lsitas sã objetos mutáveis
# criar listas através de 

# 1. construtor list
letras = list("python")

# 2. função range 
numeros = list(range(10))

# 3. colocando valores separados por vírgula dentro de colchetes
frutas = ["laranja","maça", "uva"]

# ACESSO DIRETO
frutas = ["laranja","maça", "uva"]
frutas[0] #laranja
frutas[2] #uva

# ÍNDICE NEGATIVO
frutas = ["laranja","maça", "uva"]
frutas[-1] #uva
frutas[-2] #laranja

# LISTA ANINHADA (LISTAS QUE ARMAZENAM LISTAS CRIAM TABELAS)
matriz = [
    [1, "a", 2]
    ["b", 3, 4]
    [6, 5, "c"]
]
matriz[0] # [1,"a",2]
matriz[0][0] # 1
matriz[-1][-1] # "c"
matriz[3][-2] # 4

# FATIAMENTO para acessar valores diretamente
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[0:3:2] # ["p", "y", "t"]
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::-2] # ["n", "o, "h", "t", "y", "p"]

# ITERAR LISTAS
carros = ["gol", "celta", "palio"]
for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f'{indice}:{carro}')

# COMPRESSÃO DE LISTAS
numeros = [1, 30, 21, 2]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# python
numeros = [1, 30, 21, 2]
pares = [numero for numero in numeros if numero % 2 == 0]

# MODIFICAR VALOR
numeros = [1, 30, 21, 2]
quadrado = [numero **2 for numero in numeros]

# MÉTODOS DA CLASSE LIST
[].append # unir
[].clear # limpar
[].copy # copia e cria nova lista
[].count # quantidade de vezes um objeto aparece
[].extend # unir listas sem tirar objetos repetidos
[].index # acha a PRIMEIRA ocorrência de um objeto
[].pop # tirar o último objeto "PRATO" da lista
[].remove # tira a primeira ocorrência de um objeto específico
[].reverse #espelhamento 
[].sort # ordena a lista alfabeticamente
len # mostra a quantidade de elementos
sorted # ordena por ordem alfabetica