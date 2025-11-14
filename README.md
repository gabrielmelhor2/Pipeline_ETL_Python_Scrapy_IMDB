# Pipeline ETL Python - Web Scraping com Scrapy IMDB

Projeto backend para coleta automatizada dos dados dE 25 filmes do IMDB Top 250 utilizando Python e Scrapy.

## Objetivo

Extrair informações detalhadas dos filmes mais bem avaliados do IMDB, estruturando os dados para uso em pipelines ETL, análises ou integrações.

## Requisitos

- Python 3.12.1
- Scrapy 2.13.3
- Ambiente virtual recomendado (`python -m venv .venv`)

## Estrutura do Projeto

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/gabrielmelhor2/Pipeline_ETL_Python_Scrapy_IMDB.git
   cd Pipeline_ETL_Python_Scrapy_IMDB
```

2. Crie e ative o ambiente virtual:
  python -m venv .venv
  .venv\Scripts\activate

3. Instale as dependências:
  pip install scrapy

## Execução
  1.Navegue até a pasta coleta:
    cd coleta

  2.Execute o spider IMDB:
    scrapy crawl imdb -o data.csv
