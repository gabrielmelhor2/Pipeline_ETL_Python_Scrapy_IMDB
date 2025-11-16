import pandas as pd
import sqlite3
import datetime

df = pd.read_json("../../data/data.jsonl", lines=True)

# Configura o pandas para exibir todas as colunas
pd.options.display.max_columns = None

# Adiciona a coluna _source com o valor um valor fixo
df['_source'] = 'https://www.imdb.com/pt/chart/toptv/'

# Adiciona a coluna data_coleta com a data e hora atual
df['_data_coleta'] = datetime.datetime.now()

# Trata coluna rating: converter para float e trocar vírgula por ponto
df['rating'] = df['rating'].str.replace(',', '.', regex=False).astype(float)

# Trata coluna year: extrair ano inicial e final
def extrair_anos(valor):
	if pd.isnull(valor):
		return pd.NA, pd.NA
	partes = str(valor).split('–')
	ano_inicio = partes[0].strip() if partes[0].strip().isdigit() else pd.NA
	if len(partes) > 1:
		ano_fim = partes[1].strip()
		ano_fim = ano_fim if ano_fim.isdigit() else pd.NA
	else:
		ano_fim = pd.NA
	return ano_inicio, ano_fim


df[['ano_inicio', 'ano_fim']] = df['year'].apply(lambda x: pd.Series(extrair_anos(x)))

# Remove a coluna year
df = df.drop(columns=['year'])

# Conecta ao banco de dados SQLite e/ou cria o banco de dados se não existir
conn = sqlite3.connect('../../data/database.db')

df.to_sql("imdb_top_tv", conn, if_exists="replace", index=False)

# Fecha a conexão com o banco de dados
conn.close()

# ...existing code...
print(df)