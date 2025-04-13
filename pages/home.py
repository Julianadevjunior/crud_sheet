import streamlit as st
import function
from pathlib import Path
from functions import style

primary_text, secondary_text, background_card, theme_css = style.get_theme_css(st)
st.markdown(theme_css, unsafe_allow_html=True)

# Carrega os dados dos imóveis
dados = function.read_data()

# Gera páginas de imóvel no diretório "pages/detalhes" (por compatibilidade temporária)
pages_dir = Path("pages/detalhes")
pages_dir.mkdir(parents=True, exist_ok=True)

for imovel in dados:
    id_imovel = imovel.get("id")
    tipo = imovel.get("tipo", "")
    bairro = imovel.get("bairro", "")
    valor = imovel.get("valor", 0)
    quartos = imovel.get("quarto", 0)
    banheiros = imovel.get("banheiro", 0)
    area = imovel.get("area", "Não informado")
    descr = imovel.get("descricao", "Sem descrição")

    filename = pages_dir / f"{id_imovel}.py"
    if not filename.exists():
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

# Mensagem visual na home
st.markdown(f"""
<div style="padding: 30px 10px; text-align: center; background-color: #dce6f7; border-radius: 8px; margin-top: 20px;">
  <h2 style="margin-bottom: 10px; color: {primary_text};">🏡 Bem-vindo ao sistema de imóveis</h2>
  <p style="color: {secondary_text}; font-size: 18px;">Gerencie seus imóveis com agilidade, edite, visualize e compartilhe com seus clientes de forma simples.</p>
</div>
""", unsafe_allow_html=True)