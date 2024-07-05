import itertools

def encontrar_combinacao(valores, objetivo):
    for r in range(1, len(valores) + 1):
        for combinacao in itertools.combinations(valores, r):
            if sum(combinacao) == objetivo:
                return combinacao
    return None

valores = [
    915.25, 659.30, 273.00, 593.90, 240.00, 606.00, 195.00, 613.00, 481.25, 392.37, 
    750.00, 545.10, 312.00, 476.69, 200.00, 195.00, 323.94, 1510.00, 1484.45, 1905.55, 
    434.95, 195.00, 551.32, 537.13, 1516.70, 705.27, 310.39, 195.00, 534.23, 650.00, 
    1124.45, 635.29, 608.09, 234.00, 595.91, 520.77, 327.91, 653.75, 518.34, 620.66, 
    732.20, 620.09, 606.00, 195.00, 595.00, 535.68, 1839.15, 1840.17, 378.91, 575.30, 
    531.96, 1424.30, 195.00, 343.32, 550.00, 195.00, 550.00, 1593.15, 3495.85, 1143.85, 
    525.68, 39.00, 668.30, 1097.83, 472.46, 1389.00, 596.70
]
objetivo = 4987.64

resultado = encontrar_combinacao(valores, objetivo)
if resultado:
    print(f"A combinação que soma {objetivo} é: {resultado}")
else:
    print(f"Não há combinação que some {objetivo}")
