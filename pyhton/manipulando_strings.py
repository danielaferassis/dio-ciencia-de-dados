
# MAIÚSCULO E MINÚSCULO
curso = "pYthOn"
# tudo maiúsculo
print(curso.upper())
# tudo minúsculo
print(curso.lower())
# primeira letra maiúsculo
print(curso.title())

# ELIMINAR ESPAÇOS
curso = " Python   "
# eliminando todos os espaços
print(curso.strip())
# eliminando o espaço da esquerda
print(curso.lstrip())
# eliminando o espaço da direita
print(curso.rstrip())

# CENTRALIZAR E JUNTAR
curso = "Python"
# centralização e preenchimento de caracteres
print(curso.center(10,"#"))
# junção
print(".".join(curso))

# INTERPOLAR VARIÁVEIS
# Old Style
nome = "Guilherme" # %s para valores do tipo string
idade = 28 # %d para valores inteiros
profissao = "Programador" # %s para valores do tipo string
linguagem = "Python" # %s para valores do tipo string
# %f para valores tipo ponto flutuante

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# Método Format
nome = "Guilherme" 
idade = 28 
profissao = "Programador" 
linguagem = "Python" 

# com {} e mantendo a ordem correta
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
# colocando a posição da variável na ordem desejada
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))
# com {nome da variável} e se referindo na variável depois
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
# se referindo ao dicionario
# print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))

# F-STRING
nome = "Guilherme" 
idade = 28 
profissao = "Programador" 
linguagem = "Python"
# colocar f antes do frase
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

PI = 3.14159
 
# número de casas depois do ponto
print(f"Valor de PI: {PI:.2f}")
# colocar espaço antes do início do ponto
print(f"Valor de PI: {PI:10.2f}")

# FATIAMENTO DE STRINGS
nome = "Daniela Sofia Fernandes de Assis"
# [start: stop[, step]]
# apenas primeira  letra
print(nome[0])
# oito primeiras letras
print(nome[:8])
# começa no 10 e vai até o fim
print(nome[10:])
# começa no dez e para no 16
print(nome[10:16])
# começa no dez para no 16 e pula de dois em dois
print(nome[10:16:2])
# retornar a string inteira
print(nome[:])
# espelhamento
print(nome[::-1])

# STRING DE MÚLTIPLAS LINHAS
nome = "Guilherme"

mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo Python
"""
print(mensagem)