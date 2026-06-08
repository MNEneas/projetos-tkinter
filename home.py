import tkinter as tk
from usuarios import Usuarios
from banco import Banco

class HomePage:
    def __init__ (self, master):

        self.user = Usuarios()

        self.box1 = tk.Frame(master)
        self.box1["pady"] = 10
        self.box1.pack()

        self.box2 = tk.Frame(master)
        self.box2["padx"] = 20
        self.box2.pack()

        self.box3 = tk.Frame(master)
        self.box3["padx"] = 20
        self.box3.pack()

        self.box4 = tk.Frame(master)
        self.box4["padx"] = 20
        self.box4.pack()

        self.box5 = tk.Frame(master)
        self.box5["pady"] = 10
        self.box5.pack()

        self.box6 = tk.Frame(master)
        self.box6["padx"] = 20
        self.box6.pack()

        self.box7 = tk.Frame(master)
        self.box7["padx"] = 20
        self.box7.pack()

        self.box8 = tk.Frame(master)
        self.box8["padx"] = 20
        self.box8.pack()

        self.label1 = tk.Label(
            self.box1,
            text='Adicione um usuario e senha'
        )
        self.label1.pack()

        self.usuariolabel = tk.Label(self.box2, text = "Usuário")
        self.usuariolabel["font"] = ("Arial", "10", "bold")
        self.usuariolabel.pack(side=tk.LEFT)

        self.usuario = tk.Entry(self.box2)
        self.usuario["width"] = 30
        self.usuario.pack(side=tk.LEFT)
        
        self.senhalabel = tk.Label(self.box3, text = "Senha")
        self.senhalabel["font"] = ("Arial", "10", "bold")
        self.senhalabel.pack(side=tk.LEFT)

        self.senha = tk.Entry(self.box3)
        self.senha["width"] = 30
        self.senha["show"] = "*"
        self.senha.pack(side=tk.LEFT)
        
        self.botao = tk.Button(
            self.box4,
            text="Adicionar",
            font=("Calibri", "10"),
            width=7,
            command=lambda: self.user.InserirDados(
            self.usuario.get(),
            self.senha.get()
            ))
        self.botao.pack()
        
        self.label2 = tk.Label(
            self.box5,
            text='visualizar senha do usuario'
        )

        self.usuariolabel2 = tk.Label(self.box6, text = "Usuário")
        self.usuariolabel2["font"] = ("Arial", "10", "bold")
        self.usuariolabel2.pack(side=tk.LEFT)

        self.usuario2 = tk.Entry(self.box6)
        self.usuario2["width"] = 30
        self.usuario2.pack(side=tk.LEFT)

        self.botao2 = tk.Button(
            self.box7,
            text="Select",
            font=("Calibri", "10"),
            width=5,
            command=lambda: self.user.SelecionaUser(self.usuario2.get())
            )
        self.botao2.pack()

        self.botao3 = tk.Button(
            self.box7,
            text="Delete",
            font=("Calibri", "10"),
            width=5,
            command=lambda: self.user.DeletarUser(self.usuario2.get())
            )
        self.botao3.pack()