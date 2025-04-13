import streamlit as st
import function
from functions import style, crud_image
import pandas as pd
import requests
import time

primary_text, secondary_text, background_card, theme_css = style.get_theme_css(st)
st.markdown(theme_css, unsafe_allow_html=True)
function.bto_voltar(key="voltar_creat")
st.markdown(f"""
<div style="padding: 30px 10px; text-align: center; background-color: #dce6f7; border-radius: 8px; margin-top: 20px;">
  <h2 style="margin-bottom: 10px; color: {primary_text}">➕ Adicionar Imóvel</h2>
  <p style="color: {secondary_text}; font-size: 18px;">Preencha os campos abaixo para cadastrar um novo imóvel no sistema.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""<br>""", unsafe_allow_html=True)

# Achar o código unico
tabela = pd.DataFrame(function.read_data())

id_ap = 0

for item in range(0, 1000):
    if item in list(tabela["id"]):
        pass
    else:
        id_ap = item
        break


with st.form("form_add"):
    col1, col2 = st.columns(2)
    with col1:
        tipo = st.selectbox(label="Tipos", options=function.tipos_imoveis())
        responsavel = st.text_input("Responsável")
        valor = st.text_input("Valor")
        iptu = st.text_input("IPTU")
        cond = st.text_input("Condominío")
        bairro = st.selectbox(label="Bairro", options=function.bairros())
    with col2:
        area = st.text_input("Área")
        quarto = st.radio(label="Quartos", options=[1, 2, 3, 4, 5], horizontal=True)
        banheiro = st.radio(label="Banheiros", options=[1, 2, 3, 4, 5], horizontal=True)
        vaga = st.radio(label="Vagas", options=[1, 2, 3, 4, 5], horizontal=True)
        ano = st.text_input("Ano de entrega")
    uploaded_files = st.file_uploader(" Fotos", accept_multiple_files=True, type=["jpg", "jpeg", "png"])
    descricao = st.text_area("Descrição")

    if st.form_submit_button("Enviar"):
        try:
            # Validação de dados
            valor = float(valor)
            ano = int(ano)

            dados = [id_ap, tipo, responsavel, valor, iptu, cond, bairro, vaga, quarto, banheiro, area, ano, descricao]
            function.create_row(dados)

            # Upload de imagens com retentativa e barra de progresso
            def upload_imagem_com_retentativa(nome_arquivo, pasta_drive_id, tentativas=3, intervalo=5):
                """Envia uma imagem com retentativa em caso de erro de tempo limite."""
                for i in range(tentativas):
                    try:
                        url, file_id = crud_image.upload_imagem(nome_arquivo, nome_arquivo, pasta_drive_id)
                        return url, file_id
                    except requests.exceptions.Timeout:
                        st.warning(f"Tempo limite excedido. Tentando novamente ({i+1}/{tentativas})...")
                        time.sleep(5)
                    except Exception as e:
                        st.error(f"Erro ao enviar imagem: {e}")
                        return None, None
                st.error("Falha ao enviar imagem após várias tentativas.")
                return None, None

            def criar_imagem(id_ap, lista_fotos):
                """Cria pasta no Drive e envia as imagens com barra de progresso."""
                pasta_drive_id = crud_image.criar_pasta(str(id_ap), crud_image.FOLDER_ID)

                if lista_fotos:
                    progress_bar = st.progress(0)
                    num_fotos = len(lista_fotos)
                    for i, imagem in enumerate(lista_fotos):
                        nome_arquivo = imagem.name
                        with open(nome_arquivo, "wb") as f:
                            f.write(imagem.getbuffer())

                        upload_imagem_com_retentativa(nome_arquivo, pasta_drive_id)
                        progress_bar.progress((i + 1) / num_fotos)

            criar_imagem(id_ap, uploaded_files)
            st.success("Cadastrado com sucesso")

        except ValueError:
            st.error("Erro: Verifique se os campos numéricos estão corretos.")
        except requests.exceptions.Timeout:
            st.error("Erro: Tempo limite excedido ao enviar imagens.")
        except Exception as e:
            st.error(f"Erro no cadastro: {e}")

    st.caption("⚠️ Certifique-se de preencher todos os campos corretamente para evitar erros de cadastro.")
