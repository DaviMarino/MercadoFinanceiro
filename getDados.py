import config
import yfinance as yf
import pandas as pd
from enums import *


def get_fromYahoo_por_datas(papel: papeis, data_inicio: str, data_fim: str, intervalo: intervalos):
    acao = yf.Ticker(papel.value)
    dados = acao.history(interval=intervalo, start=data_inicio, end=data_fim)
    return dados


def get_fromYahoo_periodo(papel: papeis, periodo: periodos, intervalo: intervalos):
    acao = yf.Ticker(papel.value)
    dados = acao.history(period=periodo, interval=intervalo)
    return dados


def get_papeis():
    return pd.read_csv(r'papeis.csv', delimiter=';')


def get_papel(codigo: str):
    papel = get_papeis().query(f'Codigo == "{codigo}"')
    return papel