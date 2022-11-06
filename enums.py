from enum import Enum


class periodos(Enum):
    um_dia = '1d'
    cinco_dias = '5d'
    um_mes = '1mo'
    tres_meses = '3mo'
    seis_meses = '6mo'
    um_ano = '1y'
    dois_anos = '2y'
    cinco_anos = '5y'
    dez_anos = '10y'
    este_ano = 'ytd'
    tudo = 'max'


class intervalos(Enum):
    um_minuto = '1m'
    cinco_minutos = '5m'
    quinze_minutos = '15m'
    um_dia = '1d'
    uma_semana = '1wk'
    um_mes = '1mo'


class papeis(Enum):
    AIRB34 = 'AIRB34.SA'
    AMZO34 = 'AMZO34.SA'
    ABEV3 = 'ABEV3.SA'
    AALL34 = 'AALL34.SA'
    AMER3 = 'AMER3.SA'
    AAPL34 = 'AAPL34.SA'
    ARZZ3 = 'ARZZ3.SA'
    AZUL4 = 'AZUL4.SA'
    B3SA3 = 'B3SA3.SA'
    BBDC3 = 'BBDC3.SA'
    BBDC4 = 'BBDC4.SA'
    BBAS3 = 'BBAS3.SA'
    BIDI3 = 'BIDI3.SA'
    BIDI4 = 'BIDI4.SA'
    BPAN4 = 'BPAN4.SA'
    SANB4 = 'SANB4.SA'
    SANB3 = 'SANB3.SA'
    CEAB3 = 'CEAB3.SA'
    CAML3 = 'CAML3.SA'
    CCRO3 = 'CCRO3.SA'
    CIEL3 = 'CIEL3.SA'
    C2CA34 = 'C2CA34.SA'
    TEND3 = 'TEND3.SA'
    CVCB3 = 'CVCB3.SA'
    D1EL34 = 'D1EL34.SA'
    DEAI34 = 'DEAI34.SA'
    D2PZ34 = 'D2PZ34.SA'
    EBAY34 = 'EBAY34.SA'
    ECOR3 = 'ECOR3.SA'
    EAIN34 = 'EAIN34.SA'
    EMBR3 = 'EMBR3.SA'
    PGMN3 = 'PGMN3.SA'
    FLRY3 = 'FLRY3.SA'
    FDMO34 = 'FDMO34.SA'
    GMCO34 = 'GMCO34.SA'
    GETT3 = 'GETT3.SA'
    GETT4 = 'GETT4.SA'
    G2DD34 = 'G2DD34.SA'
    GOLL4 = 'GOLL4.SA'
    HOND34 = 'HOND34.SA'
    HPQB34 = 'HPQB34.SA'
    ITUB3 = 'ITUB3.SA'
    ITUB4 = 'ITUB4.SA'
    ITSA4 = 'ITSA4.SA'
    ITSA3 = 'ITSA3.SA'
    JHSF3 = 'JHSF3.SA'
    KEPL3 = 'KEPL3.SA'
    KLBN3 = 'KLBN3.SA'
    KLBN4 = 'KLBN4.SA'
    RENT3 = 'RENT3.SA'
    LWSA3 = 'LWSA3.SA'
    LREN3 = 'LREN3.SA'
    MGLU3 = 'MGLU3.SA'
    LEVE3 = 'LEVE3.SA'
    AMAR3 = 'AMAR3.SA'
    M2RV34 = 'M2RV34.SA'
    MSCD34 = 'MSCD34.SA'
    MCDC34 = 'MCDC34.SA'
    CASH3 = 'CASH3.SA'
    MELI34 = 'MELI34.SA'
    MSFT34 = 'MSFT34.SA'
    M1UF34 = 'M1UF34.SA'
    M1DB34 = 'M1DB34.SA'
    M1SI34 = 'M1SI34.SA'
    MOVI3 = 'MOVI3.SA'
    MRVE3 = 'MRVE3.SA'
    MLAS3 = 'MLAS3.SA'
    N1DA34 = 'N1DA34.SA'
    NFLX34 = 'NFLX34.SA'
    NIKE34 = 'NIKE34.SA'
    NOKI34 = 'NOKI34.SA'
    NUBR33 = 'NUBR33.SA'
    ORCL34 = 'ORCL34.SA'
    PAGS34 = 'PAGS34.SA'
    C1BS34 = 'C1BS34.SA'
    PYPL34 = 'PYPL34.SA'
    PEPB34 = 'PEPB34.SA'
    PETR3 = 'PETR3.SA'
    PETR4 = 'PETR4.SA'
    PFIZ34 = 'PFIZ34.SA'
    POSI3 = 'POSI3.SA'
    RADL3 = 'RADL3.SA'
    SSFO34 = 'SSFO34.SA'
    SNEC34 = 'SNEC34.SA'
    S1PO34 = 'S1PO34.SA'
    SBUB34 = 'SBUB34.SA'
    TASA4 = 'TASA4.SA'
    TASA3 = 'TASA3.SA'
    TSLA34 = 'TSLA34.SA'
    COCA34 = 'COCA34.SA'
    DISB34 = 'DISB34.SA'
    TOTS3 = 'TOTS3.SA'
    TMCO34 = 'TMCO34.SA'
    T1RI34 = 'T1RI34.SA'
    TWTR34 = 'TWTR34.SA'
    U1BE34 = 'U1BE34.SA'
    U1AL34 = 'U1AL34.SA'
    VALE3 = 'VALE3.SA'
    VIIA3 = 'VIIA3.SA'
    VISA34 = 'VISA34.SA'
    VIVA3 = 'VIVA3.SA'
    WALM34 = 'WALM34.SA'
    W1BD34 = 'W1BD34.SA'
    W1MG34 = 'W1MG34.SA'
    DOLFUT = 'USDBRL=x'
    WINFUT = '^BVSP'
