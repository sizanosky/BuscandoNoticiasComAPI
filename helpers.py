import requests
from config import *


def cabecalho(titulo, opcional=""):
    """
    Formata uma cabeçalho com o título do programa.
    :param titulo: Texto que será exibido como título.
    :param opcional: Valor opcional para ser exibido.
    :return: Título
    """

    print(f'\n{"*" * len(titulo + opcional) + 10 * "*"}')
    print(f"++++ {titulo}{opcional} ++++")
    print(f'{"*" * len(titulo + opcional) + 10 * "*"}\n')


def top_noticias(pais):
    """
    Função para buscar as top noticias do site "newsapi.org",
    site baseado em noticias da BBC.
    :param pais: País escolhido para a busca
    :return: Lista de noticias
    """
    url = f"{URL_BASE}country={pais}&category={CATEGORIA}&apiKey={API_KEY}"

    # Coletando dados no formato JSON
    resposta = requests.get(url).json()
    # print(resposta)

    # Mostrando todos os artigos encontrados.
    artigos = resposta['articles']
    # print(resposta)

    # lista com as principais notícias
    lista_noticias = []

    # Loop para buscar os itens na lista resposta e ordenar em lista_noticias
    for artigo in artigos:
        lista_noticias.append(f"{artigo['title']} ,\n\t"
                              f" URL noticia: {artigo['url']} ,\n\t"
                              f" Imagem: {artigo['urlToImage']} ,\n\t"
                              f" Publicado em: {artigo['publishedAt']} ,\n\t")

    return lista_noticias
