import pandas as pd
import requests
import json

df = pd.read_excel('exemplo lacon.xlsx', header=[2,3])
link = 'https://integragir-default-rtdb.firebaseio.com/'

class FirebaseAPI:
    def __init__(self, firebase_url):
        self.firebase_url = firebase_url

    def post(self, data):
        url = f"{self.firebase_url}.json"
        response = requests.post(url, json=data)
        return response.json()

    def get(self):
        url = f"{self.firebase_url}.json"
        response = requests.get(url)
        return response.json()

    def patch(self, data):
        url = f"{self.firebase_url}.json"
        response = requests.patch(url, json=data)
        return response.json()

    def delete(self):
        url = f"{self.firebase_url}.json"
        response = requests.delete(url)
        return response.json()

firebase_url = "https://integragir-default-rtdb.firebaseio.com/Contratos-Lacon"
firebase_api = FirebaseAPI(firebase_url)

"""data = {"nome": "Mário Marsil Xavier da Silva", "cpf-cnpj": "600.132.147-72", "imóvel": "801 - Saint John", "valor": 2287.68, "inicio": "16/05/2020", "fim": "Indeterminado" }
response = firebase_api.post(data)
print(response)"""

response = firebase_api.get()
print(response)

"""# seleciona as linhas onde o valor da coluna "Status" é "Desocupado"
print(df)
df.dropna(subset=[('A TRIBUTAR', 'A TRIBUTAR')], inplace=True)
print(df)
#print(indicess)"""


"""def on_table_data_changed(self, top_left, bottom_right):
    # Obter o modelo da tabela
    model = self.ui.tableViewLacon.model()

    # Obter os novos dados editados
    for row in range(top_left.row(), bottom_right.row() + 1):
        # Obter o ID do item
        id_index = model.index(row, 0)
        item_id = id_index.data(Qt.DisplayRole)
        print("id_item", item_id)
        
        # Verificar se o campo de ID está vazio
        if item_id == '':
            QMessageBox.warning(self, 'Aviso', 'O campo ID não pode ser vazio.')
            model.setData(id_index, '')  # Limpar o campo ID
            return

        # Verificar se o ID já existe em outro item
        for other_row in range(model.rowCount()):
            if other_row != row:  # Ignorar a linha atual
                other_id_index = model.index(other_row, 0)
                other_item_id = other_id_index.data(Qt.DisplayRole)
                if item_id == other_item_id:
                    QMessageBox.warning(self, 'Aviso', 'Já existe outro item com o mesmo ID.')
                    model.setData(id_index, '')  # Limpar o campo ID
                    return

        # Obter as informações do item a ser atualizado
        row_data = {}
        for col in range(1, model.columnCount()):
            column_name = model.headerData(col, Qt.Horizontal)
            item_index = model.index(row, col)
            item_data = item_index.data(Qt.DisplayRole)
            row_data[column_name] = item_data

        # Atualizar os dados no Firebase
        self.firebase_api.patch(item_id, row_data)"""