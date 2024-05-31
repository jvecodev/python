import pandas as pd

vendas = {
    'data': ['15/02/2021', '16/02/2021'],
    'valor': [500, 300],
    'produto': ['feijão', 'arroz'],
    'quantidade': [50, 30]
}
vendas_df = pd.DataFrame(vendas)
print('=' * 50)
print(vendas_df)
print('=' * 50)

# vendas_df1 = pd.read_excel("despesas_2.xlsx")
# print(vendas_df1)

