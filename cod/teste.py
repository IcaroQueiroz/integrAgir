import pandas as pd
from datetime import datetime

df = pd.read_excel('exemplos\estedata.xlsx')

df = df.dropna(axis=1, how='all')

print(df)    
txt = ''
for i, hitorico in enumerate (df['HISTÓRICO']):
    data_timestamp = df.loc[i, 'DATA']
    data_str = data_timestamp.strftime("%Y-%m-%d %H:%M:%S")
    data_data = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
    data_mes = f"{data_data:%m}"
    data_ano = f"{data_data:%Y}"
    data_txt = f"{data_data:%Y%m%d}"
    parcelas = df.loc[i, 'Nº PAR']
    vlr_parcelas = df.loc[i, 'VALOR PAR']
    curto_prazo = (12 - int(data_mes)) + 12
    longo_prazo = int(parcelas) - curto_prazo
    intercaladas = df.loc[i, 'Nº INT']
    intercaladas_anos = df.loc[i, 'ANO']
    vlr_intercaladas = df.loc[i, 'VALOR INT']
    longo_prazo_intercaladas = (float(intercaladas) - float(intercaladas_anos) * 2.0)
    cpfoucnpj = df.loc[i, 'PARTICIPANTE']


    parc_valor = longo_prazo * vlr_parcelas
    inter_vlr = (longo_prazo_intercaladas * vlr_intercaladas)
    if longo_prazo_intercaladas >= 1:
        hits_intercalada = ") (Intercaladas:"+ str(int(longo_prazo_intercaladas)) +"x R$"+ str(vlr_intercaladas) +")"
        valor = inter_vlr + parc_valor
    else:
        hits_intercalada = ")"
        valor = parc_valor
    lanSimp = "000001" + "," + str(data_txt) + ",2348,16," + str(valor) + ",00000000," + "Vlr. Ref. transf. p/ Longo prazo (Parcelas:"+ str(longo_prazo) +"x R$"+ str(vlr_parcelas) + str(hits_intercalada) + " " +str(hitorico)+",,"+ str(cpfoucnpj) + "," + str(cpfoucnpj) + ",""\n"
    txt += str(lanSimp)
    ano_apropriação = int(data_ano) + 1
    dataIn = "0102"

    while (int(longo_prazo) >= 12):
        data_whil = str(ano_apropriação)+str(dataIn)
        parc_valor12 = 12 * vlr_parcelas
        longo_prazo = longo_prazo - 12
        ano_apropriação = ano_apropriação + 1
        if longo_prazo_intercaladas >= 1:
            longo_prazo_intercaladas = longo_prazo_intercaladas - intercaladas_anos
            inter_vlr1 = intercaladas_anos * vlr_intercaladas
            hits_intercalada = ") (Intercaladas:"+ str(int(intercaladas_anos)) +"x R$"+ str(vlr_intercaladas) +")"
            valor = inter_vlr1 + parc_valor12
        else:
            hits_intercalada = ")"
            valor = parc_valor12
        lanSimp = "000001" + "," + str(data_whil) + ",16,2348," + str(valor) + ",00000000," + "Vlr. Ref. transf. p/Curto Prazo (Parcelas:"+ str(12) +"x R$"+ str(vlr_parcelas) + str(hits_intercalada) + " " +str(hitorico)+",,"+ str(cpfoucnpj) + "," + str(cpfoucnpj) + ",""\n"
        txt += str(lanSimp)


    if int(longo_prazo) >= 1:
        data_whil = str(ano_apropriação)+str(dataIn)
        parc_valor12 = longo_prazo * vlr_parcelas

        if longo_prazo_intercaladas >= 1:
            inter_vlr1 = longo_prazo_intercaladas * vlr_intercaladas
            hits_intercalada = ") (Intercaladas:"+ str(int(longo_prazo_intercaladas)) +"x R$"+ str(vlr_intercaladas) +")"
            valor = inter_vlr1 + parc_valor12
        else:
            hits_intercalada = ")"
            valor = parc_valor12
        lanSimp = "000001" + "," + str(data_whil) + ",16,2348," + str(valor) + ",00000000," + "Vlr. Ref. transf. p/Curto Prazo (Parcelas:"+ str(longo_prazo) +"x R$"+ str(vlr_parcelas) + str(hits_intercalada) + " " +str(hitorico)+",,"+ str(cpfoucnpj) + "," + str(cpfoucnpj) + ",""\n"
        txt += str(lanSimp)   

print(txt)

"""# Convertendo a coluna 'Data de Crédito ou Débito (No Extrato)' para o tipo datetime
df['Data de Crédito ou Débito (No Extrato)'] = pd.to_datetime(df['Data de Crédito ou Débito (No Extrato)'])

# Agrupando e somando os valores
df = df.groupby(['Data de Crédito ou Débito (No Extrato)', 'Nota Fiscal', 'AGIR']).sum().reset_index()

print(df)"""