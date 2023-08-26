import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar a base de dados
base_acidentes = pd.read_parquet("base_acidentes_processada")

def obter_dados_filtrados(ano_selecionado):
    return base_acidentes[base_acidentes["ANO"] == ano_selecionado]

def top_tipos_de_acidentes(dados_filtrados):
    top_tipos = dados_filtrados["TIPO"].value_counts().head(5)
    return top_tipos

def contagem_envolvidos(dados_filtrados):
    envolvidos_cols = ['AUTOMOVEL_ENVOLVIDO', 'MOTO_ENVOLVIDA', 'CICLO_MOTOR_ENVOLVIDO', 'CICLISTA_ENVOLVIDO',
                       'PEDESTRE_ENVOLVIDO', 'ONIBUS_ENVOLVIDO', 'CAMINHAO_ENVOLVIDO', 'VIATURA_ENVOLVIDA']
    contagem_envolvidos = dados_filtrados[envolvidos_cols].sum()
    contagem_envolvidos.index = [col.replace("_ENVOLVIDO", "") for col in contagem_envolvidos.index]
    return contagem_envolvidos

def vitimas_por_bairro(dados_filtrados):
    vitimas_por_bairro = dados_filtrados.groupby("BAIRRO")["NUM_VITIMAS"].sum().sort_values(ascending=False)
    return vitimas_por_bairro

def acidentes_por_mes(dados_filtrados):
    acidentes_por_mes = dados_filtrados.groupby("MES").size()
    return acidentes_por_mes

def acidentes_por_dia(dados_filtrados):
    acidentes_por_dia = dados_filtrados.groupby("DIA").size()
    return acidentes_por_dia

def vitimas_por_turno(dados_filtrados):
    vitimas_turno = dados_filtrados.groupby(["TURNO"])["NUM_VITIMAS"].sum()
    return vitimas_turno

def aplicacao():
    st.title("Análise Geral")

    # Filtro por ano
    ano_selecionado = st.selectbox("Selecione um ano:", base_acidentes["ANO"].unique())
    dados_filtrados = obter_dados_filtrados(ano_selecionado)

    st.header("Top 5 Tipos de Acidentes na Cidade")
    top_tipos = top_tipos_de_acidentes(dados_filtrados)
    st.bar_chart(top_tipos)
    
    st.header("Quantidade de Vítimas por Bairro")
    vitimas_bairro = vitimas_por_bairro(dados_filtrados)
    st.bar_chart(vitimas_bairro)

    st.header("Quantidade de Acidentes por Mês")
    acidentes_mes = acidentes_por_mes(dados_filtrados)
    st.bar_chart(acidentes_mes)

    st.header("Quantidade de Acidentes por Dia")
    acidentes_dia = acidentes_por_dia(dados_filtrados)
    st.bar_chart(acidentes_dia)

    st.header("Contagem de Envolvidos por Tipo")
    contagem_envolvidos_tipo = contagem_envolvidos(dados_filtrados)
    st.bar_chart(contagem_envolvidos_tipo)
    
    st.header("Quantidade de Vítimas por Turno")
    vitimas_turno = vitimas_por_turno(dados_filtrados)
    st.bar_chart(vitimas_turno)

if __name__ == "__main__":
    aplicacao()
