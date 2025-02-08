import psycopg2
from config import DB_CONFIG

def conectar():
    return psycopg2.connect(
        dbname=DB_CONFIG['DATABASE'],
        user=DB_CONFIG['USERNAME'],
        password=DB_CONFIG['PASSWORD'],
        host=DB_CONFIG['HOST'],
        port=DB_CONFIG['PORT']
    )

def salvar_agendamento(nome, telefone, horario, servico, user_id):
    conn = conectar()
    cursor = conn.cursor()
    query = 'INSERT INTO "Agendamentos" ("Nome", "Telefone", "Data", "Servico", "Usuario_Id") VALUES (%s, %s, %s, %s, %s)'
    cursor.execute(query, (nome, telefone, horario, servico, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def buscar_agendamentos(user_id):
    conn = conectar()
    cursor = conn.cursor()
    """ query = "SELECT Nome, Telefone, CONVERT(VARCHAR, Data, 103), CONVERT(VARCHAR(5), Data, 108), Servico FROM Agendamentos WHERE ISNULL(Confirmado, 0) = 0 AND Usuario_Id = ?" """
    query = '''SELECT "Nome", "Telefone", TO_CHAR("Data", 'HH24:MI'), TO_CHAR("Data", 'DD/MM/YYYY'), "Servico" FROM "Agendamentos" WHERE COALESCE("Executado", False) = False AND "Usuario_Id" = %s'''
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
