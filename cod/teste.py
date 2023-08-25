import pandas as pd


df = pd.read_excel('exemplos\estedata.xlsx')
print(df)       



# Convertendo a coluna 'Data de Crédito ou Débito (No Extrato)' para o tipo datetime
df['Data de Crédito ou Débito (No Extrato)'] = pd.to_datetime(df['Data de Crédito ou Débito (No Extrato)'])

# Agrupando e somando os valores
df = df.groupby(['Data de Crédito ou Débito (No Extrato)', 'Nota Fiscal', 'AGIR']).sum().reset_index()

print(df)