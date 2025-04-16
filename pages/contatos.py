import streamlit as st
import function
from functions import style

primary_text, secondary_text, background_card, theme_css = style.get_theme_css(st)
st.markdown(theme_css, unsafe_allow_html=True)
function.bto_voltar(key="voltar_update")
st.markdown(f"""
<div style="padding: 30px 10px; text-align: center; background-color: #dce6f7; border-radius: 8px; margin-top: 20px;">
  <h2 style="margin-bottom: 10px; color: {primary_text}">✏️ Atualizar Imóvel</h2>
  <p style="color: {secondary_text}; font-size: 18px;">Informe o código, a coluna e o novo valor para atualizar as informações do imóvel.</p>
</div>
""", unsafe_allow_html=True)



colunas = [
    "id",
    "tipo",
    "responsavel",
    "valor",
    "iptu",
    "condominio",
    "bairro",
    "vaga",
    "quarto",
    "banheiro",
    "area",
    "ano",
    "descrição"
]

st.markdown("""<br>""", unsafe_allow_html=True)

cod = st.text_input("Código do imóvel:")
col = st.selectbox("Coluna", options=colunas)
novo_valor = st.text_input("Novo valor:")

if st.button("Atualizar", type="primary"):
    if cod and col and novo_valor:
        dados = function.read_data()
        ids = [str(d["id"]) for d in dados]
        if cod in ids:
            linha = ids.index(cod) + 2
            function.update_cell(linha, colunas.index(col)+1, novo_valor)
            st.success("Imóvel atualizado com sucesso!")
        else:
            st.warning("Código não encontrado.")
    else:
        st.warning("Preencha todos os campos corretamente.")