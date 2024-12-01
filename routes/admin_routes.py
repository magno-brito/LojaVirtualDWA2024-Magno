from fastapi import APIRouter, Request

from dtos.novo_produto_dto import NovoProdutoDTO
from repositories.categoria_repo import CategoriaRepo
from repositories.produto_repo import ProdutoRepo


router = APIRouter(prefix="/manager")


@router.get("/obter_produtos")
async def obter_produtos():
    produtos = ProdutoRepo.obter_todos()
    return produtos

@router.get("/obter_um/{id:int}")
async def obter_um(request: Request, id: int):
    produto = ProdutoRepo.obter_um(id)
    return produto

@router.post("/inserir_produto")
async def inserir_produto(produto: NovoProdutoDTO):
    pass

@router.get("/obter_categorias")
async def obter_categorias():
    categorias = CategoriaRepo.obter_todos()
    return categorias