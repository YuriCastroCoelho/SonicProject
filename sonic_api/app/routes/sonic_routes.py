from fastapi import APIRouter
from app.schemas.sonic_schema import SonicGame
from app.controllers import sonic_controller

router = APIRouter()

@router.get("/jogos")
def get_jogos():
    return sonic_controller.listar_jogos()

@router.post("/jogos")
def post_jogo(jogo: SonicGame):
    return sonic_controller.criar_jogo(jogo.dict())

@router.put("/jogos/{id}")
def put_jogo(id: str, jogo: SonicGame):
    return sonic_controller.atualizar_jogo(id, jogo.dict())

@router.delete("/jogos/{id}")
def delete_jogo(id: str):
    return sonic_controller.deletar_jogo(id)