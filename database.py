import pyodbc
from config import DB_CONFIG

def conectar():
    return pyodbc.connect(
        f"DRIVER={DB_CONFIG['DRIVER']};"
        f"SERVER={DB_CONFIG['SERVER']};"
        f"DATABASE={DB_CONFIG['DATABASE']};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

def salvar_agendamento(nome, telefone, horario, servico, user_id):
    conn = conectar()
    cursor = conn.cursor()
    query = "INSERT INTO Agendamentos (Nome, Telefone, Data, Servico, Usuario_Id) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (nome, telefone, horario, servico, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def buscar_agendamentos(user_id):
    conn = conectar()
    cursor = conn.cursor()
    query = "SELECT Nome, Telefone, CONVERT(VARCHAR, Data, 103), CONVERT(VARCHAR, Data, 108) FROM Agendamentos WHERE Usuario_Id = ?"
    cursor.execute(query, (user_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def select(query):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
