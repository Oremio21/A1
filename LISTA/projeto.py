# ----------------------------------------------------------
# PROGRAMA DE LISTA DE ALUNOS COM ANÁLISE DE IDADE
# ----------------------------------------------------------
# Objetivo:
#   - Armazenar nomes em uma lista
#   - Exibir os alunos cadastrados
#   - Perguntar a idade de cada aluno
#   - Usar if, elif e else para classificar cada aluno por faixa etária
# ----------------------------------------------------------

# Criando uma lista vazia para armazenar os nomes dos alunos
alunos = []

# Pergunta quantos alunos serão cadastrados
quantidade = int(input("Quantos alunos deseja cadastrar? "))

# Loop para coletar os nomes dos alunos
for i in range(quantidade):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    alunos.append(nome)  # Adiciona o nome na lista

print("\n--- LISTA DE ALUNOS CADASTRADOS ---")
for aluno in alunos:
    print(f"- {aluno}")  # Exibe cada nome da lista

print("\n--- CLASSIFICAÇÃO POR IDADE ---")
# Para cada aluno da lista, perguntar idade e classificar
for aluno in alunos:
    idade = int(input(f"Digite a idade de {aluno}: "))

    # Estrutura condicional usando if, elif e else
    if idade < 12:
        classificacao = "Criança"
    elif idade < 18:
        classificacao = "Adolescente"
    elif idade < 60:
        classificacao = "Adulto"
    else:
        classificacao = "Idoso"

    print(f"{aluno} é classificado como: {classificacao}\n")
