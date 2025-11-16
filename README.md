
# Pipeline ETL Python - IMDB Top Séries

Projeto backend para coleta e transformação automatizada dos dados das 25 séries mais bem avaliadas do IMDB Top 250, utilizando Python, pandas e SQLite.

## Objetivo

Extrair, tratar e armazenar informações das séries do IMDB, estruturando os dados para uso em pipelines ETL, análises ou integrações.

## Requisitos

- Python 3.12.1
- pandas
- sqlite3

## Estrutura do Projeto

- `data/data.jsonl`: Dados coletados das séries do IMDB em formato JSON.
- `src/transformation/app.py`: Script de transformação dos dados e posteriormente guarda no banco SQLite.

## Instalação

1. Clone o repositório:
  ```sh
  git clone https://github.com/gabrielmelhor2/Pipeline_ETL_Python_Scrapy_IMDB.git
  cd Pipeline_ETL_Python_Scrapy_IMDB
  ```

2. Crie e ative o ambiente virtual:
  ```sh
  python -m venv .venv
  .venv\Scripts\activate
  ```

3. Instale as dependências:
  ```sh
  pip install scrapy

  pip install pandas

## Execução

1.Navegue até a pasta coleta:
    cd coleta

  Execute o spider IMDB:
        ```sh
    scrapy crawl imdb -o ../data/data.jsonl
    ```
    


2. Certifique-se de que o arquivo `data/data.jsonl` está presente com os dados das séries.

3. Execute o script de transformação:
  ```sh
  cd src/transformation
  python app.py
  ```
4. Os dados tratados serão salvos na tabela `imdb_top_tv` do banco SQLite em `data/database.db`.

## Transformações realizadas

- Conversão da coluna `rating` para float.
- Extração dos anos de início e fim das séries (`ano_inicio`, `ano_fim`).
- Remoção da coluna original `year`.
- Adição das colunas `_source` e `_data_coleta`.

