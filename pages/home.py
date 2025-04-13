import streamlit as st
import function
import os
from pathlib import Path
import function  # usa sua função real
from slugify import slugify
from functions import style

primary_text, secondary_text, background_card, theme_css = style.get_theme_css(st)
st.markdown(theme_css, unsafe_allow_html=True)

# Carrega os dados dos imóveis
dados = function.read_data()

# Pasta de destino
pages_dir = Path("pages/detalhes")
pages_dir.mkdir(parents=True, exist_ok=True)

# Gera uma página para cada imóvel
for imovel in dados:
    id_imovel = imovel["id"]
    tipo = imovel["tipo"]
    bairro = imovel["bairro"]
    valor = imovel["valor"]
    quartos = imovel["quarto"]
    banheiros = imovel["banheiro"]
    area = imovel.get("area", "Não informado")
    descr = imovel.get("descricao", "Sem descrição")

    filename = pages_dir / f"{id_imovel}.py"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""
import streamlit as st

st.set_page_config(page_title="Imóvel {id_imovel}", layout="wide")

st.markdown("<h1 style='color:#C7A56E'>Imóvel #{id_imovel}</h1>", unsafe_allow_html=True)
st.markdown("### 🏠 Tipo: {tipo}")
st.markdown("### 📍 Bairro: {bairro}")
st.markdown("### 📐 Área útil: {area} m²")
st.markdown("### 💰 Valor: R$ {valor:,.2f}".replace(",", "."))
st.markdown("### 🛏 Quartos: {quartos}  🛁 Banheiros: {banheiros}")
st.markdown("### 📝 Descrição:")
st.info("{descr}")
""")

