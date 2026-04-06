from pydantic import BaseModel

class SonicGame(BaseModel):
    nome: str
    plataforma: str
    ano_lancamento: int
    emulador: str