# ESTRUTURA DE DADOS SET.

# SET representa conjuntos matemáticos sem objetos repetidos
# ou elimina itens duplicados de um iterável
# porém não garante a ordem

numeros = set([1,2,3,1,4])
print(numeros)

letras = set(["a","b","a","c","a","x","i"])
print(letras)

# para acessar os valores dos conjuntos é necessário converter o set em lista

numeros = {1,2,3,4}

numeros = list(numeros)

print(numeros[0])

# ITERAR/percorrer OBJETOS usando conmando for
# FUNÇÃO ENUMERATE usada para saber qual o índice do objeto dentro do for
carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# {}.union unir os conjuntos
# {}.intersection seleciona o que tem em comum entre os conjuntos
# {}.difference seleciona o que tem de diferente entre os conjuntos
# {}.symmetric_difference a diferença simétrica entre os conjuntos
# {}.issubset verifica se um conjunto está dentro de outro
# {}. issuperset verifica se um conjunto contém outro
# {}.isdisjoint se um conjunto NÃO pertence ao outro
# {}.add adiciona um elemento do conjunto 
# {}.discard elimina um elemento do conjunto
# {}.clear limpa o conjunto
# {}.copy copia o conjunto
# {}.pop coloca os elementos na ordem e retira SEMPRE o primeiro valor
# {}.remove elimina um elemento mas se o elemento não existe ele dá erro
# len fala qual o tamanho do conjunto, mas não conta repetidos
# in verifica se um elemento está dentro de um elemento
