import tkinter as tk

class Application:
    def __init__(self, master):
      self.widget1 = tk.Frame(master)
      self.widget1.pack()

      self.msg = tk.Label(self.widget1, text="Primeiro widget")
      self.msg.pack ()

      self.botao = tk.Button(self.widget1, text="Sair")
      #self.botao["text"] = ("Sair") daria para fazer isso também
      self.botao["font"] = ("Calibri", "10")
      self.botao["width"] = 5
      self.botao["command"] = self.widget1.quit
      self.botao.pack(side="right") #da para movimentar o botao com side e para onde ir


root = tk.Tk()
Application(root)
root.mainloop()