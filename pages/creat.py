import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import function

st.markdown("<p style='color:black; font-size:25px; text-align:center'><b>Cadastrar imóveis</b></p>", unsafe_allow_html=True)

dados = function.read_data()

id_form = 0

lista_id = []
for dado in dados:
    lista_id.append(dado['id'])

for idx in range(0, 1000):
    if idx not in lista_id:
        id_form = idx
        break


# Tela para inserir informações
form = st.form(key='form_creat', border=True, clear_on_submit=True)

with form:
    tipo = st.selectbox(label='Tipo', options=["Casa",
                                        "Apartamento",
                                        "Cobertura",
                                        "Terreno",
                                        "Kitnet",
                                        "Garden"])

    dono = st.text_input("responsavel")
    valor = st.text_input("preco")
    iptu = st.text_input("iptu")
    cond = st.text_input("condominio")
    bairro = st.selectbox("bairro", options=["Mirim", "Ocian", "Boqueirão"])
    vaga = st.radio("vaga", options=[1, 2, 3, 4, 5], horizontal=True)
    quarto = st.radio("quarto", options=[1, 2, 3, 4, 5], horizontal=True)
    banheiro = st.radio("banheiro", options=[1, 2, 3, 4, 5], horizontal=True)
    area = st.text_input("area")
    cep = st.text_input("cep")
    descr= st.text_input("descricao")
    bt = st.form_submit_button("Inserir")

    if tipo != "" and dono != "" and valor != "" and iptu != "" and cond != "" and bairro != ""and vaga != ""and quarto != "" and banheiro != "" and area != "" and cep != "" and descr != "":
        if bt:
            function.create_row([id_form, tipo, dono, float(valor), float(iptu), float(cond), bairro, vaga, quarto, banheiro, area, cep, descr])
            st.success("Cadastrado com sucesso")