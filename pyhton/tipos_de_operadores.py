# OPERADORES ARITMÉTICOS

# adição
print (1 + 1)

# subtração
print (1 - 1)

# multiplicação
print (1 * 1)

# divisão
print (1 / 1) # número float

# divisão inteira
print (1 // 1)

# módulo
print (1 % 1)

# exponenciação 
print (1 ** 1)

produto_1 = 10
produto_2 =  20

print(produto_1+produto_2)
print(produto_1-produto_2)
print(produto_1/produto_2)
print(produto_1//produto_2)
print(produto_1%produto_2)
print(produto_1**produto_2)

#PYTHON SEGUE A PRECEDÊNCIA DA MATEMÁTICA DE ORDEM DAS OPERAÇÕES:
x = 10-5*2
y = 10/0.5 + ((2-1) ** 4)
print(x)
print(y)

# OPERADORES DE COMPARAÇÃO : resultado é bool (V/F)
# igualdade ==
# diferença !=
# maior ou igual é > OU >=
# menor ou igual é < OU <=

saldo = 200
saque = 200
print(saldo==saque)
print(saldo!= saque)
print(saldo>=saque)
print(saldo>saque)
print(saldo<=saque)
print(saldo<saque)


# OPERADORES DE ATRIBUIÇÃO : define valor inicial ou sobrescrever valor de variável
saldo = 500 #atribui 500 a variável saldo
saldo += 200 #atribui com soma no valor da variável
saldo -= 200 #atribui com subtração no valor da variável
saldo *= 200 #atribui com multiplicação no valor da variável
saldo /= 200 #atribui com divisão no valor da variável
saldo //= 200 #atribui com divisão no valor da variável
saldo %= 200 #atribui com soma no valor da variável
saldo **= 200 #atribui com soma no valor da variável


# OPERADORES LÓGICOS : resultado bool (V/F)
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite #operador E: and; TRUE se todos são true
saldo >= saque or saque <= limite #operador OU: or; TRUE se um for true
not 100>150 #operador negação: not


# OPERADORES DE IDENTIDADE : comparar se dois objetos ocupam a mesma posição na memória; resultao bool (V?F)
saldo, limite = 200,200
saldo is limite
saldo is not limite 

# OPERADORES DE ASSOCIAÇÃO : verifica se um objeto está presente em uma sequência
saques = [1500, 100]
200 in saques
100 not in saques
1500 in saques 