import tkinter as tk
from usuarios import Usuarios

class HomePage:
    def __init__ (self, master):

        self.user = Usuarios()

        self.titulo_inicial = tk.Frame(master)
        self.titulo_inicial["pady"] = 10
        self.titulo_inicial.pack()

        self.adiciona_usuario = tk.Frame(master)
        self.adiciona_usuario["padx"] = 20
        self.adiciona_usuario.pack()

        self.adiciona_senha = tk.Frame(master)
        self.adiciona_senha["padx"] = 20
        self.adiciona_senha.pack()

        self.botao_adicionar = tk.Frame(master)
        self.botao_adicionar["padx"] = 20
        self.botao_adicionar.pack()

        self.titulo_visualizar = tk.Frame(master)
        self.titulo_visualizar["pady"] = 10
        self.titulo_visualizar.pack()

        self.visualizar_usuario = tk.Frame(master)
        self.visualizar_usuario["padx"] = 20
        self.visualizar_usuario.pack()

        self.botao_visualizar_deletar = tk.Frame(master)
        self.botao_visualizar_deletar["padx"] = 20
        self.botao_visualizar_deletar.pack()

        self.atualiza_usuario = tk.Frame(master)
        self.atualiza_usuario["padx"] = 20
        self.atualiza_usuario.pack()

        self.atualiza_senha = tk.Frame(master)
        self.atualiza_senha["padx"] = 20
        self.atualiza_senha.pack()

        self.botao_atualizar = tk.Frame(master)
        self.botao_atualizar["padx"] = 20
        self.botao_atualizar.pack()

        self.label1 = tk.Label(
            self.titulo_inicial,
            text='Adicione um usuario e senha'
        )
        self.label1.pack()

        self.usuariolabel = tk.Label(self.adiciona_usuario, text = "Usuário")
        self.usuariolabel["font"] = ("Arial", "10", "bold")
        self.usuariolabel.pack(side=tk.LEFT)

        self.usuario = tk.Entry(self.adiciona_usuario)
        self.usuario["width"] = 30
        self.usuario.pack(side=tk.LEFT)
        
        self.senhalabel = tk.Label(self.adiciona_senha, text = "Senha")
        self.senhalabel["font"] = ("Arial", "10", "bold")
        self.senhalabel.pack(side=tk.LEFT)

        self.senha = tk.Entry(self.adiciona_senha)
        self.senha["width"] = 30
        self.senha["show"] = "*"
        self.senha.pack(side=tk.LEFT)
        
        self.botao = tk.Button(
            self.botao_adicionar,
            text="Adicionar",
            font=("Calibri", "10"),
            width=7,
            command=lambda: self.user.InserirDados(
            self.usuario.get(),
            self.senha.get()
            ))
        self.botao.pack()
        
        self.label2 = tk.Label(
            self.titulo_visualizar,
            text='visualizar senha do usuario'
        )

        self.usuariolabel2 = tk.Label(self.visualizar_usuario, text = "Usuário")
        self.usuariolabel2["font"] = ("Arial", "10", "bold")
        self.usuariolabel2.pack(side=tk.LEFT)

        self.usuario2 = tk.Entry(self.visualizar_usuario)
        self.usuario2["width"] = 30
        self.usuario2.pack(side=tk.LEFT)

        self.botao2 = tk.Button(
            self.botao_visualizar_deletar,
            text="Select",
            font=("Calibri", "10"),
            width=5,
            command=lambda: self.user.SelecionaUser(self.usuario2.get())
            )
        self.botao2.pack()

        self.botao3 = tk.Button(
            self.botao_visualizar_deletar,
            text="Delete",
            font=("Calibri", "10"),
            width=5,
            command=lambda: self.user.DeletarUser(self.usuario2.get())
            )
        self.botao3.pack()

        self.usuariolabel3 = tk.Label(self.atualiza_usuario, text="Usuario")
        self.usuariolabel3["font"] = ("Arial", "10", "bold")
        self.usuariolabel3.pack(side=tk.LEFT)

        self.usuario3 = tk.Entry(self.atualiza_usuario)
        self.usuario3["width"] = 30
        self.usuario3.pack(side=tk.LEFT)

        self.senhalabel2 = tk.Label(self.atualiza_senha, text="Nova Senha")
        self.senhalabel2["font"] = ("Arial", "10", "bold")
        self.senhalabel2.pack(side=tk.LEFT)


        self.senha3 = tk.Entry(self.atualiza_senha)
        self.senha3["width"] = 30
        self.senha3["show"] = "*"
        self.senha3.pack(side= tk.LEFT)

        self.botao4 = tk.Button(
            self.botao_atualizar,
            text="Atualizar senha",
            font=("Calibri", "10"),
            width=12,
            command=lambda: self.user.AtualizarSenha(self.usuario3.get(), self.senha3.get())
        )
        self.botao4.pack()