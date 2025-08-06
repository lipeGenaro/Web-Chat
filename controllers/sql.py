import sqlite3
from datetime import datetime

class Banco:
    def __init__(self):
        self.conexao = None
        self.cursor = None

    def conectar(self):
        self.conexao = sqlite3.connect("models/chatbot.db")
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        if self.conexao: 
            self.conexao.close()

    def inserir(self, tabela, dados: dict):
        self.conectar()
        colunas = ", ".join(dados.keys())
        valores = ", ".join(['?'] * len(dados))
        lista = list(dados.values())
        sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"
        self.cursor.execute(sql, lista)
        self.conexao.commit()
        self.desconectar()

    def consultar(self, tabela):
        self.conectar()
        sql = f"SELECT * FROM {tabela}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.desconectar()
        return resultado

    def inserir_mensagem(self, id_usuario, mensagem, imagem=None):
        try:
            self.conectar()
            sql = "INSERT INTO tb_chat (id_usuario, mensagem, imagem, data) VALUES (?, ?, ?, ?)"
            data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Obtendo a data atual
            self.cursor.execute(sql, (id_usuario, mensagem, imagem, data_atual))
            self.conexao.commit()
            self.desconectar()
        except Exception as e:
            print(f"Erro ao inserir mensagem: {e}")
            self.desconectar()
