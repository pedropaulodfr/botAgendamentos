### Botões do MENU
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from database import select
from datetime import datetime


def menu_principal():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Agendar"), KeyboardButton("Visualizar Agendamento"))
    return markup

def horarios_disponiveis(data_agendamento):
    """ horarios = select(f'''
        SELECT CONVERT(VARCHAR(5), Hora, 108) Hora FROM Horarios H
        WHERE NOT EXISTS (
            SELECT A.Id FROM Agendamentos A
            WHERE CONVERT(VARCHAR(5), A.Data, 108) = CONVERT(VARCHAR(5), H.Hora, 108)
            AND CONVERT(VARCHAR, A.DATA, 103) = '{data_agendamento}'
        ) 
    ''') """
    horarios = select(f'''
        SELECT TO_CHAR(H."Hora", 'HH24:MI') FROM "Horarios" H
        WHERE NOT EXISTS (
            SELECT A."Id" FROM "Agendamentos" A
            WHERE TO_CHAR(A."Data", 'HH24:MI') = TO_CHAR(H."Hora", 'HH24:MI')
            AND TO_CHAR(A."Data", 'DD/MM/YYYY') = '{data_agendamento}'
        )
    ''')
    
    # Verifica se há horários disponíveis
    if not horarios:
        return None
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for horario in horarios:
        markup.add(KeyboardButton(horario[0]))
    return markup

def servicos_disponiveis():
    servicos = select('''SELECT "Identificacao" FROM "Servicos" WHERE COALESCE("Ativo", True) = True''')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for servico in servicos:
        markup.add(KeyboardButton(servico[0]))
    return markup
