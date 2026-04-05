from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
import os

API_KEY_NAME = "X-API-Key"
SECRET_API_KEY = os.getenv("EGIDE_API_KEY", "chave_secreta_egide")
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def verificar_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == SECRET_API_KEY:
        return api_key_header
    
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Acesso negado. Chave de API inválida ou ausente."
    )