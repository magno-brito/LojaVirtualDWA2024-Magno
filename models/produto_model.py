from dataclasses import dataclass
from typing import Optional

from models.categoria_model import Categoria


@dataclass
class Produto():
    id: Optional[int] = None
    nome: Optional[str] = None
    preco: Optional[float] = None
    descricao: Optional[str] = None
    estoque: Optional[int] = None
    categoria_id: Optional[Categoria] = None