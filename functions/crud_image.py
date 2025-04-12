import streamlit as st
import gspread
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

# -------------------- Configurações iniciais --------------------
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
service_account_info = st.secrets["gcp_service_account"]
creds = service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES)

# Google Sheets
SPREADSHEET_ID = '1hcCMgIIFenfWaZrGyqG16RudnV47-wiz2rl7U4lkk5Y'
WORKSHEET_NAME = 'imovel'
client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID).worksheet(WORKSHEET_NAME)

# Google Drive
FOLDER_ID = '174Wp0K8EVNWckC2J2qRG9Pzf8IPyNw1q'
drive_service = build('drive', 'v3', credentials=creds)

# -------------------- Funções --------------------
def upload_imagem(file_path, nome_arquivo, folder_id):
    file_metadata = {'name': nome_arquivo, 'parents': [folder_id]}
    media = MediaFileUpload(file_path, resumable=True)

    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    # Torna a imagem pública!
    drive_service.permissions().create(
        fileId=file['id'],
        body={'type': 'anyone', 'role': 'reader'},
        supportsAllDrives=True
    ).execute()

    return f"https://drive.google.com/uc?id={file['id']}", file['id']

def listar_imagens(folder_id):
    results = drive_service.files().list(
        q=f"'{folder_id}' in parents and mimeType contains 'image/' and trashed = false",
        fields="files(id, name, webContentLink, webViewLink)"
    ).execute()
    return results.get('files', [])

def deletar_imagem(file_id):
    drive_service.files().delete(fileId=file_id).execute()

def substituir_imagem(old_file_id, new_file_path, nome_arquivo, folder_id):
    deletar_imagem(old_file_id)
    return upload_imagem(new_file_path, nome_arquivo, folder_id)

def criar_pasta(nome_pasta, parent_id):
    metadata = {
        'name': nome_pasta,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_id]
    }
    pasta = drive_service.files().create(body=metadata, fields='id').execute()
    return pasta.get('id')

def listar_pastas(parent_folder_id):
    query = f"'{parent_folder_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed = false"
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()
    return results.get('files', [])

