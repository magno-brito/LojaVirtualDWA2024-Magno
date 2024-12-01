SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL)
"""

SQL_INSERIR = """
    INSERT INTO categorias(nome)
    VALUES (?)
"""

SQL_OBTER_TODOS = """
    SELECT id, nome
    FROM categorias
    ORDER BY nome
"""

SQL_ALTERAR = """
    UPDATE categorias
    SET nome=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM categorias
    WHERE id=?
"""

SQL_OBTER_UM = """
    SELECT id, nome
    FROM categorias
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) FROM categorias
"""

SQL_OBTER_BUSCA = """
    SELECT id, nome
    FROM categorias
    WHERE nome LIKE ? 
    ORDER BY #1
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA = """
    SELECT COUNT(*) FROM categorias
    WHERE nome LIKE ? 
"""