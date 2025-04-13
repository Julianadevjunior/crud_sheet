import streamlit as st
import function
from functions import crud_image, style
from PIL import Image
import requests
from io import BytesIO
import base64

primary_text, secondary_text, background_card, theme_css = style.get_theme_css(st)
st.markdown(theme_css, unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def carregar_dados():
    return function.read_data()

@st.cache_data(show_spinner=False)
def get_image_url(id_imovel):
    subpastas = crud_image.listar_pastas(crud_image.FOLDER_ID)
    pasta = next((p for p in subpastas if p["name"] == id_imovel), None)
    if not pasta:
        return None
    imagens = crud_image.listar_imagens(pasta["id"])
    return f"https://drive.google.com/uc?id={imagens[0]['id']}" if imagens else None

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




st.divider()

dados = carregar_dados()
bairros = sorted(set([d["bairro"] for d in dados if d["bairro"]]))
tipos = sorted(set([d["tipo"] for d in dados if d["tipo"]]))
valores = [d["valor"] for d in dados if isinstance(d["valor"], (int, float))]

with st.sidebar:
    st.markdown(f"""
    <style>
    section[data-testid="stSidebar"] label, .stSelectbox label, .stNumberInput label {{
        color:white;
        font-weight:600;
    }}
    </style>
    """, unsafe_allow_html=True)

    bairro_selecionado = st.selectbox("Filtrar por bairro:", options=["Todos"] + bairros)
    tipo_selecionado = st.selectbox("Filtrar por tipo de imóvel:", options=["Todos"] + tipos)
    quartos_opcao = st.selectbox("Quartos:", ["Todos", 1, 2, 3, 4, 5])
    banheiros_opcao = st.selectbox("Banheiros:", ["Todos", 1, 2, 3, 4, 5])
    valor_min = st.number_input("Valor mínimo (R$):", value=min(valores) if valores else 0, step=10000)
    valor_max = st.number_input("Valor máximo (R$):", value=max(valores) if valores else 1000000, step=10000)

# Aplica filtros
if bairro_selecionado != "Todos":
    dados = [d for d in dados if d["bairro"] == bairro_selecionado]
if tipo_selecionado != "Todos":
    dados = [d for d in dados if d["tipo"] == tipo_selecionado]
if quartos_opcao != "Todos":
    dados = [d for d in dados if d["quarto"] == quartos_opcao]
if banheiros_opcao != "Todos":
    dados = [d for d in dados if d["banheiro"] == banheiros_opcao]

dados = [d for d in dados if isinstance(d["valor"], (int, float)) and valor_min <= d["valor"] <= valor_max]

for i in range(0, len(dados), 3):
    linha = dados[i:i+3]
    colunas = st.columns(3)
    for idx, dado in enumerate(linha):
        with colunas[idx]:
            id_imovel = str(dado["id"])
            tipo = dado["tipo"]
            bairro = dado["bairro"]
            valor = dado["valor"]
            quartos = dado["quarto"]
            banheiros = dado["banheiro"]
            area = dado.get("area", "Não informado")

            thumb_url = get_image_url(id_imovel)
            img_base64 = gerar_base64_imagem(thumb_url) if thumb_url else "https://via.placeholder.com/400x280.png?text=Sem+Imagem"
            detalhes_url = f"/imovel?id={id_imovel}"
            whatsapp_url = f"https://wa.me/55SEUNUMERO?text=Olá! Tenho interesse no imóvel de referência {id_imovel}."

            html_card = f"""
            <div style="border-radius:12px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.1); margin-bottom:30px; font-family:Segoe UI, sans-serif; background-color:white;">
                <div style="position:relative;">
                    <img src="{img_base64}" style="width:100%; height:200px; object-fit:cover;">
                    <div style="position:absolute; top:10px; left:10px; background:#000000aa; color:white; padding:4px 8px; font-size:12px; border-radius:4px;">
                        Ref.: {id_imovel}
                    </div>
                    <div style="position:absolute; top:10px; right:10px; background:#D81B60; color:white; padding:4px 8px; font-size:12px; border-radius:4px;">
                        VENDA
                    </div>
                </div>
                <div style="padding:10px; background-color:white;">
                    <p style="margin:0 0 4px 0; font-size:13px; color:{secondary_text};">📍 {bairro}, Praia Grande/SP</p>
                    <h4 style="margin:4px 0; font-size:16px; color:{primary_text};">{tipo} com {quartos} quarto(s) e {banheiros} banheiro(s)</h4>
                    <p style="margin:4px 0; font-size:13px;">📐 Área útil: <strong>{area}m²</strong></p>
                    <p style="margin:8px 0 0 0; font-size:16px; font-weight:bold; color:#2E7D32;">R$ {valor:,.2f}</p>
                    <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center;">
                      <a href="{detalhes_url}" style="text-decoration:none;">
                        <button style="padding:6px 10px; font-size:13px; border:1px solid #ccc; border-radius:6px; background:#f9f9f9; cursor:pointer;">
                            🔍 Ver
                        </button>
                     </a>
                        <a href="{whatsapp_url}" target="_blank" style="text-decoration:none;">
                            <button style="padding:6px 10px; font-size:13px; border:none; border-radius:6px; background:#25D366; color:white; cursor:pointer;">
                                💬 Whats
                            </button>
                        </a>
                    </div>
                </div>
            </div>
            """
            st.markdown(html_card, unsafe_allow_html=True)