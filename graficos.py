import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import getDados



def LinhasPrevisão2(df_previsao: pd.DataFrame, papel: str, df_prever: pd.DataFrame):
   pio.templates.default = 'plotly_dark'
   fig_candle = go.Figure()
   fig_candle = make_subplots(rows=2, cols=1) #vertical_spacing=0, row_heights=[5,5]

   fig_candle.add_trace(go.Scatter(x=df_previsao.index,
                           y=df_previsao.Real,
                           name='Real',
                           mode='lines+markers',
                           marker=dict(color='Orange')), row=1, col=1)

   fig_candle.add_trace(go.Scatter(x=df_previsao.index,
                           y=df_previsao.Previsao,
                           name='Previsão Teste',
                           mode='lines+markers',
                           marker=dict(color='Cyan')), row=1, col=1)

   fig_candle.add_trace(go.Scatter(x=df_prever.index,
                           y=df_prever.Previsao,
                           name='Previsão Futuro',
                           mode='lines+markers',
                           marker=dict(color='#fd79a8')), row=1, col=1)

   fig_candle.add_trace(go.Scatter(x=df_previsao.index,
                           y=df_previsao.Diferenca,
                           name='Diferença',
                           mode='lines+markers',
                           line_color='#2ecc71',
                           line=dict(dash='dot')), row=2, col=1)

   fig_candle.add_trace(go.Scatter(x=df_prever.index,
                           y=df_prever.Diferenca * 0,
                           name='Previsão',
                           line_color='rgba(0,0,0,0)',
                           showlegend=False), row=2, col=1)

   fig_candle.add_trace(go.Scatter(x=df_previsao.index,
                           y=df_previsao.Diferenca * 0,
                           name='Diferença',
                           line_color='#cccddd',
                           line=dict(dash='dot'),
                           showlegend=False), row=2, col=1)

   fig_candle.update_layout(title={'text': f"Previsão de {papel}",
                           'y':0.9,
                           'x':0.5,
                           'xanchor': 'center',
                           'yanchor': 'top',
                           'font':{'size':25}},
                     xaxis_rangeslider_visible=False,
                     height=700)

   fig_candle.show()


def LinhasPrevisão(df_previsao: pd.DataFrame, papel: str):
   pio.templates.default = 'plotly_dark'
   fig_candle = go.Figure()
   fig_candle = make_subplots(rows=2, cols=1) #vertical_spacing=0, row_heights=[5,5]

   fig_candle.add_trace(go.Scatter(x=df_previsao.index,
                           y=df_previsao.Real,
                           name='Real',
                           mode='lines+markers',
                           marker=dict(color='Orange')), row=1, col=1)

   fig_candle.add_trace(go.Scatter(x=df_previsao.index,
                           y=df_previsao.Previsao,
                           name='Previsão',
                           mode='lines+markers',
                           marker=dict(color='Cyan')), row=1, col=1)

   fig_candle.add_trace(go.Scatter(x=df_previsao.index,
                           y=df_previsao.Diferenca,
                           name='Diferença',
                           mode='lines+markers',
                           line_color='#2ecc71',
                           line=dict(dash='dot')), row=2, col=1)

   fig_candle.add_trace(go.Scatter(x=df_previsao.index,
                           y=df_previsao.Diferenca * 0,
                           name='Diferença',
                           line_color='#cccddd',
                           line=dict(dash='dot'),
                           showlegend=False), row=2, col=1)

   fig_candle.update_layout(title={'text': f"Previsão de {papel}",
                           'y':0.9,
                           'x':0.5,
                           'xanchor': 'center',
                           'yanchor': 'top',
                           'font':{'size':25}},
                     xaxis_rangeslider_visible=False,
                     height=700)

   fig_candle.show()


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