import streamlit as st

from urllib.parse import unquote
import function
from functions import crud_image
from PIL import Image
import requests
from io import BytesIO
import base64

@st.cache_data(show_spinner=False)
def gerar_base64_imagem(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content)).convert("RGB")
        buffer = BytesIO()
        image.save(buffer, format="JPEG", optimize=True, quality=60)
        base64_img = base64.b64encode(buffer.getvalue()).decode()
        return f"data:image/jpeg;base64,{base64_img}"
    except Exception:
        return "https://via.placeholder.com/400x280.png?text=Erro+Imagem"

query_params = st.query_params
id_imovel = query_params.get("id", [None])[0]

if not id_imovel:
    st.error("ID do imóvel não informado na URL.")
    st.stop()

@st.cache_data(show_spinner=False)
def buscar_dados(id_busca):
    dados = function.read_data()
    return next((d for d in dados if str(d["id"]) == str(id_busca)), None)

imovel = buscar_dados(id_imovel)

if not imovel:
    st.error("Imóvel não encontrado.")
    st.stop()

st.markdown(f"""
<div style='margin-bottom:20px;'>
  <p style='font-size:14px; color:#888;'>Venda / Praia Grande / {imovel['bairro']} / <strong style='color:black;'>{imovel['tipo']} com {imovel['quarto']} Quartos</strong></p>
</div>
<div style='display:flex; flex-wrap:wrap; gap:40px; align-items:center; margin-bottom:20px;'>
  <div>
    <h1 style='margin:0; font-size:32px; color:#1a1a1a;'>R$ {imovel['valor']:,.2f}</h1>
    <p style='margin:4px 0 0; color:#555;'>Venda</p>
  </div>
  <div>
    <p style='margin:0; font-weight:bold;'>Condomínio</p>
    <p style='margin:0; color:#555;'>R$ {imovel['condominio']:,.2f}</p>
  </div>
  <div>
    <p style='margin:0; font-weight:bold;'>IPTU</p>
    <p style='margin:0; color:#555;'>R$ {imovel['iptu']:,.2f}</p>
  </div>
</div>
<div style='display:flex; flex-wrap:wrap; gap:30px; font-size:16px; color:#333; margin-bottom:30px;'>
  <span>📏 {imovel['area']} m²</span>
  <span>🛏 {imovel['quarto']} quarto(s)</span>
  <span>🛁 {imovel['banheiro']} banheiro(s)</span>
  <span>🚗 {imovel.get('vaga', 0)} vaga(s)</span>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="background-color:#f7f7f7; padding:25px 30px; border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:30px;">
  <h4 style="margin-bottom:10px;">Endereço</h4>
  <p style="margin:0; font-weight:bold;">{imovel.get('endereco', 'Endereço não informado')} - {imovel['bairro']}, Praia Grande - SP</p>
  <br>
  <h4 style="margin-bottom:10px;">Descrição</h4>
  <p style="margin:0;">{imovel.get('descricao', 'Sem descrição')}</p>
</div>
""", unsafe_allow_html=True)

subpastas = crud_image.listar_pastas(crud_image.FOLDER_ID)
pasta = next((p for p in subpastas if p["name"] == str(imovel["id"])), None)
if pasta:
    imagens = crud_image.listar_imagens(pasta["id"])
    if imagens:
        st.markdown("<h3 style='margin-top:30px;'>📷 Galeria de Imagens</h3>", unsafe_allow_html=True)
        for i in range(0, len(imagens), 3):
            linha = [img for img in imagens[i:i+3] if img is not None]
            colunas = st.columns(3)
            for idx, imagem in enumerate(linha):
                if imagem is None:
                    continue
                url = f"https://drive.google.com/uc?id={imagem['id']}"
                base64_img = gerar_base64_imagem(url)
                with colunas[idx]:
                    st.markdown(f'<img src="{base64_img}" alt="Imagem" style="width:100%; border-radius:12px; margin-bottom:15px">', unsafe_allow_html=True)
    else:
        st.warning("Nenhuma imagem encontrada na pasta do imóvel.")
else:
    st.warning("Pasta do imóvel não encontrada.")

st.markdown("---")
st.markdown(f"🔗 Link desta página: [Clique aqui](?id={id_imovel}) ou copie o link da URL para compartilhar.")
