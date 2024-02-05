from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
from time import strptime, struct_time, localtime, mktime, strftime
import pandas as pd
import getpass
import os
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize



class FuncoesEmpretimo():
    def file_open_pdf(self):
        self.Criar_pdf() 
    def Usuario(self):
        # vamos obter o nome do usuário logado no sistema
        self.usuario = getpass.getuser()  
        # e mostramos o resultado
        print("O usuário logado no momento é:", self.usuario)

    def Criar_pdf(self):
        self.Calcular_Lan()
        #self.file = filedialog.asksaveasfilename(initialdir='C://file', filetypes=[('text file', '*.pdf')],defaultextension='*.pdf')
        self.file, _ = QFileDialog.getSaveFileName(self, 'Salvar arquivo', 'C://file', 'Arquivos de Texto (*.pdf)')
        data_formatada = f"{self.data:%d/%m/%Y}"
        cnv = canvas.Canvas(self.file, pagesize=A4)
        cnv.setFont("Helvetica-Oblique", 10)
        x = 50
        y = 810
        #variaveis
        self.txt = ''
        cpfoucnpj = ''
        banco = '555555555555555555555555555'
        taxa = ''
        iof = ''
        juros_passivo = ''
        emprestimo_CP = ''
        encargo_CP = ''
        emprestimo_LP = ''
        encargo_LP = ''        
        self.hitorico = ''
        data_txt = f"{self.data:%Y%m%d}"
        contador = 1
        contador_formatado = "{:06d}".format(contador)

        cnv.drawString(x, y-4, "_________________________________________________________________________________________")
        cnv.drawString(x+170, y-20, "RESUMO DE EMPRESTIMO")
        cnv.drawString(x, y-26, "_________________________________________________________________________________________")
        cnv.drawString(x+35, y-50, str("Data: "+str(data_formatada)))
        cnv.drawString(x+35, y-65, str("Valor Emprestimo: R$ "+ str(round(self.valor, 2))))
        cnv.drawString(x+35, y-80, str("Taxa Contrato: R$ "+str(round(self.taxa_contrato, 2))))
        cnv.drawString(x+35, y-95, str("IOF: R$ "+str(self.iof)))
        cnv.drawString(x+35, y-110, str("Total Emprestimo: R$ "+str(round(self.soma, 2))))
        cnv.drawString(x+285, y-70, str("Parcelas: "+str(self.parcelas)))
        cnv.drawString(x+285, y-85, str("Valor Parcela: R$ "+str(round(self.valorParcelas, 2))))
        cnv.drawString(x, y-125, "_________________________________________________________________________________________")
        cnv.drawString(x+155, y-141, "LANÇAMENTOS DO EMPRESTIMO")
        cnv.drawString(x, y-147, "_________________________________________________________________________________________")
        cnv.drawString(x+20, y-171, "---------------------------------------------------- Banco e Taxas ----------------------------------------------------------")
        cnv.drawString(x+70, y-201, str(str(data_formatada) + "   D - Emprestimo"+ "  ...................................................."+ "R$ " + str(round(self.valor, 2))))
        lanSimp = contador_formatado + "," + str(data_txt) + ","+str(banco)+",0," + str(self.valor) + ",00000000," + "Vlr. Ref. Emprestimo "+ str(self.hitorico)+",,"+ cpfoucnpj + "," + "\n"
        self.txt += str(lanSimp)
        contador += 1        
        
        if int(self.taxa_contrato) > 0:
            cnv.drawString(x+70, y-216, str(str(data_formatada) + "   D - Taxa Contrato"+ "  ................................................"+ "R$ " + str(round(self.taxa_contrato, 2))))
            y = y-216       
            lanSimp = contador_formatado + "," + str(data_txt) + ","+str(taxa)+",0," + str(self.taxa_contrato) + ",00000000," + "Vlr. Ref. taxas s/Emprestimo "+ str(self.hitorico)+",,"+ cpfoucnpj + "," + "\n"
            self.txt += str(lanSimp)
            contador += 1 
        
        if int(self.iof) > 0:
            cnv.drawString(x+70, y-15, str(str(data_formatada) + "   D - IOF"+ "  ................................................................."+ "R$ " + str(round(self.iof, 2))))
            y = y-15
            lanSimp = contador_formatado + "," +  str(data_txt) + ","+str(iof)+",0," + str(self.iof) + ",00000000," + "Vlr. Ref. IOF s/Emprestimo "+ str(self.hitorico)+",,"+ cpfoucnpj + "," + "\n"
            self.txt += str(lanSimp)
            contador += 1

        if int(self.longoPrazo) >= 1:
            cnv.drawString(x+20, y-25, "------------------------------------------------------ Curto Prazo ------------------------------------------------------------")
            cnv.drawString(x+20, y-35, str("   [ Total de Parcelas: "+str(self.CurtoPrazo)+"]"))
            cnv.drawString(x+300, y-35, str("  [Ano "+str(self.ano)+": "+str((int(self.CurtoPrazo) - 12))+"]  [Ano "+str((int(self.ano) + 1))+ ": 12 ]"))
            cnv.drawString(x+70, y-60, str(str(data_formatada) + "  D- (-) Encargos Emprestimo CP"+ "  ........................"+ "R$ " + str(round(self.encargosParcelas * self.CurtoPrazo, 2))))
            cnv.drawString(x+70, y-75, str(str(data_formatada) + "  C - Emprestimo CP"+ "  .............................................."+ "R$ " + str(round(self.emprestimoParcelas * self.CurtoPrazo, 2))))
            lanSimp = contador_formatado + "," + str(data_txt) + ","+str(encargo_CP)+",0," + str(self.encargosParcelas * self.CurtoPrazo) + ",00000000," + "Vlr. Ref. Encargos CP s/Emprestimo Parcelas:"+ str(self.CurtoPrazo)+" "+  str(self.hitorico)+",,"+ cpfoucnpj + "," + "\n"
            self.txt += str(lanSimp)
            contador += 1
            lanSimp = contador_formatado + "," + str(data_txt) + ",0,"+str(emprestimo_CP)+"," + str(self.emprestimoParcelas * self.CurtoPrazo) + ",00000000," + "Vlr. Ref. Emprestimo CP Parcelas:"+ str(self.CurtoPrazo)+" " + str(self.hitorico)+",,"+ cpfoucnpj + "," + "\n"
            self.txt += str(lanSimp)
            contador += 1        
       
            cnv.drawString(x+20, y-100, "------------------------------------------------------ Longo Prazo ------------------------------------------------------------")
            cnv.drawString(x+20, y-110, str("   [ Total de Parcelas: "+str(int(self.longoPrazo))+"]"))
            cnv.drawString(x+70, y-135, str(str(data_formatada) + "  D - (-) Encargos Emprestimo LP"+ "  ........................"+ "R$ " + str(round(self.encargosParcelas * self.longoPrazo, 2))))
            cnv.drawString(x+70, y-150, str(str(data_formatada) + "  C - Emprestimo LP"+ "  .............................................."+ "R$ " + str(round(self.emprestimoParcelas * self.longoPrazo, 2))))
            lanSimp = contador_formatado + "," + str(data_txt) + ","+str(encargo_LP)+",0," + str(self.encargosParcelas * self.longoPrazo) + ",00000000," + "Vlr. Ref. Encargos CP s/Emprestimo Parcelas:"+ str(self.longoPrazo)+" "+  str(self.hitorico)+",,"+ cpfoucnpj + "," + "\n"
            self.txt += str(lanSimp)
            contador += 1
            lanSimp = contador_formatado + "," + str(data_txt) + ",0,"+str(emprestimo_LP)+"," + str(self.emprestimoParcelas * self.longoPrazo) + ",00000000," + "Vlr. Ref. Emprestimo CP Parcelas:"+ str(self.longoPrazo)+" " + str(self.hitorico)+",,"+ cpfoucnpj + "," + "\n"
            self.txt += str(lanSimp)
            contador += 1  
            
            cnv.drawString(x, y-174, "_________________________________________________________________________________________")
            cnv.drawString(x+210, y-190, "APROPRIAÇÃO")
            cnv.drawString(x, y-196, "_________________________________________________________________________________________")           
            y = y-192
            cnv.drawString(x+30, y-36, str(" [ Apropriação Mensal do Juros: "+str(self.parcelas)+"x ] "))
            cnv.drawString(x+236, y-28, str(" | D - Juros Passivo"+"............................."+ "R$ " + str(round(self.encargosParcelas, 2)) ))
            cnv.drawString(x+236, y-40, str(" | C - (-) Encargos Emprestimo CP"+"....."+ "R$ " + str(round(self.encargosParcelas, 2)) ))              
            for i in range(self.parcelas):
                mes = self.data.month + i
                ano = self.data.year + mes // 12
                mes = mes % 12 or 12  # Lida com a troca de ano
                ultimo_dia = {
                    1: 31,
                    2: 29 if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else 28,
                    3: 31,
                    4: 30,
                    5: 31,
                    6: 30,
                    7: 31,
                    8: 31,
                    9: 30,
                    10: 31,
                    11: 30,
                    12: 31,
                }[mes]
                nova_data = self.data.replace(year=ano, month=mes, day=ultimo_dia)
                d_txt = f"{nova_data:%Y%m%d}"
                
                lanSimp = '000001' + "," + str(d_txt) + ","+str(encargo_CP)+","+str(juros_passivo)+"," + str(self.encargosParcelas) + ",00000000," + "Vlr. Ref. Apropriação do Encargos "+ str(self.hitorico)+",,"+ cpfoucnpj + "," + "\n"
                self.txt += str(lanSimp)
                print(self.txt)
            
            y = y-36
            self.AnoApropriação = int(self.ano) + 1
            self.dataIn = "01/01/"
            cnv.setFont("Helvetica-Oblique", 9)
            while (int(self.longoPrazo) >= 12):
                cnv.drawString(x+12, y-36, str(" [ Apropriação ano subsequente:"+str(self.AnoApropriação)+"]  "+ "02/01/"+str(self.AnoApropriação)))
                cnv.setFont("Helvetica-Oblique", 8)
                cnv.drawString(x+225, y-28, str(" | D - Emprestimo LP"+"....."+ "R$ " + str(round(self.emprestimoParcelas * 12, 2)) ))
                cnv.drawString(x+225, y-40, str(" | C - Emprestimo CP"+"....."+ "R$ " + str(round(self.emprestimoParcelas * 12, 2)) ))
                cnv.drawString(x+371, y-28, str(" | D - (-) Encargos LP"+"....."+ "R$ " + str(round(self.emprestimoParcelas * 12, 2)) ))
                cnv.drawString(x+371, y-40, str(" | C - (-) Encargos CP"+"....."+ "R$ " + str(round(self.emprestimoParcelas * 12, 2)) ))
                self.longoPrazo = self.longoPrazo - 12
                self.AnoApropriação = self.AnoApropriação + 1
                y = y-30
                cnv.setFont("Helvetica-Oblique", 9)
            if int(self.longoPrazo) >= 1:
                cnv.drawString(x+12, y-36, str(" [ Apropriação ano subsequente:"+str(self.AnoApropriação)+"]  "+ "02/01/"+str(self.AnoApropriação)))
                cnv.setFont("Helvetica-Oblique", 8)
                cnv.drawString(x+225, y-28, str(" | D - Emprestimo LP"+"....."+ "R$ " + str(round(self.emprestimoParcelas * 12, 2)) ))
                cnv.drawString(x+225, y-40, str(" | C - Emprestimo CP"+"....."+ "R$ " + str(round(self.emprestimoParcelas * 12, 2)) ))
                cnv.drawString(x+371, y-28, str(" | D - (-) Encargos LP"+"....."+ "R$ " + str(round(self.emprestimoParcelas * 12, 2)) ))
                cnv.drawString(x+371, y-40, str(" | C - (-) Encargos CP"+"....."+ "R$ " + str(round(self.emprestimoParcelas * 12, 2)) ))
                self.longoPrazo = self.longoPrazo - 12
                self.AnoApropriação = self.AnoApropriação + 1
                y = y-30     
        else:
            cnv.drawString(x+70, y-15, str(str(data_formatada) + "  D- (-) Encargos Emprestimo CP"+ "  ........................"+ "R$ " + str(round(self.encargos, 2))))
            cnv.drawString(x+70, y-30, str(str(data_formatada) + "  C - Emprestimo CP"+ "  .............................................."+ "R$ " + str(round(self.emprestimo, 2))))

            cnv.drawString(x, y-54, "_________________________________________________________________________________________")
            cnv.drawString(x+210, y-70, "APROPRIAÇÃO")
            cnv.drawString(x, y-76, "_________________________________________________________________________________________")           
            y = y-76
            cnv.drawString(x+30, y-36, str(" [ Apropriação Mensal do Juros: "+str(self.parcelas)+"x ] "))
            cnv.drawString(x+236, y-28, str(" | D - Juros Passivo"+"............................."+ "R$ " + str(round(self.encargosParcelas, 2)) ))
            cnv.drawString(x+236, y-40, str(" | C - (-) Encargos Emprestimo CP"+"....."+ "R$ " + str(round(self.encargosParcelas, 2)) ))              
       
        cnv.setFont("Helvetica-Oblique", 7)
        self.usuario = getpass.getuser()
        self.usuario = self.usuario.upper()
        now = datetime.now()
        self.dataHoraHoje = now.strftime('%d/%m/%Y - %H:%M:%S')
        cnv.drawString(390, 20, str(str(self.dataHoraHoje)+" - Relatorio Emitido por: "+ str(self.usuario)))
        cnv.drawString(30, 20, str('AGIR - ASSESSORIA EMPRESARIAL LTDA'))
        cnv.save()

    def txt_emprestimo(self):
        self.txt = ''
        cpfoucnpj = ''
        banco = '555555555555555555555555555'
        taxa = ''
        iof = ''
        emprestimo_CP = ''
        encargo_CP = ''
        emprestimo_LP = ''
        encargo_LP = ''

        self.hitorico = ''
        data_txt = f"{self.data:%Y%m%d}"
        lanSimp = "000001,"+ str(data_txt) + ","+str(banco)+",0," + str(self.valor) + ",00000000," + "Vlr. Ref. Emprestimo "+ str(self.hitorico)+",,"+ cpfoucnpj + "," + "\n"
        self.txt += str(lanSimp)
        if int(self.taxa_contrato) > 0:
            lanSimp = "000002,"+ str(data_txt) + ","+str(taxa)+",0," + str(self.taxa_contrato) + ",00000000," + "Vlr. Ref. taxas s/Emprestimo "+ str(self.hitorico)+",,"+ cpfoucnpj + "," + "\n"
            self.txt += str(lanSimp)
        if int(self.iof) > 0:
            lanSimp = "000003,"+ str(data_txt) + ","+str(iof)+",0," + str(self.iof) + ",00000000," + "Vlr. Ref. IOF s/Emprestimo "+ str(self.hitorico)+",,"+ cpfoucnpj + "," + "\n"
            self.txt += str(lanSimp)
        if int(self.longoPrazo) >= 1:
            lanSimp = "000004,"+ str(data_txt) + ","+str(encargo_CP)+",0," + str(self.encargosParcelas * self.CurtoPrazo) + ",00000000," + "Vlr. Ref. IOF s/Emprestimo "+ str(self.hitorico)+",,"+ cpfoucnpj + "," + "\n"
            self.txt += str(lanSimp)
            lanSimp = "000005,"+ str(data_txt) + ",0,"+str(emprestimo_CP)+"," + str(self.iof) + ",00000000," + "Vlr. Ref. IOF s/Emprestimo "+ str(self.hitorico)+",,"+ cpfoucnpj + "," + "\n"
            self.txt += str(lanSimp)




    def Calcular_Lan(self):
        try:
            self.valor = float(self.ui.entryEmpEmp.text().replace(".", "").replace(",", "."))
        except ValueError:
            self.valor = 0.0
        try:        
            self.taxa_contrato = float(self.ui.entryTaxasEmp.text().replace(".", "").replace(",", "."))
        except ValueError:
            self.taxa_contrato = 0.0
        try:
            self.iof = float(self.ui.entryIoEmp.text().replace(".", "").replace(",", "."))
        except ValueError:
            self.iof = 0.0
        try:
            self.parcelas = int(self.ui.entryParcelaEmp.text())
        except ValueError:
            self.parcelas = 0        
        try:
            self.valorParcelas = float(self.ui.entryVParcEmp.text().replace(".", "").replace(",", "."))
        except ValueError:
            self.valorParcelas = 0           
        try:
            self.textData = self.ui.entryDataEmp.text()
            self.data = datetime.strptime(self.textData, '%d/%m/%Y')
        except ValueError:
            print('erro value erro')
            #data = struct_time(localtime()   

        self.emprestimo = self.valorParcelas * float(self.parcelas)
        self.emprestimoParcelas = self.emprestimo / float(self.parcelas)
        self.soma = self.valor + self.taxa_contrato + self.iof
        self.encargos = self.emprestimo - self.soma
        self.encargosParcelas = self.encargos / float(self.parcelas)
        print(type(self.data))
        print("---------------data2---------------")
        self.mes = self.data.strftime('%m')
        self.ano = self.data.strftime('%Y')
        self.ano = self.ano.replace(" ","")


        self.CurtoPrazo = (13 - int(self.mes)) + 12
        self.longoPrazo = self.parcelas - self.CurtoPrazo
        self.relatorio = '1' 
        print(self.relatorio)

        self.exibir_relatorio_emprestimo()

    def clearLayout(layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


    def exibir_relatorio_emprestimo(self):
        # Remove todos os layouts do widgetRelatorioEmprestimo.
        layout = self.ui.widgetRelatorioEmprestimo.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
                elif child.layout():  # Verifique se é um layout
                    child.layout().deleteLater()

        if new_layout.layout() is not None:
            while new_layout.count():
                child = new_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
                elif child.layout():  # Verifique se é um layout
                    child.layout().deleteLater()


        # Criar os componentes do layout
        fonte_titulo = QFont('Arial', 14, QFont.Bold)
        titulo_label = QLabel('RESUMO DE EMPRÉSTIMO')
        titulo_label.setFont(fonte_titulo)
        titulo_label2 = QLabel('RELATÓRIOS')
        titulo_label2.setFont(fonte_titulo)

        # Criar o QLabel para cada informação
        data_label = QLabel(f"<b>Data:</b> {self.data}")
        valor_emprestimo_label = QLabel(f"<b>Valor Empréstimo:</b> R$ {self.valor}")
        taxa_contrato_label = QLabel(f"<b>Taxa Contrato:</b> R$ {self.taxa_contrato}")
        iof_label = QLabel(f"<b>IOF:</b> R$ {self.iof}")
        total_emprestimo_label = QLabel(f"<b>Total Empréstimo:</b> R$ {self.parcelas}")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        icon13 = QIcon()
        icon13.addPixmap(QPixmap(":/imagens/img/txt-btn.png"), QIcon.Normal, QIcon.Off)
        icon14 = QIcon()
        icon14.addPixmap(QPixmap(":/imagens/img/pdf-btn.png"), QIcon.Normal, QIcon.Off)
        txt_emprestimo_btn = QPushButton("TXT")
        txt_emprestimo_btn.setIcon(icon13)  # Configure o ícone conforme necessário
        txt_emprestimo_btn.setIconSize(QSize(80, 80))  # Defina o tamanho do ícone conforme necessário
        txt_emprestimo_btn.setFont(font)  # Defina a fonte do botão conforme necessário
        txt_emprestimo_btn.setObjectName("txtEmprestimo")  # Defina o nome do objeto conforme necessário
        pdf_emprestimo_btn = QPushButton("PDF")
        pdf_emprestimo_btn.setIcon(icon14)  # Configure o ícone conforme necessário
        pdf_emprestimo_btn.setIconSize(QSize(80, 80))  # Defina o tamanho do ícone conforme necessário
        pdf_emprestimo_btn.setFont(font)  # Defina a fonte do botão conforme necessário
        pdf_emprestimo_btn.setObjectName("pdfEmprestimo")  # Defina o nome do objeto conforme necessário 
        pdf_emprestimo_btn.clicked.connect(self.file_open_pdf)

        # Definir os estilos CSS
        estilo_titulo = "QLabel { border: none; font-size: 14pt; font-weight: bold; margin: 20px; margin-left: 35px }"
        estilo_titulo2 = "QLabel { border: none; font-size: 14pt; font-weight: bold; margin: 5px; margin-left: 105px; margin-top: 25px }"
        estilo_conteudo = "QLabel { border: none; font-size: 10pt; margin: 8px }"
        estilo_botão = "QPushButton { border: none; font-size: 10pt; margin: 8px }"

        # Aplicar os estilos aos QLabels
        titulo_label.setStyleSheet(estilo_titulo)
        titulo_label2.setStyleSheet(estilo_titulo2)
        data_label.setStyleSheet(estilo_conteudo)
        valor_emprestimo_label.setStyleSheet(estilo_conteudo)
        taxa_contrato_label.setStyleSheet(estilo_conteudo)
        iof_label.setStyleSheet(estilo_conteudo)
        total_emprestimo_label.setStyleSheet(estilo_conteudo)
        txt_emprestimo_btn.setStyleSheet(estilo_botão)
        pdf_emprestimo_btn.setStyleSheet(estilo_botão)

        # Criar o novo layout vertical
        new_layout = QVBoxLayout(self.ui.widgetRelatorioEmprestimo)
        new_layout.setContentsMargins(2, 2, 2, 2)
        new_layout.setSpacing(5)
        new_layout.setAlignment(Qt.AlignTop)

        # Adicionar os QLabels ao novo layout
        new_layout.addWidget(titulo_label)
        new_layout.addWidget(data_label)
        new_layout.addWidget(valor_emprestimo_label)
        new_layout.addWidget(taxa_contrato_label)
        new_layout.addWidget(iof_label)
        new_layout.addWidget(total_emprestimo_label)
        new_layout.addWidget(titulo_label2)

        # Criar o layout horizontal e adicionar os botões
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(txt_emprestimo_btn)
        layout_horizontal.addWidget(pdf_emprestimo_btn)

        if new_layout.layout() is not None:
            new_layout.addLayout(layout_horizontal)

        # Exibir o widgetRelatorioEmprestimo
        self.ui.widgetRelatorioEmprestimo.show()