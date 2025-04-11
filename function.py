import gspread
import streamlit as st
import json
from google.oauth2 import service_account

# Escopos necessários para acessar o Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Pegando as credenciais do secrets do Streamlit
service_account_info = json.loads(st.secrets["gcp_service_account"].to_json())
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