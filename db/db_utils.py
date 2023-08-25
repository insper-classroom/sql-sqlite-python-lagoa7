import sqlite3

# Setup do Banco de dados
def setup(database):
    conn = sqlite3.connect('database_alunos.db')
    cursor = conn.cursor()
    return conn, cursor

#Reset do Banco
def resetTable(cursor,conn,table):
    cursor.execute(f'DROP TABLE IF EXISTS {table};')
    conn.commit()

# Loading Template
def loadTemplate(cursor,conn,template):
    cursor.executemany("""INSERT INTO Estudantes
     (Nome,Curso,AnoIngresso) VALUES (?,?,?);""", template)
    conn.commit()

# Exibir todos os valores de uma tabela
def showAllfromTABLE(cursor, table):
    cursor.execute(f"SELECT * FROM {table}")
    print(cursor.fetchall())

# Deletar uma linha a partir do ID
def deletebyID(cursor,conn,table,id):
    cursor.execute(f"DELETE FROM {table} WHERE ID = {id}")
    conn.commit()

# Update de Dados da tabela
def updateFromTable(cursor,conn,table,set,setValue,where,whereValue):
    cursor.execute(f"UPDATE {table} SET {set} = {setValue} WHERE {where} = {whereValue}")
    conn.commit()

# Select all from an two or filters
def selectAllOr(cursor, table,where,value1,value2):
    cursor.execute(f"SELECT * FROM {table} WHERE {where} = {value1} or {where} = {value2}")
    print(cursor.fetchall())

# Select all from a specific table where the value is higher Than
def selectSpecificSince(cursor,table,where,whereValue,since,sinceValue):
    cursor.execute(f"SELECT * FROM {table} WHERE {where} = {whereValue} and {since} > {sinceValue}")
    print(cursor.fetchall())