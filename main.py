import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

paleta_cores = ['#81c8f8', '#0a6ac7', '#eab4b5']

dados_vendas = pd.read_csv("./data/vendas.csv", sep=";", decimal=",")

dados_vendas["Data"] = pd.to_datetime(dados_vendas["Date"])
dados_vendas = dados_vendas.sort_values("Data")

st.sidebar.write("Vendas")
st.sidebar.write("Página Principal")
st.sidebar.write("Página 2")

st.sidebar.markdown("---")

dados_vendas["Mes"] = dados_vendas["Data"].apply(lambda x: f"{x.year}-{x.month}")

mes_selecionado = st.sidebar.selectbox("Mês", dados_vendas["Mes"].unique())

dados_filtrados = dados_vendas[dados_vendas["Mes"] == mes_selecionado]

coluna1, coluna2 = st.columns(2)  
coluna3, coluna4, coluna5 = st.columns(3)  



grafico_faturamento_dia = px.bar(dados_filtrados, x="Data", y="Total", color="City", title="Faturamento por dia",
                                 color_discrete_sequence=paleta_cores)
grafico_faturamento_dia.update_layout()

coluna1.plotly_chart(grafico_faturamento_dia, use_container_width=True)

grafico_faturamento_produto = px.bar(dados_filtrados, x="Data", y="Product line", 
                                     color="City", title="Faturamento por tipo de produto",
                                     orientation="h", color_discrete_sequence=paleta_cores)
grafico_faturamento_produto.update_layout()

coluna2.plotly_chart(grafico_faturamento_produto, use_container_width=True)

faturamento_cidade = dados_filtrados.groupby("City")[["Total"]].sum().reset_index()

grafico_faturamento_cidade = px.bar(faturamento_cidade, x="City", y="Total", title="Faturamento por cidade",
                                    color_discrete_sequence=paleta_cores)
grafico_faturamento_cidade.update_layout()

coluna3.plotly_chart(grafico_faturamento_cidade, use_container_width=True)

grafico_tipo_pagamento = px.pie(dados_filtrados, values="Total", names="Payment", title="Faturamento por tipo de pagamento",
                                color_discrete_sequence=paleta_cores)
grafico_tipo_pagamento.update_layout()

coluna4.plotly_chart(grafico_tipo_pagamento, use_container_width=True)

avaliacao_media_cidade = dados_filtrados.groupby("City")[["Rating"]].mean().reset_index()

grafico_avaliacao_media = px.bar(dados_filtrados, y="Rating", x="City", title="Avaliação Média",
                                 color_discrete_sequence=paleta_cores)
grafico_avaliacao_media.update_layout()

coluna5.plotly_chart(grafico_avaliacao_media, use_container_width=True)
