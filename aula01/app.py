# armazenar os alunos em uma lista
# cada aluno é representado por um dicionário com as chaves 'nome', 'turma' e 'idade'
alunos = []

# while True cria um loop infinito, ou seja,
# o código dentro do bloco será executado repetidamente até que
# uma condição de parada seja atingida
# (neste caso, a opção "3" para sair do sistema)
while True:
    # cuidado com a indentação,
    # pois ela define o escopo do código dentro do loop
    # no scratch, a indentação é representada por blocos de código
    # que se encaixam
    print("\n=== Sistema de Cadastro de Alunos ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    # input é usado para ler a entrada do usuário,
    # e o texto dentro dos parênteses é exibido como um prompt
    opcao = input("Escolha uma opção: ")

    # if representa uma estrutura de decisão, onde o código dentro do bloco é executado apenas se a condição for verdadeira
    if opcao == "1":
        nome = input("Nome: ")
        turma = input("Turma: ")
        data_nascimento = input("Data de nascimento: ")

        # adicionar o aluno à lista de alunos
        # cada registro é um dicionário com as informações do aluno
        # não estamos validando os dados de entrada, mas isso pode ser melhorado posteriormente
        alunos.append({"nome": nome, "turma": turma, "data_nascimento": data_nascimento})
        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        print("\nLista de alunos:")

        # for significa "para cada" e é usado para iterar sobre os elementos de uma lista
        for aluno in alunos:
            print("-", aluno)

    elif opcao == "3":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")
