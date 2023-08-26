import streamlit as st

def main():
    st.set_page_config(
        page_title="Acidentes na cidade do Recife",
        page_icon=":pickup_truck:",
        initial_sidebar_state="expanded",
    )

    st.write("# Acidentes na Cidade do Recife  2019-2021")

    # Opções do menu lateral
    selecao_demo = st.sidebar.selectbox("Selecione uma opção:", ["Sobre o Projeto", "Análise por Bairro", "Análise por Ano", "Análise Completa"])

    if selecao_demo == "Sobre o Projeto":
        pagina_sobre()
    elif selecao_demo == "Análise por Bairro":
        analise_bairro()
    elif selecao_demo == "Análise por Ano":
        analise_ano()
    elif selecao_demo == "Análise Completa":
        analise_cidade()

def pagina_sobre():
    st.markdown(
        """##### Informações
        
        Bem-vindo ao Dashboard de Análise de Acidentes na Cidade do Recife. 
        Aqui você poderá explorar dados sobre acidentes ocorridos na cidade, 
        segmentados por bairro, ano e visualizar a análise completa da cidade.
        
        **Funcionalidades:**
        - Análise por bairro: Você pode selecionar um bairro específico e obter informações sobre os acidentes nessa área.
        - Análise por ano: Explore os acidentes segmentados por ano, compreendendo as tendências ao longo do tempo.
        - Análise completa da cidade: Visualize a análise abrangente de todos os acidentes na cidade do Recife.
        
        Sinta-se à vontade para explorar os diferentes aspectos dos acidentes na cidade utilizando as opções disponíveis no painel à esquerda.
    """
    )

def analise_bairro():
    st.title("Análise por Bairro")
    # Coloque aqui o código para a análise por bairro

def analise_ano():
    st.title("Análise por Ano")
    # Coloque aqui o código para a análise por ano

def analise_cidade():
    st.title("Análise Completa")
    # Coloque aqui o código para a análise completa da cidade

if __name__ == "__main__":
    main()
