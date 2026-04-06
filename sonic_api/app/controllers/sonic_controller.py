from app.database import collection
from bson import ObjectId

def listar_jogos():
    jogos = []
    for jogo in collection.find():
        jogo["_id"] = str(jogo["_id"])
        jogos.append(jogo)
    return jogos

def criar_jogo(dado):
    result = collection.insert_one(dado)
    return {"id": str(result.inserted_id)}

def buscar_jogo(id):
    try:
        obj_id = ObjectId(id)
    except Exception:
        return {"erro": "ID inválido"}

    jogo = collection.find_one({"_id": obj_id})
    if jogo:
        jogo["_id"] = str(jogo["_id"])
    return jogo

def atualizar_jogo(id, dado):
    try:
        obj_id = ObjectId(id)
    except Exception:
        return {"erro": "ID inválido"}

    result = collection.update_one({"_id": obj_id}, {"$set": dado})

    if result.matched_count == 1:
        return {"msg": "Atualizado com sucesso"}
    else:
        return {"erro": "Jogo não encontrado"}

def deletar_jogo(id):
    try:
        obj_id = ObjectId(id)
    except Exception:
        return {"erro": "ID inválido"}

    result = collection.delete_one({"_id": obj_id})

    if result.deleted_count == 1:
        return {"msg": "Deletado com sucesso"}
    else:
        return {"erro": "Jogo não encontrado"}