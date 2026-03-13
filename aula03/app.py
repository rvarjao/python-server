from flask import Flask
import sqlite3

app = Flask(__name__)

def get_alunos():
    conn = sqlite3.connect("escola.db")
    cursor = conn.execute("SELECT nome FROM alunos")
    alunos = [row[0] for row in cursor]
    conn.close()
    return alunos

@app.route("/")
def home():
    alunos = get_alunos()

    html = "<h1>Lista de alunos</h1>"
    html += "<ul>"

    for aluno in alunos:
        html += f"<li>{aluno}</li>"

    html += "</ul>"
    return html

app.run(debug=True)