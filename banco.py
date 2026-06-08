import sqlite3

class Banco():
    def __init__ (self):
        self.conexao = sqlite3.connect('banco.bd')
        self.c = self.conexao.cursor()
        self.CriarTabela()

    def CriarTabela(self):

        query = 'CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT UNIQUE, senha TEXT)'
        self.c.execute(query)

        self.conexao.commit()
        self.c.close()