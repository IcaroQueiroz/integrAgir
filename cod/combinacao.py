import numpy as np
from itertools import combinations

def combinacoes_com_tolerancia(valores, alvo, tolerancia=1e-6):
  """
  Encontra combinações de valores de uma lista que somem a um valor alvo,
  permitindo uma tolerância para lidar com possíveis erros de arredondamento.

  Args:
    valores: Lista de valores numéricos.
    alvo: Valor alvo que a soma da combinação deve atingir.
    tolerancia: Diferença máxima permitida entre a soma e o alvo (padrão: 1e-6).

  Returns:
    Lista de tuplas representando combinações válidas (índices dos valores na lista).
  """

  combinacoes_encontradas = []
  for tamanho_combinacao in range(1, len(valores) + 1):
    for combinacao in combinations(range(len(valores)), tamanho_combinacao):
      soma = sum(valores[i] for i in combinacao)
      if abs(soma - alvo) <= tolerancia:
        combinacoes_encontradas.append(combinacao)
  return combinacoes_encontradas

# Carregue seus valores (substitua pela sua lista real)
valores = [
    0.01, 913.00, 827.19, 624.13, 913.13, 150.00, 966.86, 
    150.00, 834.74, 472.39, 472.39, 823.05, 439.12, 515.96, 
    398.36, 409.55, 447.05, 338.83, 302.71, 466.24, 585.24, 
    564.18, 331.28, 413.23, 39.00, 466.24, 559.58, 239.62, 
    39.00, 784.74, 39.00, 195.00, 39.00, 440.43, 440.04, 
    39.00, 363.40, 719.07, 39.00, 195.00, 39.00, 345.79, 
    39.00, 39.00, 39.00, 412.32, 440.43, 381.36, 459.76, 
    386.19, 529.38, 396.55, 195.00, 780.00, 636.82, 39.00, 
    39.00, 521.76, 521.76, 273.00, 544.82, 873.05, 313.30
]

# Defina o valor alvo
alvo = 21620.47

# Encontre combinações com uma tolerância de 1e-6 (ajustável)
combinacoes = combinacoes_com_tolerancia(valores, alvo)

# Imprima os resultados
print(f"Combinações encontradas: {len(combinacoes)}")
for combinacao in combinacoes:
  valores_combinacao = [valores[i] for i in combinacao]
  soma = sum(valores_combinacao)
  print(f"- Valores: {valores_combinacao}")
  print(f"- Soma: {soma:.6f}")  # Formata a soma com 6 casas decimais
