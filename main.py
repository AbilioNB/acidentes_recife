import streamlit as st
from funcoes import *
import pandas as pd
def main():
    st.set_page_config(
        page_title="Acidentes na cidade do Recife",
        page_icon=":pickup_truck:",
        initial_sidebar_state="expanded",
    )

    st.write("# Acidentes na Cidade do Recife  2019-2021")

    
    selecao_demo = st.sidebar.selectbox("Selecione uma opção:", ["Sobre o Projeto", "Análise por Bairro", "Análise por Ano"])
    base_acidentes = pd.read_parquet("base_acidentes_processada")
    if selecao_demo == "Sobre o Projeto":
        pagina_sobre()
    elif selecao_demo == "Análise por Bairro":
        analise_bairro(base_acidentes)
    elif selecao_demo == "Análise por Ano":
        analise_ano(base_acidentes)




if __name__ == "__main__":
    main()
