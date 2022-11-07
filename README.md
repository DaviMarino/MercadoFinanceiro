# Niguém é bem vindo aqui!
😊


### Este projeto tem o objetivo de facilitar a consulta de dados financeiros da bolsa de valores, criação de análises, novos indicadores e gráficos.

#
Exemplo de consulta

```python
from enums import *
import getDados
import etl

papel = papeis.BBAS3
periodo = periodos.um_ano.value
intervalo = intervalos.um_dia.value

df_yahoo = getDados.get_fromYahoo_periodo(papel=papel, periodo=periodo, intervalo=intervalo)
df_yahoo = etl.padroniza_df_yahoo(df_yahoo=df_yahoo, papel=papel)

df_yahoo.head(3)
```


|    Date    | Papel |  Abertura |    Alta   |   Baixa   | Fechamento |  Volume  |
|:----------:|:-----:|:---------:|:---------:|:---------:|:----------:|:--------:|
| 2021-11-08 | BBAS3 | 26.980865 | 27.594912 | 26.906435 |  27.427444 |  7979400 |
| 2021-11-09 | BBAS3 | 28.283393 | 28.488077 | 27.390234 |  27.390234 | 20778600 |
| 2021-11-10 | BBAS3 | 27.464658 | 28.906738 | 27.446050 |  28.646235 | 20395200 |

#
Exemplo de análise com indicadores

```python
from enums import *
import getDados
import etl


papel = papeis.BBAS3
periodo = periodos.um_ano.value
intervalo = intervalos.um_dia.value

df_yahoo = getDados.get_fromYahoo_periodo(papel=papel, periodo=periodo, intervalo=intervalo)
df_yahoo = etl.padroniza_df_yahoo(df_yahoo=df_yahoo, papel=papel)

df_yahoo = etl.add_media_movel_simples(df=df_yahoo, periodo=9, campo='Fechamento')
df_yahoo = etl.add_media_movel_exponencial(df=df_yahoo, periodo=50, campo='Fechamento')
df_yahoo = etl.desvioPadrao(df=df_yahoo, periodo=20, campo='Fechamento')
df_yahoo = etl.bandasBollinger(df=df_yahoo, campo='MMS11', seCampoNaoExiste=True)
df_yahoo = etl.ifr(df=df_yahoo, campo='Fechamento', periodo=14)

df_yahoo[50:53]
```

|    Date    | Papel |  Abertura |    Alta   |   Baixa   | Fechamento |  Volume  |      MMS9 |     MME50 | DesvioPadrao | BandaSuperior | BandaInferior |       IFR |
|:----------:|:-----:|:---------:|:---------:|:---------:|:----------:|:--------:|----------:|----------:|-------------:|--------------:|--------------:|----------:|
| 2022-01-20 | BBAS3 | 29.501790 | 29.871628 | 29.397475 |  29.587137 | 11361000 | 28.484997 | 28.477371 |     0.816811 |     29.873303 |     26.606061 | 66.939661 |
| 2022-01-21 | BBAS3 | 29.539721 | 29.909561 | 29.293161 |  29.587137 | 14360700 | 28.739985 | 28.527102 |     0.899354 |     30.262535 |     26.665119 | 66.939661 |
| 2022-01-24 | BBAS3 | 29.520755 | 30.108705 | 29.350062 |  29.729383 | 15750300 | 28.998135 | 28.580680 |     0.976760 |     30.651838 |     26.744797 | 68.248447 |
#
Exemplo de análise com gráfico

```python
from enums import *
import getDados
import etl
import graficos


papel = papeis.BBAS3
periodo = periodos.seis_meses.value
intervalo = intervalos.um_dia.value

df_yahoo = getDados.get_fromYahoo_periodo(papel=papel, periodo=periodo, intervalo=intervalo)
df_yahoo = etl.padroniza_df_yahoo(df_yahoo=df_yahoo, papel=papel)
df_yahoo = etl.ifr(df=df_yahoo, campo='Fechamento', periodo=14)

graficos.CandleComIFR(dfGrafico=df_yahoo, LinhaSuperior=80, LinhaInfeior=20)
```


![newplot](https://user-images.githubusercontent.com/99440922/200411387-755c31f5-daef-43cc-9fc3-d5f75ebdf2fc.png)