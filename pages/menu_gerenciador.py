import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import function
from functions import style

primary_text, secondary_text, background_card, theme_css = style.get_theme_css(st)
st.markdown(theme_css, unsafe_allow_html=True)

st.divider()
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    with st.container(border=True):
        st.markdown("<h2 style='text-align:center; font-size:40px'>👍</h2>", unsafe_allow_html=True)
        if st.button("Adicionar", key="bto_add", use_container_width=True):
            st.switch_page(st.Page("pages/creat.py"))

with col2:
    with st.container(border=True):
        st.markdown("<h2 style='text-align:center; font-size:40px'>👎</h2>", unsafe_allow_html=True)
        if st.button("Deletar", key="bto_del", use_container_width=True):
            st.switch_page(st.Page("pages/delete.py"))

with col3:
    with st.container(border=True):
        st.markdown("<h2 style='text-align:center; font-size:40px'>✍️</h2>", unsafe_allow_html=True)
        if st.button("Atualizar", key="bto_uo", use_container_width=True):
            st.switch_page(st.Page("pages/update.py"))