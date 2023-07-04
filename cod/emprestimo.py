from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
from time import strptime, struct_time, localtime, mktime, strftime
import pandas as pd
import getpass
import os


class Funcoes():
    def Usuario(self):
        # vamos obter o nome do usuário logado no sistema
        self.usuario = getpass.getuser()  
        # e mostramos o resultado
        print("O usuário logado no momento é:", self.usuario)

    def Criar_pdf(self):
        self.Calcular_Lan()
        self.file = filedialog.asksaveasfilename(initialdir='C://file', filetypes=[('text file', '*.pdf')],defaultextension='*.pdf')
        cnv = canvas.Canvas(self.file, pagesize=A4)
        cnv.setFont("Helvetica-Oblique", 10)
        x = 50
        y = 810
        cnv.drawString(x, y-4, "________________________________________________________________________________")
        cnv.drawString(x+170, y-20, "RESUMO DE EMPRESTIMO")
        cnv.drawString(x, y-26, "________________________________________________________________________________")
        cnv.drawString(x+35, y-50, str("Data: "+str(self.data)))
        cnv.drawString(x+35, y-65, str("Valor Emprestimo: R$ "+str(self.valor)))
        cnv.drawString(x+35, y-80, str("Taxa Contrato: R$ "+str(self.taxa_contrato)))
        cnv.drawString(x+35, y-95, str("Taxa Banco: R$ "+str(self.taxa_banco)))
        cnv.drawString(x+35, y-110, str("IOF: R$ "+str(self.iof)))
        cnv.drawString(x+35, y-125, str("Total Emprestimo: R$ "+str(self.parcelas)))
        cnv.drawString(x+285, y-70, str("Parcelas: "+str(self.parcelas)))
        cnv.drawString(x+285, y-85, str("Valor Parcela: R$ "+str(self.valorParcelas)))
        cnv.drawString(x, y-144, "________________________________________________________________________________")
        cnv.drawString(x+155, y-160, "LANÇAMENTOS DO EMPRESTIMO")
        cnv.drawString(x, y-166, "________________________________________________________________________________")
        cnv.drawString(x+20, y-190, "---------------------------------------------- Banco e Taxas ----------------------------------------------------")
        cnv.drawString(x+70, y-220, str("D - Emprestimo"+ "  ...................................................."+ "R$ 0000,000"))
        if int(self.taxa_contrato) > 0:
            cnv.drawString(x+70, y-235, str("D - Taxa Contrato"+ "  ................................................"+ "R$ 0000,000"))
            y = y-235
        if int(self.taxa_banco) > 0:
            cnv.drawString(x+70, y-15, str("D - Taxa Banco"+ "  ...................................................."+ "R$ 0000,000"))
            y = y-15         
        if int(self.iof) > 0:
            cnv.drawString(x+70, y-15, str("D - IOF"+ "  ................................................................."+ "R$ 0000,000"))
            y = y-15
        if int(self.longoPrazo) >= 1:
            cnv.drawString(x+20, y-25, "------------------------------------------------ Curto Prazo ------------------------------------------------------")
            cnv.drawString(x+20, y-35, str("   [ Total de Parcelas: "+str(self.CurtoPrazo)+"]"))
            cnv.drawString(x+300, y-35, str("  [Ano "+str(self.ano)+": "+str((int(self.CurtoPrazo) - 12))+"]  [Ano "+str((int(self.ano) + 1))+ ": 12 ]"))
            cnv.drawString(x+70, y-60, str("D- (-) Encargos Emprestimo CP"+ "  .............................................."+ "R$ 0000,000"))
            cnv.drawString(x+70, y-75, str("C - Emprestimo CP"+ "  .............................................."+ "R$ 0000,000"))
            cnv.drawString(x+20, y-100, "------------------------------------------------ Longo Prazo ------------------------------------------------------")
            cnv.drawString(x+20, y-110, str("   [ Total de Parcelas: "+str(int(self.longoPrazo))+"]"))
            cnv.drawString(x+70, y-135, str("D - (-) Encargos Emprestimo LP"+ "  .............................................."+ "R$ 0000,000"))
            cnv.drawString(x+70, y-150, str("C - Emprestimo LP"+ "  .............................................."+ "R$ 0000,000"))
            cnv.drawString(x, y-174, "________________________________________________________________________________")
            cnv.drawString(x+210, y-190, "APROPRIAÇÃO")
            cnv.drawString(x, y-196, "________________________________________________________________________________")           
            y = y-192
            self.AnoApropriação = int(self.ano) + 2
            self.dataIn = "01/01/"
            while (int(self.longoPrazo) >= 12):
                cnv.drawString(x+25, y-36, str(" [ Apropriação ano subsequente:"+str(self.AnoApropriação)+"]"))
                cnv.drawString(x+260, y-28, str(" | C - Emprestimo CP"+"....."+ "R$ 0000,000" ))
                cnv.drawString(x+260, y-40, str(" | D - Emprestimo CP"+"....."+ "R$ 0000,000" ))
                self.longoPrazo = self.longoPrazo - 12
                self.AnoApropriação = self.AnoApropriação + 1
                y = y-39
        cnv.setFont("Helvetica-Oblique", 7)
        self.usuario = getpass.getuser()
        self.usuario = self.usuario.upper()
        now = datetime.now()
        self.dataHoraHoje = now.strftime('%d/%m/%Y - %H:%M:%S')
        cnv.drawString(390, 20, str(str(self.dataHoraHoje)+" - Relatorio Emitido por: "+ str(self.usuario)))
        cnv.drawString(30, 20, str('AGIR - ASSESSORIA EMPRESARIAL LTDA'))
        cnv.save()

    def Calcular_Lan(self):
        try:
            self.valor = float(self.entry_emprestimo.get().replace(".", "").replace(",", ".").replace("R$ ", ""))
        except ValueError:
            self.valor = 0.0
        try:        
            self.taxa_contrato = float(self.entry_emprestimo2.get().replace(".", "").replace(",", ".").replace("R$ ", ""))
        except ValueError:
            self.taxa_contrato = 0.0
        try:
            self.taxa_banco = float(self.entry_emprestimo3.get().replace(".", "").replace(",", ".").replace("R$ ", ""))
        except ValueError:
            self.taxa_banco = 0.0
        try:
            self.iof = float(self.entry_emprestimo4.get().replace(".", "").replace(",", ".").replace("R$ ", ""))
        except ValueError:
            self.iof = 0.0
        try:
            self.parcelas = int(self.entry_emprestimo7.get().replace(".", "").replace(",", ".").replace("R$ ", ""))
        except ValueError:
            self.parcelas = 0        
        try:
            self.valorParcelas = float(self.entry_emprestimo5.get().replace(".", "").replace(",", ".").replace("R$ ", ""))
        except ValueError:
            self.valorParcelas = 0           
        try:
            self.textData = self.entry_emprestimo60.get()
            self.data = datetime.strptime(self.textData, '%d/%m/%Y')
        except ValueError:
            print('erro value erro')
            #data = struct_time(localtime()   

        
        self.soma = self.valor + self.taxa_contrato + self.taxa_banco + self.iof
        self.encargos = self.valorParcelas

        print(type(self.data))
        print("---------------data2---------------")
        self.mes = self.data.strftime('%m')
        self.ano = self.data.strftime('%Y')
        self.ano = self.ano.replace(" ","")


        self.CurtoPrazo = (13 - int(self.mes)) + 12
        self.longoPrazo = self.parcelas - self.CurtoPrazo
        self.relatorio = '1' 
        print(self.relatorio)

