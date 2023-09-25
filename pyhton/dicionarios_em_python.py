# DICIONARIO é um conjunto de pareschave:valor separada por vírgulas
# para ser chave o valor tem que ser imutável

pessoa = {"nome":"Guilherme", "idade":28}
pessoa = dict(nomes="Guilherme", idade=28)

# ACESSANDO OS DADOS
# x["y"]

# DICIONARIOS ANINHADOS
# primeiro acessa a primeira chave e depois a segunda
# {}.fromkeys cria as chaves sem valor
# {}get acessar uma chuva  da empresa