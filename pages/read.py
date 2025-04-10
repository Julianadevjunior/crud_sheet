import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import function

st.divider()
# Tela para apresentar informações
st.markdown("<p style='color:black; font-size:25px; text-align:center'><b>Dados imóveis</b></p>", unsafe_allow_html=True)

dados = function.read_data()
st.dataframe(function.read_data())








