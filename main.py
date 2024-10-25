from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Produto(BaseModel):
    nome: str
    descricao: str
    preco: float

@app.post("/produtos/")
async def criar_produto(produto: Produto):
    # Aqui você vai usar a API do Gemini para gerar copys e descrições
    # e calcular o preço de venda com base nas regras
    return {"mensagem": "Produto criado com sucesso!"}