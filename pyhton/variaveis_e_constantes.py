#variavel é um valor que não permanece o msm ao longo da execução do programa
#constante é um valor que permanece o msm ao longo da execução do programa

#PYTHON NÃO TEM CONSTANTE
#usamos variáel com nome em letras maísculas (convenção) 

#BOAS PRÁTICAS EM PYTHON:
#padrão de nomes sugestivos em snake case: 
# lucro_da_empresa OK
# B NÃO

nome = 'Guilherme'
idade = 28

nome ='Giovana'
nome,idade = 'Giovana',28
print(nome,idade)

limite_saque_diario = 1000 #OK
lim_saq_di =1000 #NÃO

ESTADOS = ['SP','MG','RJ']
print(ESTADOS)
