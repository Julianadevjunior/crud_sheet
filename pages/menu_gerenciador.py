import streamlit as st
import function
from functions import style

primary_text, secondary_text, background_card, theme_css = style.get_theme_css(st)
st.markdown(theme_css, unsafe_allow_html=True)

st.markdown("""
<div style="padding: 30px 10px; text-align: center; background-color: #dce6f7; border-radius: 8px; margin-top: 20px;">
  <h2 style="margin-bottom: 10px; color: {}">📊 Menu do Gerenciador</h2>
  <p style="color: {}; font-size: 18px;">Gerencie seus imóveis com facilidade: adicione, exclua ou edite imóveis cadastrados.</p>
</div>
""".format(primary_text, secondary_text), unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    with st.container(border=True):
        st.markdown("<h2 style='text-align:center; font-size:40px'>👍</h2>", unsafe_allow_html=True)
        if st.button("Adicionar", key="bto_add", use_container_width=True):
            st.switch_page(st.Page("pages/creat.py"))

with col2:
    with st.container(border=True):
        st.markdown("<h2 style='text-align:center; font-size:40px'>🗑️</h2>", unsafe_allow_html=True)
        if st.button("Deletar", key="bto_del", use_container_width=True):
            st.switch_page(st.Page("pages/delete.py"))

with col3:
    with st.container(border=True):
        st.markdown("<h2 style='text-align:center; font-size:40px'>✏️</h2>", unsafe_allow_html=True)
        if st.button("Atualizar", key="bto_uo", use_container_width=True):
            st.switch_page(st.Page("pages/update.py"))

col4, col5, col6 = st.columns([1, 1, 1])

with col4:
    with st.container(border=True):
        st.markdown("<h2 style='text-align:center; font-size:40px'>🤝️</h2>", unsafe_allow_html=True)

        st.link_button(label="CRM", url='https://crmsheetsite-6whfhju7ofzsg6vyy5ibx5.streamlit.app/', use_container_width=True)

