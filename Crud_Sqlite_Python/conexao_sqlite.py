import sqlite3

class Comunication():
    def __init__(self):
        self.conexao = sqlite3.connect('../adega.db')
             
    def inserir_produto(self, codigo, nome, modelo, preco, quantidade):
        cursor = self.conexao.cursor()
        bd = 'INSERT INTO tabela_dados (CODIGO, NOME, MODELO, PRECO, QUANTIDADE) VALUES (?, ?, ?, ?, ?)'
        cursor.execute(bd, (codigo, nome, modelo, preco, quantidade))
        self.conexao.commit()
        cursor.close()
        
    def mostrar_produtos(self):
        cursor = self.conexao.cursor()
        bd = 'SELECT id, codigo, nome, modelo, preco, quantidade FROM  tabela_dados'
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro
    
    def busca_produto(self,nome_produto):
        cursor = self.conexao.cursor()
        bd = 'SELECT * FROM tabela_dados WHERE NOME = {}'.format(nome_produto)
        #bd = '''SELECT * FROM tabela_dados WHERE NOME LIKE '%{}%' '''.format(nome_produto)
        #bd = '''SELECT * FROM tabela_dados WHERE NOME LIKE ?'''
        #cursor.execute(bd, ('%' + nome_produto + '%',))
        
        cursor.execute(bd)
        nomeX = cursor.fetchall()
        return nomeX
    
    def elimina_produto(self, id):
        cursor = self.conexao.cursor()
        bd = 'DELETE FROM tabela_dados WHERE id = {}'.format(id)
        cursor.execute(bd)
        self.conexao.commit()
        cursor.close()
    
    def atualiza_produto(self,id, codigo, nome, modelo, preco, quantidade):
        cursor = self.conexao.cursor()
        bd = '''UPDATE tabela_dados SET CODIGO = '{}', NOME = '{}', MODELO = '{}', PRECO = '{}', QUANTIDADE = '{}' WHERE ID = {}'''.format(codigo, nome, modelo, preco, quantidade, id)
        cursor.execute(bd)
        a = cursor.rowcount
        self.conexao.commit()
        cursor.close()
        return a
