import sqlite3
from db.db_utils import *

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"



conn = sqlite3.connect('database_alunos.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS estudantes;')
conn.commit()

# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoIngresso INTEGER
);
""")

#Criando um template das informacoes na tabela Estudantes criada anteriormente

estudantes = [
    ("Ana Silva", "Computação", 2019),
    ("Pedro Mendes", "Física", 2021),
    ("Carla Souza", "Computação", 2020),
    ("João Alves", "Matemática", 2018),
    ("Maria Oliveira", "Química", 2022),
]

# Adicionando o template criado anteriormente na tabela Estudantes

cursor.executemany("""
INSERT INTO Estudantes (Nome, Curso, AnoIngresso)
VALUES (?, ?, ?);
""", estudantes)

# Sempre apos fazer alterações no banco de dados é nescessario dar este comando:
conn.commit()

print('')
print('------------------ SELECTING SPECIFIC VALUES --------------------')
print('')

# Executando um comando SQL
cursor.execute("SELECT * FROM Estudantes WHERE AnoIngresso = 2019 or AnoIngresso = 2020")

# Se usa este codigo para demontrar itens da Base de Dados
print(cursor.fetchall())

print('')
print('------------------ UPDATING VALUES ---------------')
print('')

# Atualizando Valores
cursor.execute("UPDATE Estudantes SET AnoIngresso = ? WHERE ID = ? ", (2020, 2))
conn.commit()

cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())

print('')
print('------------------ DELETING VALUES --------------------')
print('')

# Deletando Valores
cursor.execute("DELETE FROM Estudantes WHERE ID = ?", '2')
conn.commit()

cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())

print('')
print('------------------ SELECTING SPECIFIC VALUES --------------')
print('')

cursor.execute("SELECT * FROM Estudantes WHERE Curso = ? and AnoIngresso > ?",('Computação', 2019))
print(cursor.fetchall())

print('')
print('------------------ UPDATING VALUES ---------------')
print('')

# Atualizando Valores
cursor.execute("UPDATE Estudantes SET AnoIngresso = ? WHERE Curso = ? ", (2018, 'Computação'))
conn.commit()

cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())

