
# 📊 Dashboard de Desempenho dos Times do CBLOL 2024.1

Este projeto utiliza a biblioteca Dash para criar um dashboard interativo que exibe dados de desempenho dos times do CBLoL 2024.1. Os dados são obtidos por meio de web scraping do site gol.gg e processados com pandas.

## 🔎 Requisitos
- **requests**: Para fazer requisições HTTP e obter dados do site.
- **beautifulsoup4**: Para fazer o parsing do HTML.
- **re**: Para expressões regulares usadas na extração de URLs específicas.
- **dash**: Para criar o dashboard interativo.
- **pandas**: Para manipulação e análise de dados.
- **plotly**: Para visualização de dados com gráficos interativos.

Você pode instalar as bibliotecas necessárias utilizando o pip:

```
pip install requests beautifulsoup4 dash pandas plotly  
```
## 👩🏻‍💻 Estrutura do Código

### Web Scraping
O código faz uma requisição ao site gol.gg e processa os dados usando BeautifulSoup. Os dados extraídos são armazenados em um DataFrame do pandas e as colunas são convertidas para os tipos de dados apropriados.

### Dashboard
O Dash é usado para criar um dashboard interativo com vários gráficos:

    - Gráfico de barras do Win Rate por Time.
    - Gráfico de dispersão de Torres Derrubadas vs. Torres Perdidas.
    - Gráfico de barras horizontal de Ouro por Minuto.
    - Gráfico de dispersão de Abates vs. Mortes.
    - Gráfico de barras de Abates e Mortes por Time.


## Screenshots

![win_rate](https://github.com/anaiza-z/Dashboard-CBLoL-2024.1/assets/173067555/a3bcc44d-6f40-421b-93e3-ad5b75652116)
![torres](https://github.com/anaiza-z/Dashboard-CBLoL-2024.1/assets/173067555/34596814-527e-49b0-84c4-d474ca9af464)
![ouro](https://github.com/anaiza-z/Dashboard-CBLoL-2024.1/assets/173067555/47e4bed8-3be9-4106-9892-12d89f60129f)
![abates_mortes_](https://github.com/anaiza-z/Dashboard-CBLoL-2024.1/assets/173067555/e0edb890-1f13-41b2-a939-ea4fc7692da6)
![abates_mortes](https://github.com/anaiza-z/Dashboard-CBLoL-2024.1/assets/173067555/485f144a-cba0-42aa-815d-a25a47eefea5)



