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

   fig_candle.update_layout(title={'text': f"Gráfico de Candle",
                           'y':0.9,
                           'x':0.5,
                           'xanchor': 'center',
                           'yanchor': 'top',
                           'font':{'size':25}},
                        xaxis_rangeslider_visible=False)

   fig_candle.show()