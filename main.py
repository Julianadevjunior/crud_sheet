import gspread
from google.oauth2.service_account import Credentials
import streamlit as st

if "search_id" not in st.session_state:
    st.session_state['search_id'] = 0

if "form_atualizar" not in st.session_state:
    st.session_state['form_atualizar'] = []

if "login" not in st.session_state:
    st.session_state['login'] = False


if st.session_state['login'] == True:
    col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])

    with col1:
        if st.button("Home", key="home", use_container_width=True):
            st.switch_page("pages/read.py")

    with col2:
        if st.button("Adicionar", key="bto_adicionar", use_container_width=True):
            st.switch_page("pages/creat.py")

    with col3:
        if st.button("Deletar", key="delete", use_container_width=True):
            st.switch_page("pages/delete.py")

    with col4:
        if st.button("Atualizar", key="update", use_container_width=True):
            st.switch_page("pages/update.py")

    with col5:
        if st.button("Sair", key="voltar", use_container_width=True):
            st.session_state['login'] = False
            st.switch_page("pages/login.py")

lista_page = [st.Page(page='pages/login.py', title="Login"),
              st.Page(page='pages/read.py', title="Tabela"),
              st.Page(page='pages/creat.py', title="Criar"),
              st.Page(page='pages/delete.py', title="Deletar"),
              st.Page(page='pages/update.py', title="Atualizar")]

pg = st.navigation(lista_page, position="hidden")
pg.run()
