# FUNÇÕES são blocos de código que tornam o código mais legível e possibilita o reaproveitamento de código

# DECLARAR FUNÇÃO
# def nome(argumento):
#   print()
# def informa o interpretador que nome é um identificador

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo {nome}")

# CHAMAR FUNÇÃO
# nome do identificador da função(argumento)

exibir_mensagem()
exibir_mensagem_2(nome="Gui")
exibir_mensagem_2("Gui")

# RETORNANDO VALORES
# return é a função para retornar valores 
# se eu ñ definir valores Pyhton define como anônimo/nulo

def calcular_total(numeros):
    return sum(numeros)

# ARGUMENTO NOMEADO
# chave=valor

def salvar_carro(marca, modelo, ano, placa):
    #salva carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat","Palio",1999,"ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

# ARGS E KWARGS 
# *arg renderiza como tupla
# **kwargs renderiza como dicionário

# PRÂMETROS ESPECIAIS
def f(pos1, pos2, /, pos_or_kwd, *, kw1, kw2):
    print()

# PARÂMETROS APENAS POR POSIÇÃO
# def f(pos 1, pos 2, /, pos_or_kwd):
#   print()

def criar_carro(modelo, ano, placa):
    print(modelo, ano, placa)

criar_carro("Palio", 1999, "ABC-1234")

# PARÂMETROS APENAS POR NOME
# def f(*, kwd1, kwd2, ...):
#   print()

def criar_carro(*, modelo, ano, placa):
    print(modelo, ano, placa)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234")

# PARÂMETROS POR NOME OU POSIÇÃO
# def f(pos 1, pos 2, /, pos_or_kwd):
#   print():

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# OBJETOS DE PRIMEIRA CLASSE
# objeto: parâmetro para funções, valores em estruturas de dados e valor de trtorno de uma função

def somar(a, b):
    return a+ b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)

# ESCOPO LOCAL E ESCOPO GLOBAL
# palavra-chave global informa que a variável está no escopo global = Ñ É UMA BOA PRÁTICA

salario = 2000

def salario_bonus(bonus):
    global salario # busca a função salário que está no escopo global
    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista) #2500
print(salario_com_bonus)
print(lista)


