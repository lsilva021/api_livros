
# ORIGATORIAMENTE devemos instalar e ativar um ambiente virtual para utilizarmos/trabalharmos um framework

# 1ª passo: importar Flask
# o flask é a pasta e o Flask é o framework
from flask import Flask, request, jsonify
from flask_cors import CORS
# ERRO por nao conigurar o CORS. Faltou o código da linha 14 'CORS(app)'.

import sqlite3

# 2ª passo puxar o Flask e suas funcionalidades para a variável app
app = Flask(__name__)
CORS(app)

@app.route("/")

def Boas_vindas():
    return "<h1>Essa é a sua página inicial</h1>"


@app.route("/pague")

# Toda vez que criarmos uma rota/endpoint, devemos criar uma função em cima dela
def exibaMensagem():
    return "<h2> Pagar as pessoas, faz bem as pessoas!!!</h2>"

@app.route("/caloteira")

def mensagemCalote():
    return "<h3>Pessoas que não pagam, é triste viu...</h3>"



def init_db():

    # Crie o nosso banco de dados com um arquivo 'database.db' e conecte a variável conn
    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS LIVROS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    image_url TEXT NOT NULL
                )
            """
        )

# ESTRUTURA PARA DEIXAR VALORES SALVOS NO BANCO DE DADOS

# Executa uma consulta SQL para contar quantos livros existem na tabela "livros"
# Depois, usa fetchone()[0] para pegar apenas o número da contagem
    quantidade = conn.execute("SELECT COUNT(*) FROM livros").fetchone()[0]

# Se não existir nenhum livro cadastrado (ou seja, quantidade == 0)
    if quantidade == 0:
    
    # Cria uma lista de livros padrão, cada livro é uma tupla com:
    # (título, categoria, autor, link da imagem)
        livros_padrao = [
            ("Harry Potter e a Pedra Filosofal", "Fantasia", "J.K Rowling", "https://images-americanas.b2w.io/produtos/179547/imagens/livro-harry-potter-e-a-pedra-filosofal/179547_1_large.jpg"),
            ("O Príncipe", "Não ficção", "Nicola Maqiavel", "https://m.media-amazon.com/images/I/81h4CdNxdgL.jpg"),
            ("Dom Casmurro", "Romance", "Machado de Assis", "https://m.media-amazon.com/images/I/61Z2bMhGicL.jpg"),
        ]

    # Percorre cada livro da lista de livros padrão
        for livro in livros_padrao:
        # Separa os dados de cada livro em variáveis individuais
            titulo, categoria, autor, image_url = livro
        
        # Insere o livro no banco de dados, preenchendo os campos da tabela
            conn.execute(f'''
                INSERT INTO livros (titulo, categoria, autor, image_url)
                VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
            ''')
        
        # Salva (confirma) a inserção do livro no banco de dados
        conn.commit()


init_db()

@app.route("/doar", methods=["POST"]) # POST recebe informações enviadas pelo cliente . GET puxa as informações
def doar():
    # a variável dados está armazenando as informações recebidas pelo request, e o _json está escrevendo os dados informados em json.
    dados = request.get_json() # request é uma funciolidade do Flask

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")

    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"erro":"Todos os campos sao obrigatórios"}), 400
    #toda vez que quisermos nos comunicar com o database devemos utilizar este comando with sqlite3.connect
    with sqlite3.connect("database.db") as conn:

        conn.execute(f"""
        INSERT INTO LIVROS (titulo, categoria, autor, image_url)
        VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
        """)

        conn.commit() # Serve para salvar nossas alterções.

        return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201


@app.route("/livros", methods=["GET"])
def listar_livros():

    with sqlite3.connect("database.db") as conn:
        livros = conn.execute("SELECT * FROM LIVROS").fetchall() # fetchall serve para traduzir o codigo do banco de dados para python, para que a linguagem entenda o que está acontecendo

        # array criado pra receber os livros formatados
        livros_formatados = []

        # loop que vai formatar as informações dos livros
        for item in livros:
            dicionario_livros = {
                "id":item[0],
                "titulo":item[1],
                "categoria":item[2],
                "autor":item[3],
                "image_url":item[4]
            }
            livros_formatados.append(dicionario_livros)

    return jsonify(livros_formatados)








# Se app.py for o arquivo principal da API, execute o app.run com o modo de debug ativado
if __name__ == "__main__":
    # Inicia o servidor Flask no modo de depuraçao (nessee modo nossa API responde automaticamente a qualquer)
    app.run(debug=True)