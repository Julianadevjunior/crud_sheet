import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import function
import pandas as pd

# Tela para excluir informações

dados = function.read_data()
tabela = pd.DataFrame(dados)

# verificar se tem o cod

# qual linha está o código

# Confirmar exclusão

st.markdown("<p style='color:black; font-size:25px; text-align:center'><b>Excluir imóveis</b></p>", unsafe_allow_html=True)

cont = st.container(border=True)

with cont:
    cod = st.text_input("Inserir código", value=1)
    try:
        cod = int(cod)
    except:
        st.error("Digite o número")
    else:
        try:
            idx = list(tabela['id']).index(cod)
        except:
            st.error('Código não encontrado')
        else:
            linha = 2 + idx
            if st.checkbox(label='Confirmar', key="confirmar"):
                if st.button("Excluir", key="bto_excluir"):
                    function.delete_row(linha)
                    st.success("Excluido com sucesso")



