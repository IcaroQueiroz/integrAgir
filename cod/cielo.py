import pandas as pd

df = pd.read_excel('.\exemplos\cielo.xls', header=None)

# Identificar a linha do título da coluna
linha_titulo = df[df.iloc[:, 0] == 'Data da venda'].index[0]

# Definir o DataFrame para incluir apenas as colunas relevantes
df = df.iloc[linha_titulo:]

# Renumera as linhas a partir de 1 e remove a primeira linha duplicada do cabeçalho
df = df.reset_index(drop=True)
#df = df.drop(0)
# Definir a linha 0 como cabeçalho do DataFrame
df = df.rename(columns=df.iloc[0])

# Descartar a linha 0, pois ela foi usada como cabeçalho
df = df[1:]
# Função para analisar o conteúdo da coluna 'Forma de pagamento'
def analisar_forma_pagamento(forma_pagamento):
    if 'Crédito' in forma_pagamento:
        return 'Crédito'
    elif 'Débito' in forma_pagamento:
        return 'Débito'
    else:
        return 'Voucher'


df['Natureza'] = df['Forma de pagamento'].apply(analisar_forma_pagamento)


# # Criar DataFrame de exemplo
# data = {'Coluna': ['hipercard credito', 'cartao debito', 'credito pessoal']}
# df = pd.DataFrame(data)

# # Verificar se a célula contém a palavra 'credito'
# palavra_chave = 'credito'
# df['ContemPalavraChave'] = df['Coluna'].str.contains(palavra_chave) == True

print(df)
