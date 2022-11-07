import config
import yfinance as yf
import pandas as pd
from enums import *


def get_fromYahoo_por_datas(papel: papeis, data_inicio: str, data_fim: str, intervalo: intervalos):
    """Função para coletar os dados de ações do yFinance

    Args:
        papel (papeis): Enum papeis
        data_inicio (str): Texto de uma data no formato YYYY-MM-DD
        data_fim (str): Texto de uma data no formato YYYY-MM-DD
        intervalo (intervalos): Enum intervalos

    Returns:
        _type_: DataFrame
    """
    acao = yf.Ticker(papel.value)
    dados = acao.history(interval=intervalo, start=data_inicio, end=data_fim)
    return dados


def get_fromYahoo_periodo(papel: papeis, periodo: periodos, intervalo: intervalos):
    """Função para coletar os dados de ações do yFinance

    Args:
        papel (papeis): Enum papeis
        periodo (periodos): Enum periodos
        intervalo (intervalos): Enum intervalos

    Returns:
        _type_: DataFrame
    """
    acao = yf.Ticker(papel.value)
    dados = acao.history(period=periodo, interval=intervalo)
    return dados


def get_papeis():
    """Função para coletar os dados dos papeis que podem ser consultados no yFinance

    Returns:
        _type_: DataFrame
    """
    dicionario = {
        "AIRB34": {"nome": "Airbnb", "razaoSocial": "Airbnb, Inc.", "simbolo": "AIRB34.SA"},
        "AMZO34": {"nome": "Amazon", "razaoSocial": "Amazon.com, Inc.", "simbolo": "AMZO34.SA"},
        "ABEV3": {"nome": "Ambev", "razaoSocial": "Ambev S.A.", "simbolo": "ABEV3.SA"},
        "AALL34": {"nome": "American Airlines", "razaoSocial": "American Airlines Group Inc.", "simbolo": "AALL34.SA"},
        "AMER3": {"nome": "Americanas", "razaoSocial": "Americanas S.A.", "simbolo": "AMER3.SA"},
        "AAPL34": {"nome": "Apple", "razaoSocial": "Apple Inc.", "simbolo": "AAPL34.SA"},
        "ARZZ3": {"nome": "Arezzo", "razaoSocial": "Arezzo Indústria e Comércio S.A.", "simbolo": "ARZZ3.SA"},
        "AZUL4": {"nome": "Azul", "razaoSocial": "Azul S.A.", "simbolo": "AZUL4.SA"},
        "B3SA3": {"nome": "B3", "razaoSocial": "B3 S.A. - Brasil, Bolsa, Balcão", "simbolo": "B3SA3.SA"},
        "BBDC3": {"nome": "Bradesco 3", "razaoSocial": "Banco Bradesco S.A.", "simbolo": "BBDC3.SA"},
        "BBDC4": {"nome": "Bradesco 4", "razaoSocial": "Banco Bradesco S.A.", "simbolo": "BBDC4.SA"},
        "BBAS3": {"nome": "Banco do Brasil", "razaoSocial": "Banco do Brasil S.A.", "simbolo": "BBAS3.SA"},
        "BIDI3": {"nome": "Banco Inter 3", "razaoSocial": "Banco Inter S.A.", "simbolo": "BIDI3.SA"},
        "BIDI4": {"nome": "Banco Inter 4", "razaoSocial": "Banco Inter S.A.", "simbolo": "BIDI4.SA"},
        "BPAN4": {"nome": "Pan", "razaoSocial": "Banco Pan S.A.", "simbolo": "BPAN4.SA"},
        "SANB4": {"nome": "Santanter 4", "razaoSocial": "Banco Santander (Brasil) S.A.", "simbolo": "SANB4.SA"},
        "SANB3": {"nome": "Santander 3", "razaoSocial": "Banco Santander (Brasil) S.A.", "simbolo": "SANB3.SA"},
        "CEAB3": {"nome": "C&A", "razaoSocial": "C&A Modas S.A.", "simbolo": "CEAB3.SA"},
        "CAML3": {"nome": "Camil", "razaoSocial": "Camil Alimentos S.A.", "simbolo": "CAML3.SA"},
        "CCRO3": {"nome": "CCR", "razaoSocial": "CCR S.A.", "simbolo": "CCRO3.SA"},
        "CIEL3": {"nome": "Cielo", "razaoSocial": "Cielo S.A.", "simbolo": "CIEL3.SA"},
        "C2CA34": {"nome": "Coca-Cola Mexico", "razaoSocial": "Coca-Cola FEMSA, S.A.B. de C.V.", "simbolo": "C2CA34.SA"},
        "TEND3": {"nome": "Tenda", "razaoSocial": "Construtora Tenda S.A.", "simbolo": "TEND3.SA"},
        "CVCB3": {"nome": "CVC", "razaoSocial": "CVC Brasil Operadora e Agência de Viagens S.A.", "simbolo": "CVCB3.SA"},
        "D1EL34": {"nome": "Dell", "razaoSocial": "Dell Technologies Inc.", "simbolo": "D1EL34.SA"},
        "DEAI34": {"nome": "Delta Airlines", "razaoSocial": "Delta Air Lines, Inc.", "simbolo": "DEAI34.SA"},
        "D2PZ34": {"nome": "Domino's Pizza", "razaoSocial": "Domino's Pizza, Inc.", "simbolo": "D2PZ34.SA"},
        "EBAY34": {"nome": "eBay", "razaoSocial": "eBay Inc.", "simbolo": "EBAY34.SA"},
        "ECOR3": {"nome": "Eco Rodovias", "razaoSocial": "EcoRodovias Infraestrutura e Logística S.A.", "simbolo": "ECOR3.SA"},
        "EAIN34": {"nome": "EA", "razaoSocial": "Electronic Arts Inc.", "simbolo": "EAIN34.SA"},
        "EMBR3": {"nome": "Embraer", "razaoSocial": "Embraer S.A.", "simbolo": "EMBR3.SA"},
        "PGMN3": {"nome": "Pague Menos", "razaoSocial": "Empreendimentos Pague Menos S.A.", "simbolo": "PGMN3.SA"},
        "FLRY3": {"nome": "Fleury", "razaoSocial": "Fleury S.A.", "simbolo": "FLRY3.SA"},
        "FDMO34": {"nome": "Ford", "razaoSocial": "Ford Motor Company", "simbolo": "FDMO34.SA"},
        "GMCO34": {"nome": "GM", "razaoSocial": "General Motors Company", "simbolo": "GMCO34.SA"},
        "GETT3": {"nome": "Getnet 3", "razaoSocial": "Getnet Adquirência e Serviços para Meios de Pagamento S.A.", "simbolo": "GETT3.SA"},
        "GETT4": {"nome": "Getnet 4", "razaoSocial": "Getnet Adquirência e Serviços para Meios de Pagamento S.A.", "simbolo": "GETT4.SA"},
        "G2DD34": {"nome": "GoDaddy", "razaoSocial": "GoDaddy Inc.", "simbolo": "G2DD34.SA"},
        "GOLL4": {"nome": "Gol", "razaoSocial": "Gol Linhas Aéreas Inteligentes S.A.", "simbolo": "GOLL4.SA"},
        "HOND34": {"nome": "Honda", "razaoSocial": "HONDA MO DRN", "simbolo": "HOND34.SA"},
        "HPQB34": {"nome": "HP", "razaoSocial": "HP Inc.", "simbolo": "HPQB34.SA"},
        "ITUB3": {"nome": "Itaú 3", "razaoSocial": "Itaú Unibanco Holding S.A.", "simbolo": "ITUB3.SA"},
        "ITUB4": {"nome": "Itaú 4", "razaoSocial": "Itaú Unibanco Holding S.A.", "simbolo": "ITUB4.SA"},
        "ITSA4": {"nome": "Itaúsa 4", "razaoSocial": "Itaúsa - Investimentos Itaú SA", "simbolo": "ITSA4.SA"},
        "ITSA3": {"nome": "Itaúsa 3", "razaoSocial": "Itaúsa - Investimentos Itaú SA", "simbolo": "ITSA3.SA"},
        "JHSF3": {"nome": "JHSF", "razaoSocial": "JHSF Participações S.A.", "simbolo": "JHSF3.SA"},
        "KEPL3": {"nome": "Kepler", "razaoSocial": "Kepler Weber S.A.", "simbolo": "KEPL3.SA"},
        "KLBN3": {"nome": "Klabin 3", "razaoSocial": "Klabin S.A.", "simbolo": "KLBN3.SA"},
        "KLBN4": {"nome": "Klabin 4", "razaoSocial": "Klabin S.A.", "simbolo": "KLBN4.SA"},
        "RENT3": {"nome": "Localiza", "razaoSocial": "Localiza Rent a Car S.A.", "simbolo": "RENT3.SA"},
        "LWSA3": {"nome": "Locaweb", "razaoSocial": "Locaweb Serviços de Internet S.A.", "simbolo": "LWSA3.SA"},
        "LREN3": {"nome": "Renner", "razaoSocial": "Lojas Renner S.A.", "simbolo": "LREN3.SA"},
        "MGLU3": {"nome": "Magalu", "razaoSocial": "Magazine Luiza S.A.", "simbolo": "MGLU3.SA"},
        "LEVE3": {"nome": "Mahle", "razaoSocial": "MAHLE Metal Leve S.A.", "simbolo": "LEVE3.SA"},
        "AMAR3": {"nome": "Marisa", "razaoSocial": "Marisa Lojas S.A.", "simbolo": "AMAR3.SA"},
        "M2RV34": {"nome": "Marvell", "razaoSocial": "Marvell Technology, Inc.", "simbolo": "M2RV34.SA"},
        "MSCD34": {"nome": "Mastercard", "razaoSocial": "Mastercard Incorporated", "simbolo": "MSCD34.SA"},
        "MCDC34": {"nome": "McDonald", "razaoSocial": "McDonald's Corporation", "simbolo": "MCDC34.SA"},
        "CASH3": {"nome": "Méliuz", "razaoSocial": "Méliuz S.A.", "simbolo": "CASH3.SA"},
        "MELI34": {"nome": "Mercado Livre", "razaoSocial": "MercadoLibre, Inc.", "simbolo": "MELI34.SA"},
        "MSFT34": {"nome": "Microsoft", "razaoSocial": "Microsoft Corporation", "simbolo": "MSFT34.SA"},
        "M1UF34": {"nome": "Mitsubishi", "razaoSocial": "MITSUBISHI UDRN", "simbolo": "M1UF34.SA"},
        "M1DB34": {"nome": "MongoDB", "razaoSocial": "MongoDB, Inc.", "simbolo": "M1DB34.SA"},
        "M1SI34": {"nome": "Motorola", "razaoSocial": "Motorola Solutions, Inc.", "simbolo": "M1SI34.SA"},
        "MOVI3": {"nome": "Movida", "razaoSocial": "Movida Participações S.A.", "simbolo": "MOVI3.SA"},
        "MRVE3": {"nome": "MRV", "razaoSocial": "MRV Engenharia e Participações S.A.", "simbolo": "MRVE3.SA"},
        "MLAS3": {"nome": "Multilaser", "razaoSocial": "Multilaser Industrial S.A.", "simbolo": "MLAS3.SA"},
        "N1DA34": {"nome": "Nasdaq", "razaoSocial": "Nasdaq, Inc.", "simbolo": "N1DA34.SA"},
        "NFLX34": {"nome": "Netflix", "razaoSocial": "Netflix, Inc.", "simbolo": "NFLX34.SA"},
        "NIKE34": {"nome": "Nike", "razaoSocial": "NIKE, Inc.", "simbolo": "NIKE34.SA"},
        "NOKI34": {"nome": "Nokia", "razaoSocial": "Nokia Corporation", "simbolo": "NOKI34.SA"},
        "NUBR33": {"nome": "Nubank", "razaoSocial": "Nu Holdings Ltd.", "simbolo": "NUBR33.SA"},
        "ORCL34": {"nome": "Oracle", "razaoSocial": "Oracle Corporation", "simbolo": "ORCL34.SA"},
        "PAGS34": {"nome": "PagSeguro", "razaoSocial": "PagSeguro Digital Ltd.", "simbolo": "PAGS34.SA"},
        "C1BS34": {"nome": "Paramount", "razaoSocial": "Paramount Global", "simbolo": "C1BS34.SA"},
        "PYPL34": {"nome": "Paypal", "razaoSocial": "PayPal Holdings, Inc.", "simbolo": "PYPL34.SA"},
        "PEPB34": {"nome": "Pepsi", "razaoSocial": "PepsiCo, Inc.", "simbolo": "PEPB34.SA"},
        "PETR3": {"nome": "Petrobras 3", "razaoSocial": "Petróleo Brasileiro S.A. - Petrobras", "simbolo": "PETR3.SA"},
        "PETR4": {"nome": "Petrobras 4", "razaoSocial": "Petróleo Brasileiro S.A. - Petrobras", "simbolo": "PETR4.SA"},
        "PFIZ34": {"nome": "Pfizer", "razaoSocial": "Pfizer Inc.", "simbolo": "PFIZ34.SA"},
        "POSI3": {"nome": "Positivo", "razaoSocial": "Positivo Tecnologia S.A.", "simbolo": "POSI3.SA"},
        "RADL3": {"nome": "Raia Drogasil", "razaoSocial": "Raia Drogasil S.A.", "simbolo": "RADL3.SA"},
        "SSFO34": {"nome": "Salesforce", "razaoSocial": "Salesforce, Inc.", "simbolo": "SSFO34.SA"},
        "SNEC34": {"nome": "Sony", "razaoSocial": "SONY GROUP DRN", "simbolo": "SNEC34.SA"},
        "S1PO34": {"nome": "Spotify", "razaoSocial": "Spotify Technology S.A.", "simbolo": "S1PO34.SA"},
        "SBUB34": {"nome": "Starbucks", "razaoSocial": "Starbucks Corporation", "simbolo": "SBUB34.SA"},
        "TASA4": {"nome": "Taurus 4", "razaoSocial": "Taurus Armas S.A.", "simbolo": "TASA4.SA"},
        "TASA3": {"nome": "Taurus 3", "razaoSocial": "Taurus Armas S.A.", "simbolo": "TASA3.SA"},
        "TSLA34": {"nome": "Tesla", "razaoSocial": "Tesla, Inc.", "simbolo": "TSLA34.SA"},
        "COCA34": {"nome": "Coca-Cola", "razaoSocial": "The Coca-Cola Company", "simbolo": "COCA34.SA"},
        "DISB34": {"nome": "Walt Disney", "razaoSocial": "The Walt Disney Company", "simbolo": "DISB34.SA"},
        "TOTS3": {"nome": "Totvs", "razaoSocial": "TOTVS S.A.", "simbolo": "TOTS3.SA"},
        "TMCO34": {"nome": "Toyota", "razaoSocial": "TOYOTAMO DRN", "simbolo": "TMCO34.SA"},
        "T1RI34": {"nome": "Tripadvisor", "razaoSocial": "Tripadvisor, Inc.", "simbolo": "T1RI34.SA"},
        "TWTR34": {"nome": "Twitter", "razaoSocial": "Twitter, Inc.", "simbolo": "TWTR34.SA"},
        "U1BE34": {"nome": "Uber", "razaoSocial": "Uber Technologies, Inc.", "simbolo": "U1BE34.SA"},
        "U1AL34": {"nome": "United Airlines", "razaoSocial": "United Airlines Holdings, Inc.", "simbolo": "U1AL34.SA"},
        "VALE3": {"nome": "Vale", "razaoSocial": "Vale S.A.", "simbolo": "VALE3.SA"},
        "VIIA3": {"nome": "Via Varejo", "razaoSocial": "Via S.A.", "simbolo": "VIIA3.SA"},
        "VISA34": {"nome": "Visa", "razaoSocial": "Visa Inc.", "simbolo": "VISA34.SA"},
        "VIVA3": {"nome": "Vivara", "razaoSocial": "Vivara Participações S.A.", "simbolo": "VIVA3.SA"},
        "WALM34": {"nome": "Walmart", "razaoSocial": "Walmart Inc.", "simbolo": "WALM34.SA"},
        "W1BD34": {"nome": "Warner Bros", "razaoSocial": "Warner Bros. Discovery, Inc.", "simbolo": "W1BD34.SA"},
        "W1MG34": {"nome": "Warner Music", "razaoSocial": "Warner Music Group Corp.", "simbolo": "W1MG34.SA"},
        "DOLFUT": {"nome": "Dolar", "razaoSocial": "Dolar Americano", "simbolo": "USDBRL=x"},
        "WINFUT": {"nome": "Indice Futuro", "razaoSocial": "Indice Futuro", "simbolo": "^BVSP"}
    }
    papeis = pd.DataFrame(dicionario)
    return papeis


def get_papel(codigo: str):
    """Função para coletar no .CSV os dados de um dos papeis que podem ser consultados no yFinance

    Args:
        codigo (papeis): Enum papeis _name_

    Returns:
        _type_: DataFrame
    """
    papeis = get_papeis()[codigo]
    papel = papeis.to_dict()
    return papel
