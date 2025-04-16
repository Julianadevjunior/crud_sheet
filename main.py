import streamlit as st
import os
from functions import style



# Aplica tema e estilos globais
primary_text, secondary_text, background_card, theme_css = style.get_theme_css(st)
st.markdown(theme_css, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([1.5, 1.5, 5, 1.5])

with col1:
    if st.button("Home", key='bto_1', use_container_width=True):
        st.switch_page(st.Page("pages/read.py"))
with col2:
    if st.button("Contato", key='bto_2', use_container_width=True):
        st.switch_page(st.Page("pages/contatos.py"))
with col4:
    if st.button("Corretor", key='bto_3', use_container_width=True):
        st.switch_page(st.Page("pages/login.py"))

# Lista de páginas principais
lista_page = [
    st.Page(page='pages/read.py', title="Tabela"),
    st.Page(page='pages/home.py', title="Home"),
    st.Page(page='pages/login.py', title="Login"),
    st.Page(page='pages/creat.py', title="Criar"),
    st.Page(page='pages/delete.py', title="Deletar"),
    st.Page(page='pages/update.py', title="Atualizar"),
    st.Page(page='pages/menu_gerenciador.py', title="Menu"),
    st.Page(page='pages/imovel.py', title="Imóvel"),
    st.Page(page='pages/contatos.py', title="Contatos")
]

# streamlit run main.py


# Navegação lateral
tela = st.navigation(lista_page, position="hidden")
tela.run()