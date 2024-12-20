SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco FLOAT NOT NULL,
        descricao TEXT NOT NULL,
        estoque INTEGER NOT NULL,
        categoria_id INTEGER NOT NULL,
        FOREIGN KEY (categoria_id) REFERENCES categoria(id))
"""

SQL_INSERIR = """
    INSERT INTO produto(nome, preco, descricao, estoque, categoria_id)
    VALUES (?, ?, ?, ?, ?)
"""

SQL_OBTER_TODOS = """
    SELECT produto.id, produto.nome, produto.preco, produto.descricao, produto.estoque, categorias.nome AS categoria_nome
    FROM produto
    JOIN categorias ON produto.categoria_id = categorias.id
    ORDER BY produto.nome
"""


SQL_ALTERAR = """
    UPDATE produto
    SET produto.nome=?, produto.preco=?, protudo.descricao=?, produto.estoque=?, produto.categoria_id=?
    WHERE produto.id=?
"""

SQL_EXCLUIR = """
    DELETE FROM produto    
    WHERE produto.id=?
"""

SQL_OBTER_UM = """
    SELECT produto.id, produto.nome, produto.preco, produto.descricao, produto.estoque, categorias.nome AS categoria_nome
    FROM produto
    JOIN categorias ON produto.categoria_id = categorias.id
    WHERE produto.id=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) FROM produto
"""

SQL_OBTER_BUSCA = """
    SELECT produto.id, produto.nome, produto.preco, produto.descricao, produto.estoque, produto.categoria_id
    FROM produto
    JOIN categorias ON produto.categoria_id = categorias.id
    WHERE produto.nome LIKE ? OR descricao LIKE ?
    ORDER BY produto.nome
    LIMIT ? OFFSET ?
"""

SQL_OBTER_POR_CATEGORIA = """
    SELECT produto.id, produto.nome, produto.preco, produto.descricao, produto.estoque, categorias.nome AS categoria_nome
    FROM produto
    JOIN categorias ON produto.categoria_id = categorias.id
    WHERE produto.categoria_id = ?
    ORDER BY produto.nome
    LIMIT ? OFFSET ?
"""


SQL_OBTER_QUANTIDADE_BUSCA = """
    SELECT COUNT(*) FROM produto
    WHERE produto.nome LIKE ? OR descricao LIKE ?
"""

