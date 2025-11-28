alunos = [] #lista de armazenamento 

lista = open("alunos.txt", "r") #abre a lista em modo "r" = read / leitura 
for linha in lista:  #loop / for = para / in = em 
    alunos = alunos + [linha] 
lista.close() #fecha

print("Lista de Alunos:") #imprime o nome "Lista de Alunos:"
for aluno in alunos:  #mesma coisa que a linha 4
    print(aluno) #chama a variavel alunos, agora chamando o .txt "alunos"