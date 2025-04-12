
import streamlit as st

st.set_page_config(page_title="Imóvel 2", layout="wide")

st.markdown("<h1 style='color:#C7A56E'>Imóvel #2</h1>", unsafe_allow_html=True)
st.markdown("### 🏠 Tipo: Apartamento")
st.markdown("### 📍 Bairro: Ocian")
st.markdown("### 📐 Área útil: 87 m²")
st.markdown("### 💰 Valor: R$ 573,000.00".replace(",", "."))
st.markdown("### 🛏 Quartos: 2  🛁 Banheiros: 1")
st.markdown("### 📝 Descrição:")
st.info("Sem descrição")
