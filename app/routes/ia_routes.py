from fastapi import APIRouter
from app.services.ia_service import gerar_mensagem

router = APIRouter()

@router.get("/mensagem/{id_usuario}")
def obter_mensagem(id_usuario: int):
    mensagem = gerar_mensagem(id_usuario)
    return {"id_usuario": id_usuario, "mensagem": mensagem}