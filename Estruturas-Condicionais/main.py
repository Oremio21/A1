idade = int(input("Digite sua idade: ")) # Declarado o valor da variavel 

if idade < 18: # se a idade do usuário for abaixo de 18, não será permitida a entrada no evento 
    print("Você não pode entrar no evento") # imprimida a idade
elif idade >= 50: # se o usuário for mais velho que 50 anos, não poderá entrar no evento
    print("Você é velho para o evento") # imprimida a mensagem de negação de entrada
else: # se não se aplicar e ele tenha entre 18 e 49 anos poderá entrar no evento 
    print("Você pode ir para o evento, aproveite!") # imprimida a mensagem de permissão de entrada