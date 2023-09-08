import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from datetime import datetime

df = pd.read_excel('exemplos\exemplo lacon.xlsx', header=[2])

data_dict= {'0001': {'01-imovel': '101 - Vila Beira Rio', '02-locatario': 'Itapicuru Agro Industrial S/A', '03-cpf-cnpj': '10.319.846/0013-86', '04-valor': 2818.5, '05-inicio': '2014-07-30', '06-fim': 'indeterminado'}, '0002': {'01-imovel': '701 - Vila Beira Rio', '02-locatario': 'Wanessa Costa de Carvalho', '03-cpf-cnpj': '065.111.754-21', '04-valor': 4278.12, '05-inicio': '2022-02-01', '06-fim': '2024-08-01'}, '0003': {'01-imovel': '901 - Saint Joseph', '02-locatario': 'Maria Alice Rodrigues Barros', '03-cpf-cnpj': '034.882.824-14', '04-valor': 7271.74, '05-inicio': '2018-12-20', '06-fim': '2021-06-20'}, '0004': {'01-imovel': '901 - Vila Beira Rio', '02-locatario': 'Francisco Eduardo de Lima Andrade', '03-cpf-cnpj': '408.155.524-91', '04-valor': 8014.7, '05-inicio': '2007-07-01', '06-fim': 'indeterminado'}, '0005': {'01-imovel': '126 - Casa Afonso Bat.', '02-locatario': 'Brasil Ortopedia Com. E Imp. de prod. Cirurgicos e hosp. Ltda', '03-cpf-cnpj': '12.257.361/0001-05', '04-valor': 6016.6, '05-inicio': '2021-02-15', '06-fim': '2023-08-15'}, '0006': {'01-imovel': '96 - Casa Afonso Bat.', '02-locatario': 'Brasil Ortopedia Com. E Imp. de prod. Cirurgicos e hosp. Ltda', '03-cpf-cnpj': '12.257.361/0001-05', '04-valor': 6275.58, '05-inicio': '2021-02-15', '06-fim': '2023-08-15'}, '0007': {'01-imovel': '601 - Saint John', '02-locatario': 'Bianca de Oliveira Ferraz Gominho', '03-cpf-cnpj': '020.244.632-82', '04-valor': 2280.39, '05-inicio': '2021-08-10', '06-fim': '2024-02-10'}, '0008': {'01-imovel': '602 - Saint John', '02-locatario': 'Guilherme Lima Caminha filho', '03-cpf-cnpj': '051.707.594-60', '04-valor': 2445.3, '05-inicio': '2020-12-22', '06-fim': '2023-06-22'}, '0009': {'01-imovel': '801 - Saint John', '02-locatario': 'Aline de Souza Vieira', '03-cpf-cnpj': '027.646.684-57', '04-valor': 2500.0, '05-inicio': '2022-11-20', '06-fim': '2025-05-20'}, '0010': {'01-imovel': '802 - Saint John', '02-locatario': "Suely Cristina D'Almeida Silva", '03-cpf-cnpj': '254.038.934-15', '04-valor': 2411.0, '05-inicio': '2021-01-11', '06-fim': '2023-07-11'}, '0011': {'01-imovel': '701 - Saint John', '02-locatario': 'Linaldo Tavares dos Santos Junior', '03-cpf-cnpj': '818.880.404-59', '04-valor': 2445.3, '05-inicio': '2020-12-05', '06-fim': '2023-06-05'}, '0012': {'01-imovel': '702 - Saint John', '02-locatario': 'Guilherme Costa Torres', '03-cpf-cnpj': '085.721.096-33', '04-valor': 2486.58, '05-inicio': '2021-02-01', '06-fim': '2023-08-01'}, '0013': {'01-imovel': '120 - Casa Ruy Bapt', '02-locatario': 'JPLL Comércio e Serviços EIRELI', 
'03-cpf-cnpj': '05.994.622/0003-68', '04-valor': 10000.0, '05-inicio': '2020-10-20', '06-fim': '2025-10-20'}, '0014': {'01-imovel': '1101 - Saint Sebastien', '02-locatario': 'Vera Maria Santos Correia de Araújo', '03-cpf-cnpj': '583.558.714-72', '04-valor': 4258.32, '05-inicio': '2021-03-01', '06-fim': '2023-09-01'}, '0015': {'01-imovel': '1102 - Saint Sebastien', '02-locatario': 'Manfredo Alberto Guimarães Hopper Júnior', '03-cpf-cnpj': '684.028.134-53', '04-valor': 4500.0, '05-inicio': '2023-05-18', '06-fim': '2025-11-18'}, '0016': {'01-imovel': '1202 - Saint Sebastien', '02-locatario': 'Paulo Jorge Rocha Saunders', '03-cpf-cnpj': '848.324.014-91', '04-valor': 4606.85, '05-inicio': '2012-03-05', '06-fim': 'indeterminado'}, '0017': {'01-imovel': '401 - Saint Martin', '02-locatario': 'José Marques Filho', '03-cpf-cnpj': '093.713.704-91', '04-valor': 4100.0, '05-inicio': '2009-10-15', '06-fim': 'indeterminado'}, '0018': {'01-imovel': '501 - Saint Martin', '02-locatario': 'José Simão de Sá Lima', '03-cpf-cnpj': '083.977.674-87', '04-valor': 4456.22, '05-inicio': '2017-10-10', '06-fim': '2020-04-10'}, '0019': {'01-imovel': '502 - Saint Martin', '02-locatario': 'Pedro Aureliano Almeida', '03-cpf-cnpj': '009.937.344-05', '04-valor': 4134.38, '05-inicio': '2019-09-01', '06-fim': '2022-03-01'}, '0020': {'01-imovel': '601 - Saint Martin', '02-locatario': 'Sandra Maria Durand Rêgo', '03-cpf-cnpj': '292.771.245-04', '04-valor': 3856.0, '05-inicio': '2010-06-01', '06-fim': 'indeterminado'}, '0021': {'01-imovel': '302 - Jaqueira Garden', '02-locatario': 'Desocupado', '03-cpf-cnpj': '', '04-valor': '', '05-inicio': '', '06-fim': ''}, '0022': {'01-imovel': '401 - Maria Amélia', '02-locatario': 'Itapicuru Agro Industrial S/A', '03-cpf-cnpj': '10.319.846/0013-86', '04-valor': 3977.05, '05-inicio': '2014-06-30', '06-fim': 'indeterminado'}, '0023': {'01-imovel': '402 - Maria Amélia', '02-locatario': 'José Marques de Souza Neto', '03-cpf-cnpj': '395.995.665-72', '04-valor': 3044.31, '05-inicio': '2016-05-02', '06-fim': '2018-11-02'}, '0024': {'01-imovel': '301 - Maria Irene', '02-locatario': 'Daniela Knecht', '03-cpf-cnpj': '640.052.834-20', '04-valor': 2758.46, '05-inicio': '2020-10-13', '06-fim': '2023-04-13'}, '0025': {'01-imovel': '302 - Maria Irene', '02-locatario': 'Rafael Carneiro Proto', '03-cpf-cnpj': '057.474.794-07', '04-valor': 3054.0, '05-inicio': '2021-01-11', '06-fim': '2023-07-11'}, '0026': {'01-imovel': '401 - Maria Irene', '02-locatario': 'CM Locação e Serviços Ltda', '03-cpf-cnpj': '11.819.193/0001-23', '04-valor': 4023.0, '05-inicio': 'Processo de aditivo', '06-fim': ''}, '0027': {'01-imovel': '801 - Maria Irene', '02-locatario': 'Bruna Guedes Moreira', '03-cpf-cnpj': '055.432.474-19', '04-valor': 3432.29, '05-inicio': '2017-07-07', '06-fim': '2020-01-07'}, '0028': {'01-imovel': '1002 - Maria Irene', '02-locatario': 'Desocupado', '03-cpf-cnpj': '', '04-valor': '', '05-inicio': '', '06-fim': ''}, '0029': {'01-imovel': '1102 - Maria Irene', '02-locatario': 'Caio Muniz de Araújo Bezerra', '03-cpf-cnpj': '088.254.874-36', '04-valor': 3792.72, '05-inicio': '2021-12-20', '06-fim': '2024-06-20'}, '0030': {'01-imovel': '101 - Costa Rêgo', '02-locatario': 'Antônio Reinaldo de Souza Filho', '03-cpf-cnpj': '012.518.683-55', '04-valor': 2379.12, '05-inicio': '2021-06-05', '06-fim': '2023-12-04'}, '0031': {'01-imovel': '601 - Costa Rêgo', '02-locatario': 'Leandro Lima Soares da Silva', '03-cpf-cnpj': '019.615.834-61', '04-valor': 3629.88, '05-inicio': '2021-01-20', '06-fim': '2023-07-20'}, '0032': {'01-imovel': '602 - Costa Rêgo', '02-locatario': 'Antônio Carlos Ferreira de Souza Jr', '03-cpf-cnpj': '051.831.001-38', '04-valor': 3548.59, '05-inicio': '2016-01-25', '06-fim': '2019-01-25'}, '0033': {'01-imovel': '301 - São Gabriel', '02-locatario': 'Cristiana Altino de Almeida', '03-cpf-cnpj': '168.509.634-49', '04-valor': 3000.0, '05-inicio': '2022-08-15', '06-fim': '2025-02-15'}, '0034': {'01-imovel': '401 - São Gabriel', '02-locatario': 'Darlan Antônio Andrade Moutinho', '03-cpf-cnpj': '068.957.274-34', '04-valor': 3000.0, '05-inicio': '2023-04-14', '06-fim': '2025-10-14'}, '0035': {'01-imovel': '301 - Jardim da Aurora', '02-locatario': 'Jairo José do Amaral Costa Junior', '03-cpf-cnpj': '008.280.534-21', '04-valor': 4000.0, '05-inicio': '2022-10-05', '06-fim': '2025-04-05'}, '0036': {'01-imovel': '401 - Jardim da Aurora', '02-locatario': 'Valcler Antônio Cabral Rodrigues', '03-cpf-cnpj': '023.048.033-00', '04-valor': 4000.0, '05-inicio': '2022-08-15', '06-fim': '2025-02-15'}, '0037': {'01-imovel': '402 - Jardim da Aurora', '02-locatario': 'Priscila Belmiro Pessoa de Albuquerque', '03-cpf-cnpj': '053.860.355-09', '04-valor': 4000.0, '05-inicio': '2023-01-30', '06-fim': '2025-07-30'}, '0038': {'01-imovel': '465 - Casa Boa Viagem', '02-locatario': 'SOMAR - Creche Crianças Especiais LRV', '03-cpf-cnpj': '09.004.589/0001-70', '04-valor': 9593.86, '05-inicio': '2016-08-08', '06-fim': '2020-08-08'}, '0039': {'01-imovel': '101 - IBIJAU-SP', '02-locatario': 'Bernardo Rodrigues Besouchet', '03-cpf-cnpj': '097.541.447-02', '04-valor': 4261.98, '05-inicio': '2020-07-10', '06-fim': '2023-01-10'}, '0040': {'01-imovel': '111 - IBIJAU-SP', '02-locatario': 'Gustavo da Silva Porto', '03-cpf-cnpj': '088.104.857-77', '04-valor': 4500.0, 
'05-inicio': '2023-02-24', '06-fim': '2025-08-24'}, '0041': {'01-imovel': '112 - IBIJAU-SP', '02-locatario': 'Abelardo Melo de Oliveira Neto', '03-cpf-cnpj': '080.232.644-78', '04-valor': 4500.0, '05-inicio': '2023-01-15', '06-fim': '2025-07-15'}, '0042': {'01-imovel': '181 - Maison Blanche-SP', '02-locatario': 'Desocupado', '03-cpf-cnpj': '', '04-valor': '', '05-inicio': '', '06-fim': ''}, '0043': {'01-imovel': '91 - Arte 2-SP', '02-locatario': 'Leandro Ribeiro de Souza Cruz', '03-cpf-cnpj': '107.305.927-82', '04-valor': 20658.0, '05-inicio': '2021-04-05', '06-fim': '2023-10-04'}, '0044': {'01-imovel': '400 - CASA 400', '02-locatario': 'Tama Representações de Confecções Ltda', '03-cpf-cnpj': '09.512.877/0001-36', '04-valor': 12887.03, '05-inicio': '2019-11-27', '06-fim': '2020-11-27'}}

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
    for chave, valor in data_dict.items():
        if valor.get('01-imovel') ==  imovel:
            cpf_cnpj = valor.get('03-cpf-cnpj')
            print(f'O CPF/CNPJ correspondente a {imovel}: {cpf_cnpj}')
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

        txt += lanSim

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

        txt += lanMult
        valorSoma = valorSoma + float(bancoValor)
        meu_dict[MultVerificação] = [valorSoma,contador,banco,data_txt]


        

    cpfoucnpj = "x"
    cpfoucnpj = cpfoucnpj.replace('.', '').replace('/', '').replace('-', '')

for chave, valor in meu_dict.items():
    valorSoma, contador, banco, data_txt = valor
    lanMultFinal = str('{:06d}'.format(contador)) +"," + str(data_txt) + ","+str(banco)+",0," + str(round(valorSoma,2)) + ",00000000," + "Recebimento diversos" + ",,," + "\n"
    txt += lanMultFinal


print(meu_dict)
print(txt)