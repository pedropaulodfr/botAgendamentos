import telebot
from telebot.types import ForceReply
from keyboards import horarios_disponiveis, servicos_disponiveis
from database import salvar_agendamento, select
from datetime import date, datetime

# LIsta para armazenar os dados do agendamento
dados_agendamento = []

def agendamento_handlers(bot):
    @bot.message_handler(func=lambda message: message.text == "Agendar")
    def agendar(message):
        bot.send_message(message.chat.id, "Digite seu nome:", reply_markup=ForceReply())

    @bot.message_handler(func=lambda message: message.reply_to_message and message.reply_to_message.text == "Digite seu nome:")
    def receber_nome(message):
        nome = message.text
        dados_agendamento.append(nome) # Adicionando nome à lista
        bot.send_message(message.chat.id, "Agora digite seu telefone:", reply_markup=ForceReply())
        bot.register_next_step_handler(message, receber_telefone)
    
    def receber_telefone(message):
        telefone = message.text
        dados_agendamento.append(telefone)
        bot.send_message(message.chat.id, "Escolha um serviço:", reply_markup=servicos_disponiveis())
        bot.register_next_step_handler(message, receber_servico)

    def receber_servico(message):
        servico = message.text
        dados_agendamento.append(servico)
        bot.send_message(message.chat.id, "Digite uma data:")
        bot.send_message(message.chat.id, "Exemplo: " + datetime.now().strftime("%d/%m/%Y"))
        bot.register_next_step_handler(message, receber_data)

    def receber_data(message):
        try:
            data = datetime.strptime(message.text, "%d/%m/%Y")
            data_formatada = data.strftime("%Y-%m-%d")
            
            teclado_horarios = horarios_disponiveis(message.text)
            
            if teclado_horarios:
                dados_agendamento.append(data_formatada)
                bot.send_message(message.chat.id, "Escolha um horário disponível:", reply_markup=teclado_horarios)
                bot.register_next_step_handler(message, receber_horario)
            else:
                bot.send_message(message.chat.id, "❌ Não há horários disponíveis para esta data. Por favor, escolha outra data.")
                bot.register_next_step_handler(message, receber_data)
        except ValueError:
            bot.send_message(
            message.chat.id, f"❌ Data inválida! Por favor, digite a data no formato **dd/mm/aaaa**.\nExemplo: {datetime.now().strftime('%d/%m/%Y')}")
            # Registra novamente o handler para receber a data correta
            bot.register_next_step_handler(message, receber_data)
        
    def receber_horario(message):
        horario = message.text
        dados_agendamento.append(horario)
        confirmar_agendamento(message)

    def confirmar_agendamento(message):
        # Salva o agendamento no banco de dados
        salvar_agendamento(
            dados_agendamento[0],  # Nome
            dados_agendamento[1],  # Telefone
            dados_agendamento[3] + " " + dados_agendamento[4],  # Data e Hora
            dados_agendamento[2],  # Serviço
            message.chat.id        # ID do chat
        )

        # Exibe as informações contidas em dados_agendamento
        bot.send_message(
            message.chat.id,
            f"Agendamento confirmado para {dados_agendamento[0]}!\n"
            f"Serviço: {dados_agendamento[2]}\n"
            f"Telefone: {dados_agendamento[1]}\n"
            f"Data e Hora: {datetime.strptime(dados_agendamento[3], '%Y-%m-%d').strftime('%d/%m/%Y')} às {dados_agendamento[4]}"
        )

        # Limpa a lista para o próximo agendamento
        dados_agendamento.clear()
