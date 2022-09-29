import psycopg2 as pg
import pandas as pd

conn = pg.connect(
    host= 'ec2-44-207-133-100.compute-1.amazonaws.com',
    database= 'ddtauj7f93nl03',
    user= 'mglmqkvorcqaeu',
    password= '9ce06ee51049064f936937ee74d8259cd5dc46a14c80616dabe735e3b2d77b45'
)

cur = conn.cursor()

cur.execute('''SELECT 
idvenda,
round(bruto) as bruto,
round(desconto) as desconto_porcentagem,
round(bruto - (bruto * (desconto / 100))) as liquido,
data_venda,
status
FROM vendas
''')

query = cur.fetchall()

df_query = pd.DataFrame(query)

df_query.columns = ['idvenda','bruto','desconto_porcent','liquido','data_venda','status']

df_query.to_csv('vendas.csv', index=False, sep=',')