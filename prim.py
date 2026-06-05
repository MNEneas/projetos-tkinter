import tkinter as tk

class Application:
    def __init__(self, master):
      self.widget1 = tk.Frame(master)
      self.widget1.pack()

      self.msg = tk.Label(self.widget1, text="Primeiro widget")
      self.msg.pack ()


root = tk.Tk()
Application(root)
root.mainloop()