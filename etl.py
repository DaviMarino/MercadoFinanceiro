import config
from enums import *
import pandas as pd


def padroniza_df_yahoo(df_yahoo, papel: papeis):
    df_yahoo.rename(columns=config.DE_PARA_COLS_YAHOO, inplace=True)
    df_yahoo['Papel'] = papel._name_
    df_yahoo = df_yahoo[['Papel', 'Abertura', 'Alta', 'Baixa', 'Fechamento', 'Volume']]
    return df_yahoo


def add_media_movel_simples(df, periodo: int, campo: str):
    df_mms = pd.DataFrame(df[campo].rolling(window=periodo).mean())
    df_mms.rename(columns={campo: f'MMS{periodo}'}, inplace=True)
    df = df.join(df_mms)
    return df


def add_media_movel_exponencial(df, periodo: int, campo: str):
    df_mme = pd.DataFrame(df[campo].ewm(span=periodo).mean())
    df_mme.rename(columns={campo: f'MME{periodo}'}, inplace=True)
    df = df.join(df_mme[periodo-1:])
    return df

