import streamlit as st
import pandas as pd

def obter_bairros(base_acidentes):
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

def obter_dados_filtrados(ano_selecionado,base_acidentes):
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



def analise_bairro(base_acidentes):
    st.title("Análise por Bairro")
        
    bairros = obter_bairros(base_acidentes)
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

def analise_ano(base_acidentes):
    st.title("Análise por Ano")
    
    ano_selecionado = st.selectbox("Selecione um ano:", base_acidentes["ANO"].unique())
    dados_filtrados = obter_dados_filtrados(ano_selecionado,base_acidentes)

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

def pagina_sobre():
    st.title("Sobre o Projeto")
    
    st.markdown(
        """
        Bem-vindo ao Dashboard de Análise de Acidentes na Cidade do Recife. 
        Aqui você poderá explorar dados sobre acidentes ocorridos na cidade, 
        segmentados por bairro, ano e visualizar a análise completa da cidade.
        """
    )
    
    st.markdown(
        """
        **Funcionalidades:**
        
        - Análise por bairro: Você pode selecionar um bairro específico e obter informações sobre os acidentes nessa área.
        - Análise por ano: Explore os acidentes segmentados por ano, para toda a cidade do Recife.
        """
    )
    
    st.markdown(
        """
        **Sobre a Base de Dados Original:**
        
        - Fonte original: [Dados Recife](http://dados.recife.pe.gov.br/dataset/acidentes-de-transito-com-e-sem-vitimas)
        - Os anos alvo desse trabalho foram 2019 a 2021, pois o ano de 2022 ainda se encontra incompleto para nossa análise.
        - Durante o processamento, dados ausentes das colunas relevantes para o projeto foram removidos.
        - Todo o processo de tratamento e exportação de dados pode ser verificado na pasta "etapa_processamento".
        """
    )
    
    st.markdown(
        """
        **Desenvolvido por:**
        
        Abílio Nogueira
        
        Projeto da disciplina de LAB-1 LC-UFRPE
        """
    )