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
    print(" -----------------------", i ,"-------------------------")
    data_str = data_timestamp.strftime("%d/%m/%Y")
    data_data = datetime.strptime(data_str, "%d/%m/%Y")
    data_txt = f"{data_data:%Y%m%d}"
    competencia_timestamp = df.loc[i,'Mês/\nRef.']
    competencia_str = competencia_timestamp.strftime("%d/%m/%Y")
    competencia_competencia = datetime.strptime(competencia_str, "%d/%m/%Y")
    competencia_txt = f"{competencia_competencia:%m%Y}"

    ValoresSimples = ['simples', 'Simples', 'SIMPLES']
    banco = "xxXxx"
    bancoValor = round(df.loc[i,'Receita\nBruta\n(Extrato)'],2)
    contSimples = 0
    lancarBancoSimples = 0
    lanSim = ''

    imovel = df.loc[i,'Imóvel']
    aluguel = abs(df.loc[i,'Aluguel'])
    aluguelConta = "5556"
    condominio = abs(df.loc[i,'Condomínio'])
    condominioConta = "5555555"		
    iptu = abs(df.loc[i,'IPTU'])
    iptuConta = "5555555"		
    bombeiro = abs(df.loc[i,'Bombeiro'])
    bombeiroConta = 0		
    spu = abs(df.loc[i,'SPU'])
    spuConta = 5454		
    taxaExtra = abs(df.loc[i,'Taxa Extra'])
    taxaExtraConta = 5
    agua = abs(df.loc[i,'Água'])
    aguaConta = 55
    multaJuros = abs(df.loc[i,'Multa/Juros'])
    multaJurosConta = 546
    desconto = abs(df.loc[i,'Desconto'])
    descontoConta = 546		
    seguro = abs(df.loc[i,'Seguro'])		
    seguroConta = 546
    cercaEletrica = abs(df.loc[i,'Cerca Elétrica'])
    cercaEletricaConta = 5464
    outrosGastos = abs(df.loc[i,'Outros Gastos'])
    outrosGastosConta = 6545
    
    if controlador in ValoresSimples:
        valoresSimplesContador = [aluguel, condominio, iptu, bombeiro, spu, taxaExtra, agua, multaJuros, desconto, seguro, cercaEletrica, outrosGastos]
        
        for valor in valoresSimplesContador:
            if valor > 0:
                contSimples += 1
        
        if contSimples > 1:
            bancoSimples = 0
            lancarBancoSimples = 1
            contSimples = 1
        else:
            bancoSimples = banco
 
        if aluguel > 0:
            lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ","+str(aluguelConta)+","+str(bancoSimples)+"," + str(aluguel) + ",00000000," + "Recebimento de Aluguel do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contSimples += 1
            
        if condominio > 0:
            lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(condominioConta)+"," + str(condominio) + ",00000000," + "Recuperação de condominio do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contSimples += 1
            
        if iptu > 0:
            lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(iptuConta)+"," + str(iptu) + ",00000000," + "Recuperação de IPTU do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contSimples += 1
            
        if bombeiro > 0:
            lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(bombeiroConta)+"," + str(bombeiro) + ",00000000," + "Recuperação da taxa do bombeiro do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contSimples += 1
            
        if spu > 0:
            lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(spuConta)+"," + str(spu) + ",00000000," + "Recuperação de SPU do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contSimples += 1
            
        if taxaExtra > 0:
            lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(taxaExtraConta)+"," + str(taxaExtra) + ",00000000," + "Recuperação de Taxas Extras do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contSimples += 1
            
        if agua > 0:
            lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(aguaConta)+"," + str(agua) + ",00000000," + "Recuperação de Agua e Esgoto do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contSimples += 1
            
        if multaJuros > 0:
            lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(multaJurosConta)+"," + str(multaJuros) + ",00000000," + "Valor Referente a Multas e Jutos do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contSimples += 1
            
        if desconto > 0:
            lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(descontoConta)+"," + str(desconto) + ",00000000," + "Valor Referente a Desconto do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contSimples += 1

        if seguro > 0:
            lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(seguroConta)+"," + str(seguro) + ",00000000," + "Recuperação de Seguros do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contSimples += 1
            
        if cercaEletrica > 0:
            lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(cercaEletricaConta)+"," + str(cercaEletrica) + ",00000000," + "Recuperação de Cerca Eletrica do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contSimples += 1
            
        if outrosGastos > 0:
            lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(outrosGastosConta)+"," + str(outrosGastos) + ",00000000," + "Recuperação de Gastos no Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contSimples += 1

        if lancarBancoSimples == 1:
            lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ","+str(banco)+",0," + str(bancoValor) + ",00000000," + "Recebimento do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"


        print(lanSim)
    else:
        MultVerificação = str(df.loc[i,'AGIR']) + str(df.loc[i,'Data\nPag.\nExtrato'])
        print("MultVerificação", MultVerificação)
        try:
            contador = meu_dict[MultVerificação][1]
            valorSoma = float(meu_dict[MultVerificação][0])
        except:    
            contador = 1
            valorSoma = 0.0
        lanMult = ''

        if aluguel > 0:
            lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ","+str(aluguelConta)+",0," + str(aluguel) + ",00000000," + "Recebimento de Aluguel do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contador += 1
            
        if condominio > 0:
            lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(condominioConta)+"," + str(condominio) + ",00000000," + "Recuperação de condominio do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contador += 1
            
        if iptu > 0:
            lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(iptuConta)+"," + str(iptu) + ",00000000," + "Recuperação de IPTU do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contador += 1
            
        if bombeiro > 0:
            lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(bombeiroConta)+"," + str(bombeiro) + ",00000000," + "Recuperação da taxa do bombeiro do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contador += 1
            
        if spu > 0:
            lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(spuConta)+"," + str(spu) + ",00000000," + "Recuperação de SPU do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contador += 1
            
        if taxaExtra > 0:
            lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(taxaExtraConta)+"," + str(taxaExtra) + ",00000000," + "Recuperação de Taxas Extras do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contador += 1
            
        if agua > 0:
            lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(aguaConta)+"," + str(agua) + ",00000000," + "Recuperação de Agua e Esgoto do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contador += 1
            
        if multaJuros > 0:
            lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(multaJurosConta)+"," + str(multaJuros) + ",00000000," + "Valor Referente a Multas e Jutos do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contador += 1
            
        if desconto > 0:
            lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(descontoConta)+"," + str(desconto) + ",00000000," + "Valor Referente a Desconto do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contador += 1

        if seguro > 0:
            lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(seguroConta)+"," + str(seguro) + ",00000000," + "Recuperação de Seguros do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contador += 1
            
        if cercaEletrica > 0:
            lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(cercaEletricaConta)+"," + str(cercaEletrica) + ",00000000," + "Recuperação de Cerca Eletrica do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contador += 1
            
        if outrosGastos > 0:
            lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(outrosGastosConta)+"," + str(outrosGastos) + ",00000000," + "Recuperação de Gastos no Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
            contador += 1

            valorSoma = valorSoma + float(bancoValor)
            meu_dict[MultVerificação] = [valorSoma,contador,banco,data_txt]

        print(lanMult)

        

    cpfoucnpj = "x"
    cpfoucnpj = cpfoucnpj.replace('.', '').replace('/', '').replace('-', '')



print(meu_dict)