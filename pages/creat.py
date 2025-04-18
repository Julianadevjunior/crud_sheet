import streamlit as st
import function
from functions import style, crud_image
import pandas as pd
import requests
import time

# Estilos do tema
primary_text, secondary_text, background_card, theme_css = style.get_theme_css(st)
st.markdown(theme_css, unsafe_allow_html=True)

# Botão voltar
function.bto_voltar(key="voltar_creat")

# Cabeçalho
st.markdown(f"""
<div style="padding: 30px 10px; text-align: center; background-color: #dce6f7; border-radius: 8px; margin-top: 20px;">
  <h2 style="margin-bottom: 10px; color: {primary_text}">➕ Adicionar Imóvel</h2>
  <p style="color: {secondary_text}; font-size: 18px;">Preencha os campos abaixo para cadastrar um novo imóvel no sistema.</p>
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Botão para limpar o cache e recarregar
if st.button("🔄 Recarregar dados (limpar cache)"):
    st.cache_data.clear()
    st.experimental_rerun()

# Função cacheada para carregar a planilha
@st.cache_data
def get_tabela():
    return pd.DataFrame(function.read_data())

tabela = get_tabela()

# Achar o próximo ID disponível
id_ap = 0
for item in range(0, 1000):
    if item in list(tabela["id"]):
        continue
    id_ap = item
    break

# Formulário
with st.form("form_add"):
    col1, col2 = st.columns(2)
    with col1:
        tipo = st.selectbox("Tipos", options=function.tipos_imoveis())
        responsavel = st.text_input("Responsável")
        residencial = st.text_input("Residencial")
        telefone = st.text_input("Telefone")
        valor = st.text_input("Valor")
        iptu = st.text_input("IPTU")
        cond = st.text_input("Condominío")
    with col2:
        bairro = st.selectbox("Bairro", options=function.bairros())
        area = st.text_input("Área")
        quarto = st.radio("Quartos", options=[1, 2, 3, 4, 5], horizontal=True)
        banheiro = st.radio("Banheiros", options=[1, 2, 3, 4, 5], horizontal=True)
        vaga = st.radio("Vagas", options=[1, 2, 3, 4, 5], horizontal=True)
        ano = st.date_input("Ano de entrega", format="DD/MM/YYYY")
        ano = ano.strftime("%d/%m/%Y")  # 🔄 converte para string no formato brasileiro
    uploaded_files = st.file_uploader(" Fotos", accept_multiple_files=True, type=["jpg", "jpeg", "png"])
    descricao = st.text_area("Descrição")

    if st.form_submit_button("Enviar"):
        try:
            # Validação e conversão
            valor = function.corretor_number(valor, "Valor")
            iptu = function.corretor_number(iptu, "Iptu")
            cond = function.corretor_number(cond, "Cond")
            area = function.corretor_number(area, "Area")

            dados = [id_ap, tipo, telefone, responsavel, residencial, valor, iptu, cond, bairro, vaga, quarto, banheiro,
                     area, ano, descricao]
            function.create_row(dados)
            st.cache_data.clear()  # limpa cache após criar

            # Upload das imagens com barra de progresso
            def upload_imagem_com_retentativa(nome_arquivo, pasta_drive_id, tentativas=3, intervalo=5):
                for i in range(tentativas):
                    try:
                        url, file_id = crud_image.upload_imagem(nome_arquivo, nome_arquivo, pasta_drive_id)
                        return url, file_id
                    except requests.exceptions.Timeout:
                        st.warning(f"Tentando novamente ({i+1}/{tentativas})...")
                        time.sleep(intervalo)
                    except Exception as e:
                        st.error(f"Erro: {e}")
                        return None, None
                st.error("Falha após várias tentativas.")
                return None, None

            def criar_imagem(id_ap, lista_fotos):
                pasta_drive_id = crud_image.criar_pasta(str(id_ap), crud_image.FOLDER_ID)
                if lista_fotos:
                    progress_bar = st.progress(0)
                    for i, imagem in enumerate(lista_fotos):
                        nome_arquivo = imagem.name
                        with open(nome_arquivo, "wb") as f:
                            f.write(imagem.getbuffer())
                        upload_imagem_com_retentativa(nome_arquivo, pasta_drive_id)
                        progress_bar.progress((i + 1) / len(lista_fotos))

            criar_imagem(id_ap, uploaded_files)
            st.success("✅ Imóvel cadastrado com sucesso!")

        except ValueError:
            st.error("❌ Verifique os campos numéricos.")
        except requests.exceptions.Timeout:
            st.error("⏱️ Tempo limite excedido.")
        except Exception as e:
            st.error(f"❌ Erro inesperado: {e}")

    st.caption("⚠️ Certifique-se de preencher todos os campos corretamente para evitar erros.")
