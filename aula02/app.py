import sqlite3

# se conecta com o banco de dados escola.db, ou cria o arquivo se ele não existir
conn = sqlite3.connect("escola.db")

# ler o arquivo ../schema.sql e executar as instruções SQL contidas nele
# é o mesmo que fizemos manualmente quando colocamos o conteúdo
# do arquivo no dbFiddle, mas agora automatizado no código Python
# isso é útil para criar as tabelas e a estrutura do banco de dados de forma programática
# deve verificar se o banco de dados já existe antes de executar o script, para evitar erros de tabela já existente
dbExiste = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='alunos'").fetchone() is not None
if not dbExiste:
    schemaDb = open("../schema.sql").read()
    conn.executescript(schemaDb)


while True:
    print("\n=== Sistema de Cadastro de Alunos ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        data_nascimento = input("Data de nascimento: ")
        # inserir um novo registro na tabela alunos usando SQL
        # os valores são passados como parâmetros para evitar problemas de segurança (SQL injection)
        conn.execute("INSERT INTO alunos (nome, email, data_nascimento) VALUES (?, ?, ?)", (nome, email, data_nascimento))
        conn.commit()  # salvar as alterações no banco de dados
        print("Aluno cadastrado com sucesso!")


    elif opcao == "2":
        cursor = conn.execute("SELECT id, nome, email, data_nascimento FROM alunos")
        print("\nLista de alunos:")
        for aluno in cursor:
            print(aluno)

    elif opcao == "3":
        break

conn.close()