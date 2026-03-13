alunos = []

while True:
    print("\n=== Sistema de Cadastro de Alunos ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        alunos.append(nome)
        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        print("\nLista de alunos:")
        for aluno in alunos:
            print("-", aluno)

    elif opcao == "3":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")