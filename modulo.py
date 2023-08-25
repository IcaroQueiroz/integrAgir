import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from datetime import datetime

df = pd.read_excel('exemplos\exemplo lacon.xlsx', header=[2])

print(df)

if 'CONFERIDO' in df.columns:
    try:
        df = df.loc[df['CONFERIDO'] == 'OK']
    except:
        print("Erro")

df = df.reset_index(drop=False)
print(df)

txt = ''
txtM = ''
contador = 0
meu_dict = {}
for i, controlador in enumerate(df['AGIR']):
    data_timestamp = df.loc[i,'Data\nPag.\nExtrato']
    print(" -------------------", i ,"---------------------")
    data_str = data_timestamp.strftime("%d/%m/%Y")
    data_data = datetime.strptime(data_str, "%d/%m/%Y")
    data_txt = f"{data_data:%Y%m%d}"
    ValoresSimples = ['simples', 'Simples', 'SIMPLES']
    banco = "xx"
    aluguel = abs(df.loc[i,'Aluguel'])
    if aluguel > 0:
        print(aluguel)
    condominio = abs(df.loc[i,'Condomínio'])
    iptu = abs(df.loc[i,'IPTU'])
    bombeiro = abs(df.loc[i,'Bombeiro'])
    spu = abs(df.loc[i,'SPU'])
    taxaExtra = abs(df.loc[i,'Taxa Extra'])
    agua = abs(df.loc[i,'Água'])
    multaJuros = abs(df.loc[i,'Multa/Juros'])
    desconto = abs(df.loc[i,'Desconto'])
    seguro = abs(df.loc[i,'Seguro'])
    cercaEletrica = abs(df.loc[i,'Cerca Elétrica'])
    outrosGastos = abs(df.loc[i,'Outros Gastos'])
 




    cpfoucnpj = "x"
    cpfoucnpj = cpfoucnpj.replace('.', '').replace('/', '').replace('-', '')