import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


base_acidentes = pd.read_parquet("base_acidentes_processada")

def obter_bairros():
    return base_acidentes["BAIRRO"].unique()

def grafico_acidentes_por_ano(dados_bairro):
    anos = [2019, 2020, 2021]
    acidentes_por_ano = dados_bairro.groupby("ANO").size().reindex(anos, fill_value=0)
    return acidentes_por_ano




def grafico_vitimas_por_dia(dados_bairro):
    vitimas_por_dia = dados_bairro.groupby("DIA")["NUM_VITIMAS"].sum()
    return vitimas_por_dia

def grafico_vitimas_por_mes(dados_bairro):
    vitimas_por_mes = dados_bairro.groupby("MES")["NUM_VITIMAS"].sum()
    return vitimas_por_mes

def grafico_vitimas_por_turno(dados_bairro):
    vitimas_por_turno = dados_bairro.groupby("TURNO")["NUM_VITIMAS"].sum()
    return vitimas_por_turno

def analise_bairro():
    st.title("Análise por Bairro")

    
    bairros = obter_bairros()
    bairro_selecionado = st.selectbox("Selecione um bairro:", bairros)

    
    dados_bairro = base_acidentes[base_acidentes["BAIRRO"] == bairro_selecionado]

    st.header("Quantidade de Acidentes ao Longo dos Anos")
    acidentes_por_ano = grafico_acidentes_por_ano(dados_bairro)
    st.bar_chart(acidentes_por_ano)

    st.header("Vítimas por Dia")
    vitimas_por_dia = grafico_vitimas_por_dia(dados_bairro)
    st.line_chart(vitimas_por_dia)

    st.header("Vítimas por Mês")
    vitimas_por_mes = grafico_vitimas_por_mes(dados_bairro)
    st.line_chart(vitimas_por_mes)

    st.header("Vítimas por Turno")
    vitimas_por_turno = grafico_vitimas_por_turno(dados_bairro)
    st.bar_chart(vitimas_por_turno)

if __name__ == "__main__":
    analise_bairro()