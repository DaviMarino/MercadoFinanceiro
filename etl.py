import config
from enums import *
import pandas as pd
import etl


def padroniza_df_yahoo(df_yahoo: pd.DataFrame, papel: papeis):
    """Função para padronizar o DataFrame das ações do yFinance renomeando as colunas e reordenando para o padrão

    Args:
        df_yahoo (DataFrame): Dados que o yFinance fornece
        papel (papeis): Enum papeis

    Returns:
        _type_: DataFrame
    """
    df_yahoo.rename(columns=config.DE_PARA_COLS_YAHOO, inplace=True)
    df_yahoo['Papel'] = papel._name_
    df_yahoo = df_yahoo[['Papel', 'Abertura', 'Alta', 'Baixa', 'Fechamento', 'Volume']]
    return df_yahoo


def add_media_movel_simples(df: pd.DataFrame, periodo: int, campo: str):
    """Recebe o DataFrame do yFinance e adiciona um campo de Média Móvel de acordo com o período e campo escolhido

    Args:
        df (DataFrame): DataFrame do yFinance já padronizado
        periodo (int): Período que a média deve considerar
        campo (str): Campo para calcular a média

    Returns:
        _type_: DataFrame
    """
    df_mms = pd.DataFrame(df[campo].rolling(window=periodo).mean())
    df_mms.rename(columns={campo: f'MMS{periodo}'}, inplace=True)
    df = df.join(df_mms)
    return df


def add_media_movel_exponencial(df: pd.DataFrame, periodo: int, campo: str):
    """Recebe o DataFrame do yFinance e adiciona um campo de Média Móvel de acordo com o período e campo escolhido

    Args:
        df (DataFrame): DataFrame do yFinance já padronizado
        periodo (int): Período que a média deve considerar
        campo (str): Campo para calcular a média

    Returns:
        _type_: DataFrame
    """
    df_mme = pd.DataFrame(df[campo].ewm(span=periodo).mean())
    df_mme.rename(columns={campo: f'MME{periodo}'}, inplace=True)
    df = df.join(df_mme[periodo-1:])
    return df


def desvioPadrao(df: pd.DataFrame, campo: str='Fechamento', periodo: int=20):
    """Recebe o DataFrame do yFinance e adiciona um campo de DesvioPadrao de acordo com o período e campo escolhido

    Args:
        df (_type_): DataFrame do yFinance já padronizado
        campo (str, optional): Campo para calcular o DesvioPadrao. Padrão='Fechamento'.
        periodo (int, optional): Período que a média deve considerar. Padrão=20.

    Returns:
        _type_: Dataframe
    """
    df_desvioPadrao = pd.DataFrame(df[campo].rolling(window=periodo).std())
    df_desvioPadrao.rename(columns={campo: 'DesvioPadrao'}, inplace=True)
    df = df.join(df_desvioPadrao)
    return df


def bandasBollinger(df: pd.DataFrame, seCampoNaoExiste: bool, campo: str='Fechamento'):
    """Recebe o DataFrame do yFinance e adiciona os campos de BandaSuperior e BandaInferior de acordo com o campo escolhido

    ⚠️ Para executar esta função precisa existir o campo DesvioPadrao no DataFrame

    Args:
        df (DataFrame): DataFrame do yFinance já padronizado
        seCampoNaoExiste (bool): Caso o campo escolhido não exista no DataFrame, informe True para criar automaticamente ou False para não criar
        campo (str): Campo para calcular as Bandas. Padrão='Fechamento'

    Returns:
        _type_: DataFrame
    """
    tudoCerto = True
    if 'DesvioPadrao' not in df.columns:
        print(f'{config.PRINT_FAIL}ERRO: Para criar Bandas de Bollinger, falta o campo "DesvioPadrão"{config.PRINT_ENDC}')
        tudoCerto = False

    if (campo not in df.columns) and (not seCampoNaoExiste == True):
        print(f'{config.PRINT_FAIL}ERRO: Para criar Bandas de Bollinger, falta o campo "{campo}"{config.PRINT_ENDC}')
        tudoCerto = False

    if campo[:3] == 'MMS' and seCampoNaoExiste == True:
        df = etl.add_media_movel_simples(df=df, periodo=int(campo[3:]), campo='Fechamento')
    elif campo[:3] == 'MME' and seCampoNaoExiste == True:
        df = etl.add_media_movel_exponencial(df=df, periodo=int(campo[3:]), campo='Fechamento')
    elif seCampoNaoExiste == True:
        print(f'{config.PRINT_FAIL}ERRO: Para criar Bandas de Bollinger, precisa digitar um campo válido, MMS ou MME{config.PRINT_ENDC}')
        tudoCerto = False

    if tudoCerto == True:
        bandaSuperior = pd.DataFrame(df[campo] + 2 * df['DesvioPadrao'])
        bandaInferior = pd.DataFrame(df[campo] - 2 * df['DesvioPadrao'])
        bandaSuperior.rename(columns={0: 'BandaSuperior'}, inplace=True)
        bandaInferior.rename(columns={0: 'BandaInferior'}, inplace=True)
        df = df.join(bandaSuperior).join(bandaInferior)
        df.drop(columns=[campo], inplace=True)
        return df


def ifr(df: pd.DataFrame, campo:str='Fechamento', periodo:int=14):
    """Recebe o DataFrame do yFinance e adiciona o campo de IFR de acordo com o período campo escolhido

    Args:
        df (DataFrame): DataFrame do yFinance já padronizado
        campo (str, optional): Campo para calcular as Bandas. Defaults to 'Fechamento'.
        periodo (int, optional): Período que a média deve considerar. Defaults to 14.

    Returns:
        _type_: DataFrame
    """
    df.reset_index(inplace=True)
    df['Dif'] = df[campo].diff(1)
    df['ganho'] = df['Dif'].clip(lower=0).round(2)
    df['perda'] = df['Dif'].clip(upper=0).abs().round(2)
    df['MediaMovelGanho'] = df['ganho'].rolling(window=periodo, min_periods=periodo).mean()[:periodo+1]
    df['MediaMovelPerda'] = df['perda'].rolling(window=periodo, min_periods=periodo).mean()[:periodo+1]    
    for i in range(periodo+1, len(df)):
        df.loc[i, 'MediaMovelGanho'] = (df.loc[i-1, 'MediaMovelGanho'] * (periodo-1) + df.loc[i, 'ganho']) / periodo
        df.loc[i, 'MediaMovelPerda'] = (df.loc[i-1, 'MediaMovelPerda'] * (periodo-1) + df.loc[i, 'perda']) / periodo
    df['IFR'] = 100 - (100 / (1 + (df.MediaMovelGanho / df.MediaMovelPerda)))
    df.drop(columns=['Dif', 'ganho', 'perda', 'MediaMovelGanho', 'MediaMovelPerda'], inplace=True)
    df.set_index('Date', inplace=True)
    return df