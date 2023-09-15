# IDENTAÇÃO E BLOCOS
# Identar um código auxilia o interpretador conseguir identificar onde um bloco começa e termina
# Em Pyhton, se coloca 4 espaços para cada nova adição dentro de um bloco
# Python inicia um bloco com ":"

# ESTRUTURAS CONDICIONAIS permitem o desvio de fluxo de controle

# IF testa a expressão lógica e em caso de retorno V as ações serão executadas
MAIOR_IDADE = 18

idade = input("Informe a sua idade")

if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar CNH.")

if idade < MAIOR_IDADE:
    print("Menor de idade não pode tirar CNH.")
# IF/ELSE testa a expressão lógica do IF e em caso de retorno V o IF será executado, 
#caso contrário o ELSE será executado
MAIOR_IDADE = 18

idade = input("Informe a sua idade")

if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar CNH.")

else:
    print("Menor de idade não pode tirar CNH.")
# IF/ELIF/ELSE testa a expressão lógica do IF e em caso de retorno V o IF será executado, 
#caso contrário o ELIF e, posteiormente, o ELSE será executado se o ELIF der F
MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = input("Informe a sua idade")

if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas.")
else:
    print("Menor de idade não pode tirar CNH.")
# IF ANINHADO possuem estruturas if/elif/else dentro de bloco de estruturas if/elif/else
conta_normal = True
saldo = 2000
saque = 500
cheque_especial = 450
conta_universitaria = False 
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do chque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    else:
        print("Saldo insuficiente!")
 # IF TERNÁRIO serve para escrever uma condição em uma única linha
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")

# ESTRUTURAS DE REPETIÇÃO são utilizadas para repetir um trecho de código um determinado nº de vezes

# FOR para quando sabemos o nº de repetições
texto = input("Informe um texto: ")
VOGAIS  = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() # adiciona uma quebra de linha
# FOR/ELSE 
texto = input("Informe um texto: ")
VOGAIS  = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço")

# FUNÇÃO RANGE é utilizada para produzir uma sequência de números inteiros a partir de um início (inclusivo) para um fim (exclusivo)
# Ela recebe os argumentos STOP, START, STEP
list(range(4))

# RANGE COM FOR
for numero in range(0, 11):
    print(numero, end=" ")


# WHILE para quando não sabemos o númro de repetições

# BREAK para quando estamos repetindo e precisamos parar
# CONTINUE para quando queremos pular uma execução