# forma mais comum de se criar listas
frutas = ["laranja", "maca", "uva"]
print(frutas)
# criar listas vazias   
frutas = []
print(frutas)
# cada letra será um argumento
letras = list("python")
print(letras)
# cria um elemento para cada número do 0 ao 9
numeros = list(range(10))
print(numeros)
# atributos de um carro
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "Sao Paulo", True]
print(carro) 


# ACESSO DIRETO
# acessar por meio de índices a partir de zero
frutas = ["maca", "laranja", "banana"]
print(frutas[0]) #imprime só maca
print(frutas[2]) #imprime só banana
print(frutas) # imprime todas         

# ÍNDICES NEGATIVOS
frutas = ["maca", "laranja", "banana"]
print(frutas[-1]) #imprime só banana
print(frutas[-2]) #imprime só laranja
        
# LISTAS ANINHADAS
# listas dentro de listas
matriz = [
    [1, 4, "a"]
    ["b", 2, 0]
    [6, 5, "c"]
]

print(matriz[0]) # valor de uma linha
print(matriz[0][0]) # linha x coluna
print(matriz[-1][2]) # linha x coluna
print(matriz[-1][3]) # linha x coluna

# FATIAMENTO
# passar valor inicial/final para acessar um conjunto de elementos
lista = [2, 5, 0, 3, 7, 1]

lista[2:] # começa do segundo
lista[:2] # pega os dois primeiros
lista[1:3] # 
lista[0:3:2] #
lista[::] # vazio total retorna tudo
lista[::-1] # inverter a declaração de uma lista

# ITERAR AS LISTAS
# fazer leitura dos elementos e filtrar
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

numeros = [1,30,21,2,9,65,34]
pares = [numero for numero in numeros if numero % 2 == 0]

# TRABALHANDO COM LISTAS EM PYTHON
# [].append adiciona um novo elemento no fim da lista
# [].clear limpa a lista
# [].copy modifica o id da lista então o que eu faço em um não afeta o outro
# [].count conta a qunatidade de vezes que um objeto aparece 
# [].extend junta duas listas e não elimina os valores duplicados
# [].index para saber a primeira ocorrência de um elemento
# [].pop aparece o "prato" que está por cima, o último elemento da lista, a não ser que alguém selecione o prato que deseja retirar
# [].remove retira apenas a primeira ocorrência de um elemento específico da lista
# [].reverse espelhamento da lista
# [].sort ordena a lista 
# [].len saber a quantidade de elementos
# [].sorted ordena a lista