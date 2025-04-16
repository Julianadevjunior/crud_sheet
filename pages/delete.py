import streamlit as st
import function
import functions.crud_image
from functions import style

primary_text, secondary_text, background_card, theme_css = style.get_theme_css(st)
st.markdown(theme_css, unsafe_allow_html=True)
function.bto_voltar(key="voltar_delete")
st.markdown(f"""
<div style="padding: 30px 10px; text-align: center; background-color: #dce6f7; border-radius: 8px; margin-top: 20px;">
  <h2 style="margin-bottom: 10px; color: {primary_text}">🗑️ Excluir Imóvel</h2>
  <p style="color: {secondary_text}; font-size: 18px;">Digite o código do imóvel que deseja remover da base.</p>
</div>
""", unsafe_allow_html=True)

cod = st.text_input("Digite o código do imóvel para deletar:", max_chars=10)

if st.button("Deletar imóvel", type="primary"):
    if cod:
        dados = function.read_data()
        ids = [str(d["id"]) for d in dados]
        if cod in ids:
            linha = ids.index(cod) + 2
            function.delete_row(linha)
            functions.crud_image.deletar_pasta_do_imovel(cod)
            st.success(f"Imóvel código {cod} removido com sucesso.")
        else:
            st.warning(f"Código {cod} não encontrado na base.")
    else:
        st.warning("Por favor, preencha o campo com um código válido.")