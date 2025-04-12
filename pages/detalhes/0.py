
import streamlit as st

st.set_page_config(page_title="Imóvel 0", layout="wide")

st.markdown("<h1 style='color:#C7A56E'>Imóvel #0</h1>", unsafe_allow_html=True)
st.markdown("### 🏠 Tipo: Kitnet")
st.markdown("### 📍 Bairro: Ocian")
st.markdown("### 📐 Área útil: 85 m²")
st.markdown("### 💰 Valor: R$ 845,000.00".replace(",", "."))
st.markdown("### 🛏 Quartos: 1  🛁 Banheiros: 1")
st.markdown("### 📝 Descrição:")
st.info("Sem descrição")
