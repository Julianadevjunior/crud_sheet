import gspread
from google.oauth2.service_account import Credentials

# Escopos necessários para acessar o Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Caminho para o arquivo JSON com as credenciais
CREDENTIALS_FILE = 'crud-456119-62e29f1da7be.json'

# ID da planilha do Google Sheets
SPREADSHEET_ID = '1hcCMgIIFenfWaZrGyqG16RudnV47-wiz2rl7U4lkk5Y'

# Nome da planilha dentro do arquivo
WORKSHEET_NAME = 'imovel'

# Autenticação
creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

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