from controllers.sql import Banco

class Usuarios:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.banco = Banco()

    def login(self):
        try:
            self.banco.conectar()
            usuarios = self.banco.consultar("tb_usuarios")
            for usuario in usuarios:
                if usuario[1] == self.nome and usuario[2] == self.senha:
                    print("Login bem-sucedido!")
                    self.banco.desconectar()
                    return True
            print("Usuário ou senha incorretos!")
            self.banco.desconectar()
            return False
        except Exception as e:
            print(f"Erro ao fazer login: {e}")
            return False
        
    def cadastrar(self):
        try:
            dados = {
                'nome_usuario': self.nome_usuario,
                'senha': self.senha
            }
            self.banco.inserir('tb_usuarios', dados)
            return True
        except Exception as e:
            print(f"Erro ao cadastrar usuário: {e}")
            return False
