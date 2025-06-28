from keycloak import KeycloakOpenID
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# Configuração do Keycloak
KEYCLOAK_URL = "http://localhost:8080/auth/"
REALM_NAME = "lar-idosos"
CLIENT_ID = "lar-idosos-api"
CLIENT_SECRET = "sua-chave-secreta"

keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_URL,
    client_id=CLIENT_ID,
    realm_name=REALM_NAME,
    client_secret_key=CLIENT_SECRET
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        user_info = keycloak_openid.userinfo(token)
        return user_info
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado"
        )
