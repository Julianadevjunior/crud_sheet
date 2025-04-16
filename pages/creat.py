import streamlit as st
from urllib.parse import unquote
import function
from functions import crud_image, style
from PIL import Image
import requests
from io import BytesIO
import base64
from twilio.rest import Client

col1, col2, col3 = st.columns([2, 2, 2])
with col1:
    st.link_button(label="Whatsapp", url="https://wa.me/+5513974242919/?text=gostaria%20de%20mais%20informacoes", use_container_width=True)
with col2:
    st.link_button(label="Facebook", url="https://www.facebook.com/profile.php?id=100092216181380&locale=pt_BR", use_container_width=True)
with col3:
    st.link_button(label="Instagram", url="https://www.instagram.com/corretorfelipecarlos/reels/", use_container_width=True)

st.markdown(f"""<div style='text-align:center; color:black; font-size:24px;'>Fomulário de contato</div>""", unsafe_allow_html=True)
form_contato = st.form(border=True, clear_on_submit=True, key='form_contato')

# Substitua pelos seus dados da Twilio
account_sid = st.secrets['twillio']['account_sid']
auth_token = st.secrets['twillio']['auth_token']
seu_numero_twilio = st.secrets['twillio']['tel']
numero_destino = "+5513996376382"

client = Client(account_sid, auth_token)

with form_contato:
    nome = st.text_input(label="Nome", key="nome_contato", placeholder="Nome completo")
    telefone = st.text_input(label="Telefone", key="tel_contato", placeholder="Número com DDD")
    email = st.text_input(label="E-mail", key="email_contato", placeholder="E-mail válido")
    texto = st.text_area(label="Mensagem", key="msg_contato", placeholder="Digite sua mensagem")
    mensagem = f"Mensagem do cliente {nome}, com o telefone {telefone}, e-mail {email}, texto {texto}"
    if st.form_submit_button("Enviar"):
        try:
            message = client.messages.create(
                body=mensagem,
                from_=seu_numero_twilio,
                to=numero_destino,
            )
            st.success("Mensagem enviada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao enviar mensagem: {e}")