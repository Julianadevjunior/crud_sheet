
import streamlit as st

st.set_page_config(page_title="Imóvel 3", layout="wide")

st.markdown("<h1 style='color:#C7A56E'>Imóvel #3</h1>", unsafe_allow_html=True)
st.markdown("### 🏠 Tipo: Kitnet")
st.markdown("### 📍 Bairro: Ocian")
st.markdown("### 📐 Área útil: 80 m²")
st.markdown("### 💰 Valor: R$ 678.00".replace(",", "."))
st.markdown("### 🛏 Quartos: 2  🛁 Banheiros: 1")
st.markdown("### 📝 Descrição:")
st.info("Sem descrição")
