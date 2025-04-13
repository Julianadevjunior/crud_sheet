import gspread
import streamlit as st
import json
from google.oauth2 import service_account
import os
# Escopos necessários para acessar o Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# Pegando as credenciais do secrets do Streamlit
service_account_info = st.secrets["gcp_service_account"]
creds = service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES)

# Autorizando com gspread
client = gspread.authorize(creds)

# ID da planilha do Google Sheets
SPREADSHEET_ID = '1hcCMgIIFenfWaZrGyqG16RudnV47-wiz2rl7U4lkk5Y'
WORKSHEET_NAME = 'imovel'

# Acessar a planilha
sheet = client.open_by_key(SPREADSHEET_ID).worksheet(WORKSHEET_NAME)

# CRUD Operations

# Create (Criar)
def create_row(row_data):
    sheet.append_row(row_data)

# Read (Ler)
def read_data():
    return sheet.get_all_records()

# Update (Atualizar)
def update_cell(row, col, value):
    sheet.update_cell(row, col, value)

# Delete (Deletar)
def delete_row(row):
    sheet.delete_rows(row)

# # Exemplos de uso
# create_row(['01', 'titulo', 'tipo', 'preco', 'bairro', 'descricao'])
# data = read_data()
# print(data)
# update_cell(2, 2, 'Ap')
# delete_row(3)

def fotos(cod):
    # Criar pasta se não existir
    UPLOAD_FOLDER = f"midias/fotos_{cod}"
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Upload do arquivo
    fotos = st.file_uploader("Fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if st.button("Salvar", key="fotos"):
        # Salvar os arquivos
        if fotos:
            for foto in fotos:
                caminho_arquivo = os.path.join(UPLOAD_FOLDER, foto.name)
                with open(caminho_arquivo, "wb") as f:
                    f.write(foto.getbuffer())
                st.success(f"Arquivo salvo: {foto.name}")


from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

# Autenticação
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)


# Função para upload
def upload_imagem(file_path, nome_arquivo, folder_id):
    file_metadata = {
        'name': nome_arquivo,
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    # Tornar público
    drive_service.permissions().create(
        fileId=file['id'],
        body={'type': 'anyone', 'role': 'reader'}
    ).execute()

    # Link direto da imagem
    return f"https://drive.google.com/uc?id={file['id']}"

def bairros():
    lista = [
        "Anhanguera",
        "Aviação",
        "Balneário Esmeralda",
        "Balneário Flórida",
        "Balneário Maracanã",
        "Balneário Mirim",
        "Balneário Paquetá",
        "Balneário Real",
        "Boqueirão",
        "Caiçara",
        "Canto do Forte",
        "Cidade da Criança",
        "Esmeralda",
        "Canto do Forte",
        "Guilhermina",
        "Ilha das Caieiras",
        "Imperador",
        "Jardim Aloha",
        "Jardim Anchieta",
        "Jardim Aprazível",
        "Jardim Boqueirão",
        "Jardim Caieiras",
        "Jardim Calmarias",
        "Jardim Cavalcante",
        "Jardim Corumbá",
        "Jardim Fátima",
        "Jardim Guaramar",
        "Jardim Imperador",
        "Jardim Imperador IV",
        "Jardim Maracanã",
        "Jardim Melvi",
        "Jardim Mirian",
        "Jardim Princesa",
        "Jardim Quietude",
        "Jardim Real",
        "Jardim Samambaia",
        "Jardim Santa Helena",
        "Jardim São Jorge",
        "Jardim Sônia",
        "Jardim Tupã",
        "Jardim Tupiniquins",
        "Jardim Vicente de Carvalho",
        "Mirim",
        "Nova Mirim",
        "Ocian",
        "Parque das Américas",
        "Quietude",
        "Real",
        "Ribeirópolis",
        "Samambaia",
        "Santa Marina",
        "Sítio do Campo",
        "Solemar",
        "Tupi",
        "Tupiry",
        "Vila Antártica",
        "Vila Assunção",
        "Vila Balneária",
        "Vila Caiçara",
        "Vila Érica",
        "Vila Guilhermina",
        "Vila Harmonia",
        "Vila Isabel",
        "Vila Linda",
        "Vila Magalhães",
        "Vila Mirim",
        "Vila Nova Mirim",
        "Vila Ocean",
        "Vila Sônia",
        "Vila Tupi",
        "Vila Tupiniquins",
        "Vila Verde"
    ]
    return lista

def tipos_imoveis():
    lista = [
    "Casa",
    "Apartamento",
    "Kitnet",
    "Sobrado",
    "Terreno",
    "Loja",
    "Sala comercial",
    "Galpão",
    "Chácara",
    "Sítio",
    "Fazenda",
    "Ponto comercial",
    "Prédio comercial",
    "Lote",
    "Imóvel na planta"
]
    return lista

def bto_voltar(key):
    col1, col2 = st.columns([14.5, 2])
    with col2:
        if st.button("←voltar", key=key):
            st.switch_page(st.Page("pages/menu_gerenciador.py"))