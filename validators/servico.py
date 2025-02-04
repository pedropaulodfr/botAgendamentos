from database import select
from datetime import datetime

# Verifica se o usuário já possui o serviço agendado para essa data
def verificar_servico(servico, data_agendamento, user_id):
    servicos = select(f'''
        SELECT A.* FROM Agendamentos A
        JOIN Servicos S ON A.Servico = S.Identificacao
        WHERE S.Identificacao = '{servico}'
        AND CONVERT(VARCHAR, A.DATA, 103) = '{data_agendamento}'
        AND ISNULL(A.Confirmado, 0) = 0
        AND Usuario_Id = {user_id}
    ''')
    
    if servicos:
        return True
    else:
        return False
    