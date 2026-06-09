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
            print("Usuario cadastrado com sucesso")
        except Exception:
            print("Usuario ja adicionado")

    def SelecionaUser(self, nome):

        try:

            cursor = self.c.cursor()
            cursor.execute('SELECT * FROM usuarios WHERE usuario=?', (nome,))
            resultado = cursor.fetchone()
            cursor.close()

            if resultado != []:
                print(f"A senha de {resultado[1]}: {resultado[2]}")
            else:
                print("Usuario nao existe")
        except Exception as erro:
            print(erro)

    def DeletarUser(self, nome):

        try:

            cursor = self.c.cursor()
            cursor.execute('DELETE FROM usuarios WHERE usuario=?', (nome,))
            cursor.close()
            self.c.commit()

            if cursor.rowcount == 0:
                print("Usuario nao encontrado")
            else:
                print("Usuario deletado com sucesso")
            
        except Exception as error:
            print(error)

    def AtualizarSenha(self, usuario, novasenha):

        try:
            cursor = self.c.cursor()
            cursor.execute('UPDATE usuarios SET senha = ? WHERE usuario = ?', (novasenha, usuario))

            cursor.close()
            self.c.commit()

            if cursor.rowcount > 0:
                print(f"Senha do {usuario} atualizada!")
            else:
                print("Usuario nao encontrado")
        
        except Exception as error:
            print(error)
