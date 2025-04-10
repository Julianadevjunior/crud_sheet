import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import function
import pandas as pd


# Tela para editar informações
st.markdown("<p style='color:black; font-size:25px; text-align:center'><b>Atualizar imóveis</b></p>", unsafe_allow_html=True)
dados = function.read_data()
tabela = pd.DataFrame(dados)
cont = st.container(border=True)

# Procurar o código
with cont:
    cod = st.text_input("Inserir código", value=1)
    try:
        cod = int(cod)
    except:
        st.error("Digite o número")
    else:
        try:
            idx = list(tabela['id']).index(cod)
            st.session_state["search_id"] = idx
            # st.write(tabela.loc[idx])
        except:
            st.error('Código não encontrado')

        else:
            # Tela para inserir informações
            form = st.form(key='form_creat', border=True, clear_on_submit=True)

            with form:
                linha = tabela.loc[st.session_state["search_id"]]
                tipo = st.selectbox(label='Tipo', options=[linha[1],"Casa",
                                                    "Apartamento",
                                                    "Cobertura",
                                                    "Terreno",
                                                    "Kitnet",
                                                    "Garden"])

                dono = st.text_input("responsavel", value=linha[2])
                valor = st.text_input("preco", value=linha[3])
                iptu = st.text_input("iptu", value=linha[4])
                cond = st.text_input("condominio", value=linha[5])
                bairro = st.selectbox("bairro", options=[linha[6],"Mirim", "Ocian", "Boqueirão"])
                vaga = st.radio("vaga", options=[linha[7], 1, 2, 3, 4, 5], horizontal=True)
                quarto = st.radio("quarto", options=[linha[8],1, 2, 3, 4, 5], horizontal=True)
                banheiro = st.radio("banheiro", options=[linha[9],1, 2, 3, 4, 5], horizontal=True)
                area = st.text_input("area", value=linha[10])
                cep = st.text_input("cep", value=linha[11])
                descr= st.text_input("descricao", value=linha[12])
                bt = st.form_submit_button("Salvar")

                if bt:
                    st.session_state['form_atualizar'] = [int(linha[0]), tipo, dono, float(valor), float(iptu), float(cond), bairro, int(vaga), int(quarto), int(banheiro), area, cep, descr]
                    for col, titulo in enumerate(st.session_state['form_atualizar']):
                        function.update_cell(idx+2, col+1, titulo)
                    st.success("Atualizado")



