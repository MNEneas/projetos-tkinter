import tkinter as tk

janela=tk.Tk()

janela.geometry("300x400")
janela.title("Minha Janela")

l1 = tk.Label(text="Test", fg="black", bg="white")
l1.place(x=100, y=50)#tem o grid e pack para adicionar

botao=tk.Button(janela, text="Clique aqui")
botao.pack()

entrada=tk.Entry(janela)
entrada.pack()

janela.mainloop() #Para manter a janela aberta até que seja fechada