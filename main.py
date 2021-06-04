"""
* Módulo 20 - Buscando notícias com API
* Criado por Marcos Fabricio Sizanosky
* Professor: Jefferson Santos
* Data criação: 02/06/2021
  Programa em Python 3 para pesquisar notícias com a API "newsapi.org".
"""
from helpers import *
print("Hello World!")

if __name__ == '__main__':

    # Cabeçalho.
    cabecalho("Buscando notícias BR com API 'newsapi.org'")

    # Variável armazena o retorno da função que busca as notícias.
    lista_noticias = top_noticias(PAIS)

    # Loop para percorrer os itens da lista_noticias e imprimir na tela
    print(f"\n==== Top noticias {PAIS.upper()} ====\n")
    for numero in range(len(lista_noticias)):
        print(f"{numero + 1} - {lista_noticias[numero]}")  # {item_lista[índice]
