import tkinter as tk

class Application:
    def __init__(self, master):
        self.fontepadrao = ("Arial", "10")

        self.widget1 = tk.Frame(master)
        self.widget1["pady"]=10
        self.widget1.pack()

        self.widget2 = tk.Frame(master)
        self.widget2["padx"]=20
        self.widget2.pack()

        self.widget3 = tk.Frame(master)
        self.widget3["padx"] = 20
        self.widget3.pack()

        self.widget4 = tk.Frame(master)
        self.widget4["padx"] = 20
        self.widget4.pack()

        self.titulo = tk.Label(self.widget1, text="Dados do Usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack ()

        self.usuariolabel = tk.Label(self.widget2, text = "Usuário")
        self.usuariolabel["font"] = ("Arial", "10", "bold")
        self.usuariolabel.pack(side=tk.LEFT)

        self.usuario = tk.Entry(self.widget2)
        self.usuario["width"] = 30
        self.usuario["font"] = self.fontepadrao
        self.usuario.pack(side=tk.LEFT)

        self.senhalabel = tk.Label(self.widget3, text = "Senha")
        self.senhalabel["font"] = ("Arial", "10", "bold")
        self.senhalabel.pack(side=tk.LEFT)

        self.senha = tk.Entry(self.widget3)
        self.senha["width"] = 30
        self.senha["font"] = self.fontepadrao
        self.senha["show"] = "*"
        self.senha.pack(side=tk.LEFT)

        self.botao = tk.Button( #juntando tudo em um só
            self.widget4,
            text="Click",
            font=("Calibri", "10"),
            width=5,
            command=self.autenticacao
            )
        
        self.labelaut = tk.Label(self.widget4, text = "", font = self.fontepadrao)
        self.labelaut.pack()

        #self.botao.bind("<Button-1>", self.mudar_texto) # bind serve para não so capturar um click mas também qual click foi dado
                                                        # "<Button-1>" é o click esquerdo do mouse "<Button-2>" o do scroll"
                                                        # <Button-3>" o direito
      
        #self.botao["text"] = ("Sair") daria para fazer isso também
        #self.botao["font"] = ("Calibri", "10")
        #self.botao["width"] = 5
        #self.botao["command"] = self.widget1.quit

        self.botao.pack() #da para movimentar o botao com side e para onde ir
           
    # def mudar_texto(self):        caso use command e nao bind como: command = self.mudar_texto
    #    if self.msg["text"]=="Mudar":
    #       self.msg["text"]="Mudar novamente"
    #    else:
    #       self.msg["text"]="Mudar"



    def autenticacao(self):

        nome = self.usuario.get()
        senha = self.senha.get()

        if nome == "Eneas" and senha == "1234":
            self.labelaut["text"] = "Você foi autenticado"  
        else:
            self.labelaut["text"] = "Você não foi autenticado"    
       

app = tk.Tk()
Application(app)
app.mainloop()