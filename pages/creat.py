import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import os
from functions import crud_sheet, crud_image  # Certifique-se que `crud_image` tem `upload_imagem`
from functions import style

primary_text, secondary_text, background_card, theme_css = style.get_theme_css(st)
st.markdown(theme_css, unsafe_allow_html=True)

col1, col2 = st.columns([14.5, 2])

with col2:
    if st.button("←Voltar", key="Voltar_del"):
        st.switch_page(st.Page("pages/menu_gerenciador.py"))

dados = crud_sheet.read_data()

# Gerar novo ID
lista_id = [dado['id'] for dado in dados]
id_form = next(idx for idx in range(1000) if idx not in lista_id)

# Formulário
form = st.form(key='form_creat', border=True, clear_on_submit=True)
with form:
    tipo = st.selectbox('Tipo', ["Casa", "Apartamento", "Cobertura", "Terreno", "Kitnet", "Garden"])
    dono = st.text_input("Responsável")
    valor = st.text_input("Preço")
    iptu = st.text_input("IPTU")
    cond = st.text_input("Condomínio")
    bairro = st.selectbox("Bairro", ["Mirim", "Ocian", "Boqueirão"])
    vaga = st.radio("Vaga", [1, 2, 3, 4, 5], horizontal=True)
    quarto = st.radio("Quarto", [1, 2, 3, 4, 5], horizontal=True)
    banheiro = st.radio("Banheiro", [1, 2, 3, 4, 5], horizontal=True)
    area = st.text_input("Área")
    cep = st.text_input("CEP")
    descr = st.text_input("Descrição")

    uploaded_files = st.file_uploader("📸 Enviar fotos do imóvel", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

    bt = st.form_submit_button("Inserir")

    if bt:
        if all([tipo, dono, valor, iptu, cond, bairro, vaga, quarto, banheiro, area, cep, descr]):
            crud_sheet.create_row([id_form, tipo, dono, float(valor), float(iptu), float(cond),
                                 bairro, vaga, quarto, banheiro, area, cep, descr])
            st.success("Imóvel cadastrado com sucesso!")

            # CRIA PASTA NO DRIVE COM ID DO IMÓVEL
            pasta_drive_id = crud_image.criar_pasta(str(id_form), crud_image.FOLDER_ID)

            if uploaded_files:
                for imagem in uploaded_files:
                    nome_arquivo = imagem.name
                    with open(nome_arquivo, "wb") as f:
                        f.write(imagem.getbuffer())

                    url, file_id = crud_image.upload_imagem(nome_arquivo, nome_arquivo, pasta_drive_id)
                    st.image(imagem, caption="Imagem enviada com sucesso!", use_column_width=True)
                    st.rerun()

            else:
                st.info("Imóvel cadastrado, mas nenhuma imagem foi enviada.")
        else:
            st.warning("Preencha todos os campos para cadastrar.")
