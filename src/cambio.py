import requests

URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL"


def buscar_cotacao_dolar():
    resposta = requests.get(URL, timeout=5)
    resposta.raise_for_status()
    dados = resposta.json()
    cotacao = float(dados["USDBRL"]["bid"])
    return cotacao


def converter_para_dolar(valor_brl):
    cotacao = buscar_cotacao_dolar()
    return round(valor_brl / cotacao, 2)
