import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.uic import loadUi
from conexao_sqlite import Comunication
import time

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super(JanelaPrincipal, self).__init__()
        loadUi('AdegaV3.ui', self)
        self.tabela_produtos.setColumnWidth(6,120) #mantendo a coluna dos botões estreita (120 pixels)
        self.tabela_produtos.setColumnWidth(0,80)  #mantendo a coluna do id estreita (80 pixels)
        
        #conectando com o banco de dados, janela maximizada, iniciando com a base de dados (mostrar_produtos)
        self.adega = Comunication()
        self.showMaximized()
        self.mostrar_produtos()
        
        #Título da janela e ícone
        self.setWindowTitle("Base de Dados")
        self.setWindowIcon(QtGui.QIcon("imagens/icone.png"))
        
        #conexao botões
        self.bt_dados_geral.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_dados))
        self.bt_registrar_geral.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
        
        #botões
        self.bt_atualizar_base.clicked.connect(self.mostrar_produtos)
        self.bt_registrar.clicked.connect(self.registrar_produto)
        self.bt_buscar.clicked.connect(self.busca_por_nome)
        
        #colunas adaptaveis para ocupar toda a tela, exceto a coluna do id e de ações
        #self.tabela_produtos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela_produtos.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tabela_produtos.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.tabela_produtos.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.tabela_produtos.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.tabela_produtos.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        
        #validação do campo reg_codigo e quantidade para receber apenas números
        reg_ex = QtCore.QRegExp("[0-9]+")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.reg_codigo)
        self.reg_codigo.setValidator(input_validator)
        
        reg_ex = QtCore.QRegExp("[0-9]+")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.reg_qtd)
        self.reg_qtd.setValidator(input_validator)
        
        #formatar_moeda
        self.reg_preco.textChanged.connect(self.formatar_moeda)

    def formatar_moeda(self):
        # Obtém o texto atual do campo reg_preco
        texto = self.reg_preco.text()
        print(f'Texto original: {texto}')

        # Remove qualquer caractere que não seja um dígito numérico
        texto = ''.join(c for c in texto if c.isdigit())
        print(f'Texto após remoção de caracteres não-numéricos: {texto}')

        # Verifica se o texto está vazio
        if not texto:
            return

        # Converte o texto para um valor float
        valor = float(texto) / 100

        # Formata o valor como um valor monetário
        texto_formatado = f'R$ {valor:.2f}'

        # Define o texto formatado como o texto do campo reg_preco
        self.reg_preco.setText(texto_formatado)
        
    #mover janela
    def mousePressEvent(self, event):
        self.click_position = event.globalPos()
        
    def mover_janela():
        if self.isMaximized() == False:
            if event.button() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.click_position)
                self.click_position = event.globalPos()
                event.accept()
        if event.globalPos().y() <=10:
            self.showMaximized()
            self.bt_maximizar.hide()
            self.bt_restaurar.show()
        else:
            self.showNormal()
            self.bt_restaurar.hide()
            self.bt_maximizar.show()
            
    #método para mover o menu para a lateral esquerda
    def mover_menu(self):
        if True:
            width = self.frame_control.width()
            normal = 0
            if width ==0:
                extender = 200
            else:
                extender = normal
            self.animacao = QPropertyAnimation(self.frame_control, b'minimumWidth')
            self.animacao.setDuration(300)
            self.animacao.setStartValue(width)
            self.animacao.setEndValue(extender)
            self.animacao.setEasingCurve(QtCore, QEasingCurve.InOutQuart)
            self.animacao.start()
            
    #configurações da página de dados
    def mostrar_produtos(self):
        dados = self.adega.mostrar_produtos()
        i = len(dados)
        self.tabela_produtos.setRowCount(i)
        tablerow = 0
        
        for row in dados:
            self.id = row[0]
            #tornando a coluna do ID não-editável
            id_item = QTableWidgetItem(str(row[0]))
            id_item.setFlags(id_item.flags() & ~Qt.ItemIsEditable)
            self.tabela_produtos.setItem(tablerow, 0, id_item)
            
            self.tabela_produtos.setItem(tablerow,1,QTableWidgetItem(row[1]))
            self.tabela_produtos.setItem(tablerow,2,QTableWidgetItem(row[2]))
            self.tabela_produtos.setItem(tablerow,3,QTableWidgetItem(row[3]))
            self.tabela_produtos.setItem(tablerow,4,QTableWidgetItem(row[4]))
            self.tabela_produtos.setItem(tablerow,5,QTableWidgetItem(row[5]))

            #criando os botões editar e excluir em cada linha         
            widget = QWidget()
            btn_editar = QPushButton('Editar')
            btn_excluir = QPushButton('Excluir')

            #Estilo do botão Editar
            btn_editar.setFixedWidth(50)
            btn_editar.setStyleSheet(
                "QPushButton{"
                "background-color: rgb(62, 62, 185);"
                "}"
                 "QPushButton:hover{"
                 "background-color: rgb(76, 76, 229);"
                 "}"
                                    )
            #Estilo do botão Excluir
            btn_excluir.setFixedWidth(50)
            btn_excluir.setStyleSheet(
                "QPushButton{"
                "background-color: rgb(214, 0, 0);"
                "}"
                "QPushButton:hover{"
                "background-color: rgb(255, 0, 0);"
                "}"
                                    )
            
            layout = QHBoxLayout(widget)
            layout.addWidget(btn_editar)
            layout.addWidget(btn_excluir)
            layout.setContentsMargins(5,0,5,0)
            #layout.setSpacing(10)
            
            self.tabela_produtos.setCellWidget(tablerow, 6, widget)

            #conectando os botões ás funções
            btn_excluir.clicked.connect(lambda checked, row_id=row[0]: self.excluir_linha(row_id))
            btn_editar.clicked.connect(lambda checked, row_id=row[0], row=tablerow: self.modificar_produtos(row_id, row))
                        
            tablerow +=1
            
            self.signal_base.setText("")
            self.signal_registrar.setText("")
               
    def busca_por_nome(self):
        nome_produto = self.buscar_nome.text().upper()
        nome_produto = str("'" + nome_produto + "'")
        produto = self.adega.busca_produto(nome_produto)
        i = len(produto)
        self.tabela_produtos.setRowCount(i)
        tablerow = 0
        for row in produto:
            self.id = row[0]
            #tornandoo id nãoeditável
            id_item = QTableWidgetItem(str(row[0]))
            id_item.setFlags(id_item.flags() & ~Qt.ItemIsEditable)
            self.tabela_produtos.setItem(tablerow, 0, id_item)
            
            self.tabela_produtos.setItem(tablerow,1,QTableWidgetItem(row[1]))
            self.tabela_produtos.setItem(tablerow,2,QTableWidgetItem(row[2]))
            self.tabela_produtos.setItem(tablerow,3,QTableWidgetItem(row[3]))
            self.tabela_produtos.setItem(tablerow,4,QTableWidgetItem(row[4]))
            self.tabela_produtos.setItem(tablerow,5,QTableWidgetItem(row[5]))
            
            #criando os botões editar e excluir
            widget = QWidget()
            btn_editar = QPushButton('Editar')
            btn_excluir = QPushButton('Excluir')
            widget.setStyleSheet('background-color: #ffffff;')
            
            layout = QHBoxLayout(widget)
            layout.addWidget(btn_editar)
            layout.addWidget(btn_excluir)
            layout.setContentsMargins(5,0,5,0)
            layout.setSpacing(10)
            
            self.tabela_produtos.setCellWidget(tablerow,6,widget)
            
            #fazendo as conexões dos botões com as funções
            btn_excluir.clicked.connect(lambda checked, row_id=row[0]: self.excluir_linha(row_id))
            btn_editar.clicked.connect(lambda checked, row_id=row[0], row=tablerow: self.modificar_produtos(row_id, row))
            
            #Estilo do botão Editar
            btn_editar.setFixedWidth(50)
            btn_editar.setStyleSheet(
                "QPushButton{"
                "background-color: rgb(62, 62, 185);"
                "}"
                 "QPushButton:hover{"
                 "background-color: rgb(76, 76, 229);"
                 "}"
                                    )
            #Estilo do botão Excluir
            btn_excluir.setFixedWidth(50)
            btn_excluir.setStyleSheet(
                "QPushButton{"
                "background-color: rgb(214, 0, 0);"
                "}"
                "QPushButton:hover{"
                "background-color: rgb(255, 0, 0);"
                "}"
                                    )
                        
            tablerow +=1
            
            self.buscar_nome.clear()
            
            #self.signal_atualizar.setText("")
            #self.signal_registrar.setText("")
            #self.signal_eliminar.setText("")
            
    def modificar_produtos(self, row_id, tablerow):
        id = self.tabela_produtos.item(tablerow, 0).text()
        codigo = self.tabela_produtos.item(tablerow, 1).text()
        nome =   self.tabela_produtos.item(tablerow, 2).text()
        modelo = self.tabela_produtos.item(tablerow, 3).text()
        preco =  self.tabela_produtos.item(tablerow, 4).text()
        qtd =    self.tabela_produtos.item(tablerow, 5).text()
        resultado = self.adega.atualiza_produto(id, codigo, nome, modelo, preco, qtd)
            
        # atualizando a interface do usuário
        self.tabela_produtos.item(tablerow, 1).setText(codigo)
        self.tabela_produtos.item(tablerow, 2).setText(nome)
        self.tabela_produtos.item(tablerow, 3).setText(modelo)
        self.tabela_produtos.item(tablerow, 4).setText(preco)
        self.tabela_produtos.item(tablerow, 5).setText(qtd)
        self.signal_base.setText('Registro Editado')
        self.buscar_nome.clear()
            
    def registrar_produto(self):
        codigo = self.reg_codigo.text().upper()
        nome = self.reg_nome.text().upper()
        modelo = self.reg_modelo.text().upper()
        preco = self.reg_preco.text().upper()
        qtd = self.reg_qtd.text().upper()
        
        if codigo != '' and nome != '' and modelo != '' and preco != '' and qtd != '':
            self.adega.inserir_produto(codigo,nome,modelo,preco,qtd)
            self.signal_registrar.setText('Protudo Registrado')
            self.reg_codigo.clear()
            self.reg_nome.clear()
            self.reg_modelo.clear()
            self.reg_preco.clear()
            self.reg_qtd.clear()
        else:
            self.signal_registrar.setText('Preencha todos os campos')
            
    def eliminar_produtos(self):
        self.row_flag = self.tabela_eliminar.currentRow()
        if self.row_flag == 0:
            self.tabela_eliminar.removeRow(0)
            self.adega.elimina_produto("'"+ self.produto_a_eliminar+ "'")
            self.signal_eliminar.setText('Produto Eliminado')
            self.eliminar_buscar.clear()
            
    def excluir_linha(self, id):
        # excluindo a linha do banco de dados
        self.adega.elimina_produto(id)

        # atualizando a interface do usuário
        row = self.find_row_by_id(id)
        if row!= -1:
            self.tabela_produtos.removeRow(row)
            self.buscar_nome.clear()
            self.signal_base.setText("Registro Excluído")

    def find_row_by_id(self, id):
        # encontra a linha na tabela com o ID especificado
        for row in range(self.tabela_produtos.rowCount()):
            if self.tabela_produtos.item(row, 0).text() == str(id):
                return row
        return -1
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = JanelaPrincipal()
    mi_app.show()
    sys.exit(app.exec()) 
    
