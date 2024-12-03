import asyncio
from typing import List
from fastapi import APIRouter, Request

from dtos.novo_produto_dto import NovoProdutoDTO
from models.usuario_model import Usuario
from repositories.categoria_repo import CategoriaRepo
from repositories.produto_repo import ProdutoRepo
from repositories.usuario_repo import UsuarioRepo


SLEEP_TIME = 0.2
router = APIRouter(prefix="/admin")


@router.get("/obter_usuarios")
async def obter_usuarios() -> List[Usuario]:
    await asyncio.sleep(SLEEP_TIME)
    usuarios = UsuarioRepo.obter_todos()
    return usuarios

@router.get("/obter_produtos")
async def obter_produtos():
    produtos = ProdutoRepo.obter_todos()
    return produtos



@router.get("/obter_um/{id:int}")
async def obter_um(request: Request, id: int):
    produto = ProdutoRepo.obter_um(id)
    return produto

@router.get("/obter_todos")
async def obter_todos():
    produtos = ProdutoRepo.obter_todos()
    return produtos

@router.post("/inserir_produto")
async def inserir_produto(produto: NovoProdutoDTO):
    pass

@router.get("/obter_categorias")
async def obter_categorias():
    categorias = CategoriaRepo.obter_todos()
    return categorias

