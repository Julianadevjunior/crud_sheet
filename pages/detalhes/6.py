
import streamlit as st

st.set_page_config(page_title="Imóvel 6", layout="wide")

st.markdown("<h1 style='color:#C7A56E'>Imóvel #6</h1>", unsafe_allow_html=True)
st.markdown("### 🏠 Tipo: Cobertura")
st.markdown("### 📍 Bairro: Mirim")
st.markdown("### 📐 Área útil: 95 m²")
st.markdown("### 💰 Valor: R$ 251.00".replace(",", "."))
st.markdown("### 🛏 Quartos: 1  🛁 Banheiros: 1")
st.markdown("### 📝 Descrição:")
st.info("Sem descrição")
