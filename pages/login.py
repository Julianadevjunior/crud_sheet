import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import function

st.markdown("<p style='color:black; font-size:25px; text-align:center'><b>Login</b></p>", unsafe_allow_html=True)

with st.container(border=True):
    email = st.text_input(label="E-mail", placeholder='Digite seu e-mail')
    senha = st.text_input(label="Senha", placeholder='Digite sua senha')


if st.secrets["login"]['email'] == str(email):
    if st.secrets["login"]['senha'] == str(senha):
        st.success("Seja bem vindo")
        st.session_state['login'] = True
    else:
        st.error(f"Senha não inválida!")
else:
    st.error(f"E-mail {email} não cadastrado!")

if st.button("Entrar", key='bto_login', use_container_width=True) and st.session_state['login'] == True:
    st.switch_page("pages/menu_gerenciador.py")