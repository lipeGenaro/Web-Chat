from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send
from controllers.usuarios import Usuarios
from controllers.sql import Banco

app = Flask(__name__)
socketio = SocketIO(app)

# Rota para login
@app.route('/')
def login():
    return render_template('login.html')

# Rota para autenticação
@app.route('/login', methods=['POST'])
def do_login():
    nome_usuario = request.form['nome']
    senha = request.form['senha']
    usuario = Usuarios(nome_usuario, senha)
    
    if usuario.login():
        return redirect(url_for('chat', nome_usuario=nome_usuario))
    else:
        return redirect(url_for('login'))
    
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome_usuario = request.form['nome']
        senha = request.form['senha']
        
        usuario = Usuarios(nome_usuario, senha)
        if usuario.cadastrar():
            return redirect(url_for('login'))
        else:
            return render_template('cadastro.html', erro="Erro ao cadastrar usuário")
    
    return render_template('cadastro.html')

# Rota para chat
@app.route('/chat')
def chat():
    nome_usuario = request.args.get('nome_usuario')
    return render_template('chatweb.html', nome_usuario=nome_usuario)

# Rota para enviar a mensagem via Socket
@socketio.on('message')
def handle_message(data):
    nome_usuario = data['nome_usuario']
    mensagem = data['mensagem']

    banco = Banco()
    banco.inserir_mensagem(nome_usuario, mensagem)

    send({
        'nome_usuario': nome_usuario,
        'mensagem': mensagem
    }, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=80)
