import pandas as pd
from sqlalchemy import create_engine, String
import os

# Identificando caminhos
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

pasta_dados = os.path.join(diretorio_atual, "brazilian-ecommerce", "versions", "2")

caminho_db = os.path.join(diretorio_atual, 'olist.db')

# Lista com os nomes exatos dos arquivos CSV
arquivos = {
    "ordens": "olist_orders_dataset.csv",
    "pagamentos": "olist_order_payments_dataset.csv",
    "itens": "olist_order_items_dataset.csv",
    "vendedores": "olist_sellers_dataset.csv",
    "clientes": "olist_customers_dataset.csv",
    "geolocalizacao": "olist_geolocation_dataset.csv",
    "revisoes": "olist_order_reviews_dataset.csv",
    "produtos": "olist_products_dataset.csv"
}

# Criação dos caminhos completos
caminho_dados_ordens = os.path.join(pasta_dados, arquivos["ordens"])
caminho_dados_ordem_pagamentos = os.path.join(pasta_dados, arquivos["pagamentos"])
caminho_dados_itens = os.path.join(pasta_dados, arquivos["itens"])
caminho_dados_vendedores = os.path.join(pasta_dados, arquivos["vendedores"])
caminho_dados_clientes = os.path.join(pasta_dados, arquivos["clientes"])
caminho_dados_geolocalizacao = os.path.join(pasta_dados, arquivos["geolocalizacao"])
caminho_dados_revisoes = os.path.join(pasta_dados, arquivos["revisoes"])
caminho_dados_produtos = os.path.join(pasta_dados, arquivos["produtos"])

# Criando a conexão com o SQLite
engine = create_engine(f'sqlite:///{caminho_db}')

#criando caminhos
df_ordens = pd.read_csv(caminho_dados_ordens)
df_itens = pd.read_csv(caminho_dados_itens)
df_ordem_pagamentos = pd.read_csv(caminho_dados_ordem_pagamentos)
df_vendedores = pd.read_csv(caminho_dados_vendedores)
df_clientes = pd.read_csv(caminho_dados_clientes)
df_geolocalizacao = pd.read_csv(caminho_dados_geolocalizacao)
df_revisoes = pd.read_csv(caminho_dados_revisoes)
df_produtos = pd.read_csv(caminho_dados_produtos)

dfs = [df_ordens,
    df_itens,
    df_ordem_pagamentos,
    df_vendedores,
    df_clientes,
    df_geolocalizacao,
    df_produtos]

#convertendo colunas de data
df_ordens['order_delivered_carrier_date'] = df_ordens['order_delivered_carrier_date'].astype(str).str.slice(0,10)
df_ordens['order_delivered_carrier_date'] = pd.to_datetime(df_ordens["order_delivered_carrier_date"], format ="%Y-%m-%d")

df_ordens['order_delivered_customer_date'] = df_ordens['order_delivered_customer_date'].astype(str).str.slice(0,10)
df_ordens['order_delivered_customer_date'] = pd.to_datetime(df_ordens["order_delivered_customer_date"], format ="%Y-%m-%d")

df_ordens['order_estimated_delivery_date'] = df_ordens['order_estimated_delivery_date'].astype(str).str.slice(0,10)
df_ordens['order_estimated_delivery_date'] = pd.to_datetime(df_ordens["order_estimated_delivery_date"], format ="%Y-%m-%d")

df_itens['shipping_limit_date'] = df_itens['shipping_limit_date'].astype(str).str.slice(0,10)
df_itens['shipping_limit_date'] = pd.to_datetime(df_itens["shipping_limit_date"], format ="%Y-%m-%d")

df_revisoes['review_creation_date'] = df_revisoes['review_creation_date'].astype(str).str.slice(0,10)
df_revisoes['review_creation_date'] = pd.to_datetime(df_revisoes['review_creation_date'], format ="%Y-%m-%d")

#Forçando tipo númerico
map_itens = {'order_item_id': String}
map_pagamentos = {'payment_sequential': String, 'payment_installments': String}
map_vendedores = {'seller_zip_code_prefix': String}
map_clientes = {'customer_zip_code_prefix': String}
map_geo = {'geolocation_zip_code_prefix': String}
map_revisoes = {'review_score': String}

#Limpando valores nulos - não tem valores nulos nessas tabelas
for df in dfs:
    df.dropna()

df_ordens.to_sql('ordens', con=engine, if_exists='replace', index=False)
df_itens.to_sql('itens', con=engine, dtype=map_itens, if_exists='replace', index=False)
df_ordem_pagamentos.to_sql('ordem pagamentos', dtype=map_pagamentos, con=engine, if_exists='replace', index=False)
df_vendedores.to_sql('vendedores', con=engine, dtype=map_vendedores, if_exists='replace', index=False)
df_clientes.to_sql('clientes', con=engine, dtype=map_clientes, if_exists='replace', index=False)
df_geolocalizacao.to_sql('geolocalizacao', con=engine, dtype=map_geo, if_exists='replace', index=False)
df_revisoes.to_sql('revisoes', con=engine, dtype=map_revisoes, if_exists='replace', index=False)
df_produtos.to_sql('produtos', con=engine, if_exists='replace', index=False)

print("Dados inseridos com sucesso!")
