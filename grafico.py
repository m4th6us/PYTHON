import psycopg2 as pg
import pandas as pd
import plotly.express as px


#conexão com o banco
conn = pg.connect(
    host= 'ec2-44-207-133-100.compute-1.amazonaws.com',
    database= 'ddtauj7f93nl03',
    user= 'mglmqkvorcqaeu',
    password= '9ce06ee51049064f936937ee74d8259cd5dc46a14c80616dabe735e3b2d77b45'
)

#criando um cursor para executar comando sql
cur = conn.cursor()

where = int(input('Qual mes:'))

cur.execute(f'''SELECT 
count(*) as Vendas,
extract(month from data_venda) as data_venda
FROM vendas
WHERE extract(month from data_venda) = {where}
group by extract(month from data_venda)
order by 2
''')

#guardando os resultados em uma lista
query = cur.fetchall()

dicionario = dict(query)

#criando o gráfico
fig = px.line(x = dicionario , y = dicionario.keys(), title = 'Vendas X Mês', height = 850, width = 1000)
fig.show()