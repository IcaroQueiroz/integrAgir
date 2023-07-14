# import pandas as pd
# import requests
# import json

# df = pd.read_excel('exemplo lacon.xlsx', header=[2,3])


from datetime import datetime, timedelta
import calendar

data = datetime(2022, 5, 14)

for i in range(5):
    ultimo_dia_mes = calendar.monthrange(data.year, data.month)[1]
    data_ultimo_dia = datetime(data.year, data.month, ultimo_dia_mes)
    print(data_ultimo_dia.strftime('%d/%m/%Y'))
    data = data_ultimo_dia + timedelta(days=1)
    data = datetime(data.year, data.month, 1)