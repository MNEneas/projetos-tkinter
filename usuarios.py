from banco import Banco

class Usuarios:

    def __init__ (self, id=None, usuario=None, senha=None):
        self.id = id
        self.usuario = usuario
        self.senha = senha
        self.c = Banco().conexao

    def InserirDados(self, user, sen):
        
        try:
            cursor = self.c.cursor()
            cursor.execute('INSERT INTO usuarios(usuario, senha) VALUES (?,?)',
                      (user, sen))
            
            self.c.commit()
            cursor.close()
            return 'Usuario cadastrado com sucesso'
        except Exception as erro:
            print(erro)

    def SelecionaUser(self, nome):

        try:
            cursor = self.c.cursor()
            cursor.execute('SELECT * FROM usuarios WHERE usuario=?', (nome,))

            resultado = cursor.fetchall()
            cursor.close()
            return print(f"Deu tudo certo e o resultado = {resultado}")
        except Exception as erro:
            print(erro)
            print("Algo deu errado")
