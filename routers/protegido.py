from fastapi import APIRouter, Depends
from app.routers.auth import get_current_user

router = APIRouter()

@router.get("/protegido")
def rota_protegida(user=Depends(get_current_user)):
    return {"mensagem": f"Acesso concedido para {user['preferred_username']}"}
