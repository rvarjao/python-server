import sqlite3

conn = sqlite3.connect("escola.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT
)
""")

conn.commit()

while True:
    print("\n=== Sistema de Cadastro de Alunos ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        conn.execute("INSERT INTO alunos (nome) VALUES (?)",(nome,))
        conn.commit()
        print("Aluno salvo no banco!")

    elif opcao == "2":
        cursor = conn.execute("SELECT * FROM alunos")
        print("\nLista de alunos:")
        for aluno in cursor:
            print(aluno)

    elif opcao == "3":
        break

conn.close()