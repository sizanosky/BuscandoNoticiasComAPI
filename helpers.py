import requests
from config import *


def cabecalho():
    """
    Formata uma cabeçalho com o título do programa.
    :return: Título
    """
    titulo = "Buscando notícias com API 'newsapi.org' - Python3"
    print(f'\n{"*" * len(titulo) + 10 * "*"}')
    print(f'{"*" * len(titulo) + 10 * "*"}')
    print(f"++++ {titulo} ++++")
    print(f'{"*" * len(titulo) + 10 * "*"}')
    print(f'{"*" * len(titulo) + 10 * "*"}\n')


def top_noticias(pais):
    """
    Função para buscar as top noticias do site "newsapi.org",
    site baseado em noticias da BBC.
    :param pais: País escolhido para a busca
    :return: Lista de noticias
    """
    url = f"{URL_BASE}country={PAIS}&category={CATEGORIA}&apiKey={API_KEY}"

    #  Coletando dados no formato JSON
    resposta = requests.get(url).json()
    #  print(resposta)

    #  Mostrando todos os artigos encontrados.
    artigos = resposta['articles']

    #  lista com as principais notícias
    lista_noticias = []

    for artigo in artigos:
        lista_noticias.append(f"Título.....: {artigo['title']}\n"
                              f"Imagem.....: {artigo['urlToImage']}\n"
                              f"Publicado..: {artigo['publishedAt']}\n")

    print(lista_noticias)

