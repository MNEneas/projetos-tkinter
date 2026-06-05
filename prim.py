import tkinter as tk

class Application:
    def __init__(self, master):
        self.widget1 = tk.Frame(master)
        self.widget1.pack()

        self.msg = tk.Label(self.widget1, text="Mudar")
        self.msg.pack ()

        self.botao = tk.Button( #juntando tudo em um só
            self.widget1,
            text="Click",
            font=("Calibri", "10"),
            width=5,
            #command=self.widget1.quit
            )
        self.botao.bind("<Button-1>", self.mudar_texto) # bind serve para não so capturar um click mas também qual click foi dado
                                                        # "<Button-1>" é o click esquerdo do mouse "<Button-2>" o do scroll"
                                                        # <Button-3>" o direito
      
        #self.botao["text"] = ("Sair") daria para fazer isso também
        #self.botao["font"] = ("Calibri", "10")
        #self.botao["width"] = 5
        #self.botao["command"] = self.widget1.quit

        self.botao.pack() #da para movimentar o botao com side e para onde ir


    def mudar_texto(self, event):
        if self.msg["text"]=="Mudar":
           self.msg["text"]="Mudar novamente"
        else:
           self.msg["text"]="Mudar"
           
    # def mudar_texto(self):        caso use command e nao bind como: command = self.mudar_texto
    #    if self.msg["text"]=="Mudar":
    #       self.msg["text"]="Mudar novamente"
    #    else:
    #       self.msg["text"]="Mudar"
           
       

root = tk.Tk()
Application(root)
root.mainloop()