from controllers.usuarios import Usuarios
from controllers.sql import Banco

class Chat:
    def __init__(self, mensagem, nome_usuario):
        self.mensagem = mensagem
        self.banco = Banco()
        self.usuarios = Usuarios(nome_usuario, senha=None)

    def enviar_mensagem(self):
        try:
            if not self.usuarios.login():  
                print("Usuário não autenticado!")
                return

            dados = {
                "mensagem": self.mensagem,
                "usuario": self.usuarios.nome
            }

    
            self.banco.inserir("tb_chat", dados)

        except Exception as e:
            print(f"Erro ao enviar a mensagem: {e}")



    









