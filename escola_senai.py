<<<<<<< HEAD
import sqlite3

# CONEXÃO COM BANCO DE DADOS
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

# CRIANDO A TABELA COM O CAMPO ID
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               nota INTEGER
               )
               """)

# LIMPAR A TABELA ANTES DE INSERIR (evita duplicação)
cursor.execute("DELETE FROM alunos")  # ← NOVO: remove todos os dados antigos

# INSERINDO MAIS DADOS DE EXEMPLO (ADICIONADAS AS VÍRGULAS)
dados = [
    ('Ana', 8), # ← faltava vírgula
    ('Diego', 5),
    ('Luiz Felipe', 9),
    ('Aleks', 8),
    ('Charles', 7),
    ('Patricia', 8),
    ('Herbert', 9)   # ← último não precisa de vírgula
]

# FUNÇÃO INSERT
cursor.executemany("INSERT INTO alunos (nome, nota) VALUES (?, ?)", dados)

conn.commit()  # ← adicionado os parênteses

print("=== Dados da Tabela ===\n")
cursor.execute("SELECT * FROM alunos ORDER BY nota DESC")
alunos = cursor.fetchall()

print("\n1. FOR simples - Mostrando nome e nota: ")
for aluno in alunos:
    print(f"{aluno[1]} tirou {aluno[2]}")

# Boa prática: fechar a conexão
conn.close()


=======
import sqlite3

# CONEXÃO COM BANCO DE DADOS
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

# CRIANDO A TABELA COM O CAMPO ID
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               nota INTEGER
               )
               """)

# LIMPAR A TABELA ANTES DE INSERIR (evita duplicação)
cursor.execute("DELETE FROM alunos")  # ← NOVO: remove todos os dados antigos

# INSERINDO MAIS DADOS DE EXEMPLO (ADICIONADAS AS VÍRGULAS)
dados = [
    ('Ana', 8), # ← faltava vírgula
    ('Diego', 5),
    ('Luiz Felipe', 9),
    ('Aleks', 8),
    ('Charles', 7),
    ('Patricia', 8),
    ('Herbert', 9)   # ← último não precisa de vírgula
]

# FUNÇÃO INSERT
cursor.executemany("INSERT INTO alunos (nome, nota) VALUES (?, ?)", dados)

conn.commit()  # ← adicionado os parênteses

print("=== Dados da Tabela ===\n")
cursor.execute("SELECT * FROM alunos ORDER BY nota DESC")
alunos = cursor.fetchall()

print("\n1. FOR simples - Mostrando nome e nota: ")
for aluno in alunos:
    print(f"{aluno[1]} tirou {aluno[2]}")

# Boa prática: fechar a conexão
conn.close()


>>>>>>> d2bd66742168fa7ce420d714a321d36f923db085
