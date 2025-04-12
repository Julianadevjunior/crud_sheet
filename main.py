import gspread
from google.oauth2.service_account import Credentials
import os
import streamlit as st

lista_page = [st.Page(page='pages/read.py', title="Tabela"),
              st.Page(page='pages/home.py', title="Home"),
              st.Page(page='pages/login.py', title="Login"),
              st.Page(page='pages/creat.py', title="Criar"),
              st.Page(page='pages/delete.py', title="Deletar"),
              st.Page(page='pages/update.py', title="Atualizar"),
              st.Page(page='pages/menu_gerenciador.py', title="Menu"),
              st.Page(page='pages/imovel.py', title="imovel")]

# Diretório onde estão as páginas individuais
detalhes_dir = "pages/detalhes"

# Adiciona dinamicamente cada arquivo de imóvel
for filename in os.listdir(detalhes_dir):
    if filename.endswith(".py"):
        id_imovel = filename.replace(".py", "")
        lista_page.append(
            st.Page(page=f"{detalhes_dir}/{filename}", title=f"Imóvel {id_imovel}")
        )

col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

with col1:
    if st.button("Home", key='home_key', use_container_width=True):
        st.switch_page(lista_page[0])

with col2:
    if st.button("Contatos", key='contatos_key', use_container_width=True):
        st.switch_page(lista_page[1])

with col5:
    if st.button("Login", key='login_key', use_container_width=True):
        st.switch_page(lista_page[2])


# if st.button("Teste", key='teste_key', use_container_width=True):
#     st.switch_page(lista_page[7])
pg = st.navigation(lista_page, position="sidebar")
pg.run()