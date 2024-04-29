from dotenv import load_dotenv
import os

load_dotenv(r'simulados\src\.env')

CONTRA_SENHA = os.getenv('CONTRA_SENHA')
CHAVE_FERNET = os.getenv('CHAVE_FERNET')
SEGREDO_CRIPTO = os.getenv('SEGREDO_CRIPTO')
