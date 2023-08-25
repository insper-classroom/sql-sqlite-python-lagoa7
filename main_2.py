import sqlite3
from db.db_utils import *

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn, cursor = setup('db/database_alunos.db')

resetTable(cursor,conn,'estudantes')

# Criando a tabela Estudantes
cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoIngresso INTEGER
);
""")

#Criando um template das informacoes na tabela Estudantes criada anteriormente
template_estudantes = [
    ("Ana Silva","Computação", 2019),
    ("Pedro Mendes","Física", 2021),
    ("Carla Souza","Computação", 2020),
    ("João Alves","Matemática", 2018),
    ("Maria Oliveira","Química", 2022),
]

# Adicionando o template criado anteriormente na tabela Estudantes
loadTemplate(cursor,conn,template_estudantes)

print('')
print('------------------ SELECTING SPECIFIC VALUES --------------------')
print('')
# Selecionando Valores
selectAllOr(cursor,'Estudantes','AnoIngresso',2019, 2020)

print('')
print('------------------ UPDATING VALUES ---------------')
print('')
# Atualizando Valores
updateFromTable(cursor,conn,'Estudantes','AnoIngresso',2020,'ID',2)
showAllfromTABLE(cursor,'Estudantes')

print('')
print('------------------ DELETING VALUES --------------------')
print('')
# Deletando da Base de Dados pelo ID
deletebyID(cursor,conn,'Estudantes',1)
showAllfromTABLE(cursor,'Estudantes')

print('')
print('------------------ SELECTING SPECIFIC VALUES --------------')
print('')
# Selecionando Valores
selectSpecificSince(cursor,"Estudantes","Curso","'Computação'","AnoIngresso",2019)

print('')
print('------------------ UPDATING VALUES ---------------')
print('')

# Atualizando Valores
updateFromTable(cursor,conn,"Estudantes","AnoIngresso",2018,"Curso","'Computação'")
showAllfromTABLE(cursor,'Estudantes')

