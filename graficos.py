import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import getDados

def Candle(dfGrafico: pd.DataFrame):
   papel = getDados.get_papel(dfGrafico.Papel[0])

   pio.templates.default = 'plotly_dark'
   fig_candle = go.Figure()
   fig_candle = make_subplots(vertical_spacing=0, rows=1, cols=1, row_heights=[1])

   fig_candle.add_trace(go.Candlestick(x=dfGrafico.index,
                              name='Candle',
                              open=dfGrafico.Abertura,
                              high=dfGrafico.Alta,
                              low=dfGrafico.Baixa,
                              close=dfGrafico.Fechamento), row=1, col=1)

   fig_candle.update_layout(title={'text': f"Análise de {papel['nome']}",
                           'y':0.9,
                           'x':0.5,
                           'xanchor': 'center',
                           'yanchor': 'top',
                           'font':{'size':25}},
                        xaxis_rangeslider_visible=False)

   fig_candle.show()


def CandleComBandasBollinger(dfGrafico: pd.DataFrame):
   papel = getDados.get_papel(dfGrafico.Papel[0])

   pio.templates.default = 'plotly_dark'
   fig_candle = go.Figure()
   fig_candle = make_subplots(vertical_spacing=0, rows=1, cols=1, row_heights=[1])

   fig_candle.add_trace(go.Candlestick(x=dfGrafico.index,
                              name='Candle',
                              open=dfGrafico.Abertura,
                              high=dfGrafico.Alta,
                              low=dfGrafico.Baixa,
                              close=dfGrafico.Fechamento), row=1, col=1)

   fig_candle.add_trace(go.Scatter(x=dfGrafico.index,
                           y=dfGrafico.BandaInferior,
                           name='Banda Inferior',
                           line_color='rgba(173,204,255,0.1)'), row=1, col=1)

   fig_candle.add_trace(go.Scatter(x=dfGrafico.index,
                           y=dfGrafico.BandaSuperior,
                           name='Banda Superior',
                           fill='tonexty',
                           fillcolor='rgba(173,204,255,0.1)',
                           line_color='rgba(173,204,255,0.1)'), row=1, col=1)

   fig_candle.add_trace(go.Scatter(x=dfGrafico.index,
                           y=dfGrafico.MMS9,
                           name='Media Movel 9',
                           line={'dash':'dash', 'color':'#FECB52', 'width':1}), row=1, col=1)
                           
   fig_candle.add_trace(go.Scatter(x=dfGrafico.index,
                           y=dfGrafico.MME50,
                           name='Media Movel 50',
                           line={'dash':'dash', 'color':'#0639FF', 'width':1}), row=1, col=1)

   fig_candle.update_layout(title={'text': f"Análise de {papel['nome']} com Bandas de Bollinger",
                           'y':0.9,
                           'x':0.5,
                           'xanchor': 'center',
                           'yanchor': 'top',
                           'font':{'size':25}},
                        xaxis_rangeslider_visible=False)

   fig_candle.show()


def CandleComIFR(dfGrafico: pd.DataFrame, LinhaSuperior:int, LinhaInfeior:int):
   papel = getDados.get_papel(dfGrafico.Papel[0])

   dfGrafico['LinhaSuperior'] = LinhaSuperior
   dfGrafico['LinhaInfeior'] = LinhaInfeior

   pio.templates.default = 'plotly_dark'
   fig_candle = go.Figure()
   fig_candle = make_subplots(vertical_spacing=0, rows=2, cols=1, row_heights=[10,3])
                           
   # Gráfico linha 1 - Candle
   fig_candle.add_trace(go.Candlestick(x=dfGrafico.index,
                              name='Candle',
                              open=dfGrafico.Abertura,
                              high=dfGrafico.Alta,
                              low=dfGrafico.Baixa,
                              close=dfGrafico.Fechamento), row=1, col=1)

   # Gráfico linha 2 - IFR
   fig_candle.add_trace(go.Scatter(x=dfGrafico.index,
                           y=dfGrafico.LinhaSuperior,
                           name='Linha Superior',
                           line_color='#FECB52'), row=2, col=1)
   fig_candle.add_trace(go.Scatter(x=dfGrafico.index,
                           y=dfGrafico.LinhaInfeior,
                           name='Linha Inferior',
                           line_color='#FECB52'), row=2, col=1)
   fig_candle.add_trace(go.Scatter(x=dfGrafico.index,
                           y=dfGrafico.IFR,
                           name='IFR',
                           line_color='#636EFA'), row=2, col=1)

   fig_candle.update_layout(title={'text': f"Análise de {papel['nome']} com IFR",
                           'y':0.9,
                           'x':0.5,
                           'xanchor': 'center',
                           'yanchor': 'top',
                           'font':{'size':25}},
                        xaxis_rangeslider_visible=False)
                        #width=300,
                        #height=700)

   fig_candle.show()