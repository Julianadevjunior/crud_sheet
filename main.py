import streamlit as st
import os
from functions import style

st.markdown(
    f"""
    <style>
    .stButton > button {{
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        background-color: #4A90E2;
        color: white;
        font-weight: 600;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
        transition: all 0.2s ease-in-out;
    }}
    .stButton > button:hover {{
        background-color: #357ABD;
        transform: scale(1.02);
        cursor: pointer;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Aplica tema e estilos globais
primary_text, secondary_text, background_card, theme_css = style.get_theme_css(st)
st.markdown(theme_css, unsafe_allow_html=True)

# Lista de páginas principais
lista_page = [
    st.Page(page='pages/read.py', title="Tabela"),
    st.Page(page='pages/home.py', title="Home"),
    st.Page(page='pages/login.py', title="Login"),
    st.Page(page='pages/creat.py', title="Criar"),
    st.Page(page='pages/delete.py', title="Deletar"),
    st.Page(page='pages/update.py', title="Atualizar"),
    st.Page(page='pages/menu_gerenciador.py', title="Menu"),
    st.Page(page='pages/imovel.py', title="Imóvel")
]

# Adiciona páginas dinâmicas
for filename in os.listdir("pages/detalhes"):
    if filename.endswith(".py"):
        id_imovel = filename.replace(".py", "")
        lista_page.append(
            st.Page(page=f"pages/detalhes/{filename}", title=f"Imóvel {id_imovel}")
        )


# Cabeçalho + botões dentro do mesmo fundo
header = st.empty()
with header.container():
    st.markdown(
        f"""
        <div style='background-color: #dce6f7; padding: 25px 25px 5px 25px; text-align:center; border-radius: 0px 0px 0 0; margin-bottom: 0;'>
            <h2 style='margin: 0 0 20px; font-size: 28px; color: {primary_text}; font-weight: bold;'>Felipe Carlos Corretor</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.container():
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
        with col1:
            if st.button("Home", use_container_width=True):
                st.switch_page(lista_page[1])
        with col2:
            if st.button("Contatos", use_container_width=True):
                st.switch_page(lista_page[2])
        with col5:
            if st.button("Login", use_container_width=True):
                st.switch_page(lista_page[3])

# Navegação lateral
tela = st.navigation(lista_page, position="sidebar")
tela.run()
