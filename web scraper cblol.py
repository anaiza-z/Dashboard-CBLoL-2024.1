import requests
from bs4 import BeautifulSoup
import re
import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

win_rate = []
times = []
ouro_por_min = []
abates = []
mortes = []
torres_derrubadas = []
torres_perdidas = []
cabecalho = {'user-agent': 'Mozilla/5.0'}

def extrair_dados(lista_dados, inicio, destino):
    for i in range(inicio, len(lista_dados), 30):
        destino.append(lista_dados[i].text)

#WEB SCRAPING

link = "https://gol.gg/teams/list/season-ALL/split-ALL/tournament-CBLOL%20Split%201%202024/"
requisicao = requests.get(link, headers=cabecalho) #obter dados do site

site = BeautifulSoup(requisicao.text, "html.parser") #dados organizados

lista_times = site.find_all('a', {'href':
    re.compile('./team-stats/.*/split-ALL/tournament-CBLOL Split 1 2024/')}) #coleta de forma genérica

for i in range(len(lista_times)):
    times.append(lista_times[i].text)

lista_dados = site.find_all('td', {'class': 'text-center'})

extrair_dados(lista_dados, 3, win_rate)
extrair_dados(lista_dados, 5, ouro_por_min)
extrair_dados(lista_dados, 8, abates)
extrair_dados(lista_dados, 9, mortes)
extrair_dados(lista_dados, 10, torres_derrubadas)
extrair_dados(lista_dados, 11, torres_perdidas)


df_cblol = pd.DataFrame({'Time': times, 'Win Rate': win_rate, 'Ouro por minuto': ouro_por_min,
                         'Abates': abates, 'Mortes': mortes, 'Torres derrubadas': torres_derrubadas,
                         'Torres perdidas': torres_perdidas})

#colunas numéricas para o tipo certo
df_cblol['Win Rate'] = df_cblol['Win Rate'].str.rstrip('%').astype('float')
df_cblol['Abates'] = df_cblol['Abates'].astype(float)
df_cblol['Mortes'] = df_cblol['Mortes'].astype(float)
df_cblol['Torres derrubadas'] = df_cblol['Torres derrubadas'].astype(float)
df_cblol['Torres perdidas'] = df_cblol['Torres perdidas'].astype(float)
df_cblol['Ouro por minuto'] = df_cblol['Ouro por minuto'].astype(int)
print(df_cblol)

#DASHBOARD

app = dash.Dash(__name__)

app.layout = dash.html.Div(children=[
    dash.html.H1(
        children='Dashboard de Desempenho dos Times CbLoL 2024.1',
        style={'marginTop': 50, 'marginLeft': 60}
    ),

    dash.dcc.Graph(
        id='win-rate-bar',
        figure=px.bar(df_cblol.sort_values('Win Rate'), x='Time', y='Win Rate', title='Win Rate por Time (%)')
    ),

    dash.dcc.Graph(
        id='torres-derrubadas-perdidas-scatter',
        figure=px.scatter(df_cblol, x='Torres perdidas', y='Torres derrubadas', color='Time', title='Torres derrubadas vs perdidas (MÉDIA)')
    ),

    dash.dcc.Graph(
        id='ouro-por-min-horizontal',
        figure=px.bar(df_cblol, x='Ouro por minuto', y='Time', title='Ouro por minuto (MÉDIA)')
    ),

    dash.dcc.Graph(
        id='abates-mortes-scatter',
        figure=px.scatter(df_cblol, x='Mortes', y='Abates', color='Time', title='Abates vs Mortes (MÉDIA)')
    ),

    dash.dcc.Graph(
        id='abates-mortes-bar',
        figure=go.Figure(data=[
            go.Bar(name='Abates', x=df_cblol['Time'], y=df_cblol['Abates']),
            go.Bar(name='Mortes', x=df_cblol['Time'], y=df_cblol['Mortes'])
        ]).update_layout(
            barmode='group',
            title='Abates e Mortes por Time (MÉDIA)',
            xaxis_title='Time',
            yaxis_title='Quantidade'
        )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)