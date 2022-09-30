from fastapi import FastAPI
import psycopg2 as pg
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

#instanciando minha API
app = FastAPI()


#criar "rotas" caminhos dos links que o user vai acessar
@app.get("/")
def home():
    return {"Escolha um Mês através da barra de pesquisa /Mes/NUMERO DO MÊS"}

@app.get("/Mes/{data}")
def pega_data(data: int):
    cur.execute(f'''SELECT
    extract(month from data_venda) as data_venda,
    count(*) as Vendas
    FROM vendas
    where extract(month from data_venda) = {data}
    group by extract(month from data_venda)
    order by 2
    ''')
    query = cur.fetchall()
    dicionario = dict(query)
    return {f'Mês {data}': dicionario[data]}


@app.get("/Grafico/{data}")
def mostra_grafico(data: int):
    cur.execute(f'''SELECT
    extract(month from data_venda) as data_venda,
    count(*) as Vendas
    FROM vendas
    where extract(month from data_venda) = {data}
    group by extract(month from data_venda)
    order by 2
    ''')
    query = cur.fetchall()
    #gera o dict
    dicionario = dict(query)
    #grafico
    fig = px.bar(x = dicionario , y = dicionario.keys(), title = 'Vendas x Mês', height = 850, width = 1000)
    return fig.show()