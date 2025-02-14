### Botões do MENU
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from database import select
from datetime import datetime, date


def menu_principal():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Agendar"), KeyboardButton("Visualizar Agendamento"))
    return markup

def datas_disponiveis():
    dia_atual = datetime.now().day
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year
    primeiro_dia = date(ano_atual, mes_atual, 1)

    if(datetime.now().month == 12):
        proximo_mes = date(ano_atual + 1, 1, 1)
    else:
        proximo_mes = date(ano_atual, mes_atual + 1, 1)
    
    dias_no_mes = (proximo_mes - primeiro_dia).days

    lista_dias = []

    for i in range(dias_no_mes):
        if (i + 1) >= dia_atual:
            lista_dias.append( f"{(i + 1):02d}" + "/" + f"{mes_atual:02d}" + "/" + str(ano_atual))
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for dias in lista_dias:
        markup.add(KeyboardButton(dias))
    return markup

def horarios_disponiveis(data_agendamento):
    horarios = select(f'''
        SELECT H."Hora" FROM "Horarios" H
        WHERE NOT EXISTS (
            SELECT A."Id" FROM "Agendamentos" A
            WHERE TO_CHAR(A."Data", 'HH24:MI') = H."Hora"
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