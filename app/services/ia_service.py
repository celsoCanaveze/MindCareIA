import json
from app.utils.generator import gerar_resposta

def gerar_mensagem(id_usuario: int):
    with open("app/data/mindcare_dataset.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    usuario = next((u for u in dados["usuarios"] if u["id"] == id_usuario), None)
    if not usuario:
        return "Usuário não encontrado no dataset."

    humor = usuario.get("humor", 5)
    return gerar_resposta(humor)