from PyQt5 import uic, QtWidgets
import sqlite3
from reportlab.pdfgen import canvas


def chama_segunda_tela():

    primeira_tela.label_3.setText("")
    segunda_tela.label_5.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_3.text()
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()

    try:
        cursor.execute(
            "SELECT senha FROM cadastro WHERE usuario = '{}'".format(nome_usuario))
        senha_db = cursor.fetchall()
        banco.close()

    except:
        print('Erro ao validar o usuário')

    else:
        pass

    if senha == senha_db[0][0]:
        primeira_tela.close()
        segunda_tela.show()

    else:
        primeira_tela.label_3.setText("Dados de login incorretos!")

    primeira_tela.lineEdit.setText("")
    primeira_tela.lineEdit_3.setText("")
    segunda_tela.label_5.setText(nome_usuario)


def logout():
    segunda_tela.close()
    primeira_tela.show()


def abre_tela_cadastro():
    tela_cadastro.show()


def cadastrar():
    tela_cadastro.label_6.setText("")
    nome = tela_cadastro.campo_nome.text()
    email = tela_cadastro.campo_email.text()
    usuario = tela_cadastro.campo_usuario.text()
    senha = tela_cadastro.campo_senha.text()
    c_senha = tela_cadastro.campo_senha_2.text()

    tela_cadastro.campo_nome.setText("")
    tela_cadastro.campo_email.setText("")
    tela_cadastro.campo_usuario.setText("")
    tela_cadastro.campo_senha.setText("")
    tela_cadastro.campo_senha_2.setText("")

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db')
            cursor = banco.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS cadastro (nome text, email text, usuario text, senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('" +
                           nome+"', '"+email+"', '"+usuario+"', '"+senha+"')")

            banco.commit()
            banco.close()
            tela_cadastro.label_6.setText("Usuário cadastrado com sucesso")

        except sqlite3.Error as erro:
            print('Erro ao inserir os dados: ', erro)

    else:
        tela_cadastro.label_6.setText("As senhas estão erradas")


def chama_tela_cadastro_paciente():
    tela_cadastro_paciente.show()


def cadastrar_paciente():

    nome = tela_cadastro_paciente.campo_nome_pac.text()
    data_nascimento = tela_cadastro_paciente.campo_pac_dtn.text()
    rg = tela_cadastro_paciente.campo_pac_rg.text()
    cpf = tela_cadastro_paciente.campo_pac_cpf.text()
    endereco = tela_cadastro_paciente.campo_pac_edn.text()
    cep = tela_cadastro_paciente.campo_pac_cep.text()
    ddd = tela_cadastro_paciente.campo_pac_ddd.text()
    telefone = tela_cadastro_paciente.campo_pac_tel.text()
    nome_uf = tela_cadastro_paciente.comboBox_2.currentText()
    nome_cidade = tela_cadastro_paciente.campo_pac_cdd.text()

    tela_cadastro_paciente.campo_nome_pac.setText("")
    tela_cadastro_paciente.campo_pac_dtn.setText("")
    tela_cadastro_paciente.campo_pac_rg.setText("")
    tela_cadastro_paciente.campo_pac_cpf.setText("")
    tela_cadastro_paciente.campo_pac_edn.setText("")
    tela_cadastro_paciente.campo_pac_cep.setText("")
    tela_cadastro_paciente.campo_pac_ddd.setText("")
    tela_cadastro_paciente.campo_pac_tel.setText("")
    # tela_cadastro_paciente.comboBox_2.currentText()
    tela_cadastro_paciente.campo_pac_cdd.setText("")

    try:
        banco = sqlite3.connect('banco_cadastro.db')
        cursor = banco.cursor()
        cursor.execute("INSERT INTO pacientes VALUES (NULL,'" +
                       nome+"', '"+data_nascimento+"', '"+rg+"', '"+cpf+"', '"+endereco+"', '"+cep+"', '"+ddd+"', '"+telefone+"', '"+nome_uf+"', '"+nome_cidade+"')")

        banco.commit()
        banco.close()
        # tela_cadastro.label_6.setText("Usuário cadastrado com sucesso")

    except sqlite3.Error as erro:
        print('Erro ao inserir os dados: ', erro)


def chama_tela_listar_paciente():

    tela_listar_paciente.show()

    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    comando_sql = "SELECT * FROM pacientes"
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()

    tela_listar_paciente.tableWidget.setRowCount(len(dados_lidos))
    tela_listar_paciente.tableWidget.setColumnCount(11)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 11):
            tela_listar_paciente.tableWidget.setItem(
                i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def excluir_dados():

    linha = tela_listar_paciente.tableWidget.currentRow()
    tela_listar_paciente.tableWidget.removeRow(linha)

    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM pacientes")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM pacientes WHERE id=" + str(valor_id))
    banco.commit()


def gerar_pdf():

    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    comando_sql = "SELECT * FROM pacientes"
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()

    y = 0

    pdf = canvas.Canvas('Cadastro_pacietes.pdf')
    pdf.setFont('Times-Bold', 12)
    pdf.drawString(200, 800, 'Pacientes cadastrados:')
    pdf.setFont('Times-Bold', 10)

    pdf.drawString(10, 750, 'ID')
    pdf.drawString(110, 750, 'NOME')
    pdf.drawString(210, 750, 'DATA_NASCIMENTO')
    pdf.drawString(310, 750, 'RG')
    pdf.drawString(410, 750, 'CPF')
    pdf.drawString(510, 750, 'ENDEREÇO')
    pdf.drawString(610, 750, 'CEP')
    pdf.drawString(710, 750, 'DDD')
    pdf.drawString(810, 750, 'TELEFONE')
    pdf.drawString(910, 750, 'UF')
    pdf.drawString(1010, 750, 'CIDADE')

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10, 750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110, 750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210, 750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310, 750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410, 750 - y, str(dados_lidos[i][4]))
        pdf.drawString(510, 750 - y, str(dados_lidos[i][5]))
        pdf.drawString(610, 750 - y, str(dados_lidos[i][6]))
        pdf.drawString(710, 750 - y, str(dados_lidos[i][7]))
        pdf.drawString(810, 750 - y, str(dados_lidos[i][8]))
        pdf.drawString(910, 750 - y, str(dados_lidos[i][9]))
        pdf.drawString(1010, 750 - y, str(dados_lidos[i][10]))

    pdf.save()
    print('O PDF FOI GERADO COM SUCESSO')


app = QtWidgets.QApplication([])

# Carregamento das telas

primeira_tela = uic.loadUi("tela_login.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
tela_cadastro_paciente = uic.loadUi("cadastro_paciente.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
tela_listar_paciente = uic.loadUi("listar_paciente.ui")

# Botões que acionam as defs
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(logout)
primeira_tela.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
primeira_tela.pushButton_2.clicked.connect(abre_tela_cadastro)
segunda_tela.bt_cad_paciente.clicked.connect(
    chama_tela_cadastro_paciente)
tela_cadastro.botao_cadastrar.clicked.connect(cadastrar)
tela_cadastro_paciente.botao_cadastrar_pac.clicked.connect(cadastrar_paciente)
tela_cadastro_paciente.comboBox_2.addItems(
    ['', 'AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'])
tela_cadastro_paciente.botao_listar.clicked.connect(chama_tela_listar_paciente)
tela_listar_paciente.bt_excluir_pac.clicked.connect(excluir_dados)
tela_listar_paciente.bt_gerar_pdf.clicked.connect(gerar_pdf)

# Execução do programa
primeira_tela.show()
app.exec()
