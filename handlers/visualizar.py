from database import buscar_agendamentos

def visualizar_handlers(bot):
    @bot.message_handler(func=lambda message: message.text == "Visualizar Agendamento")
    def visualizar_agendamento(message):
        agendamentos = buscar_agendamentos(message.chat.id)
        if agendamentos:
            resposta = "\n\n".join([f"Nome: {a[0]}\nTelefone: {a[1]}\nData e Hora: {a[2]} às {a[3]}" for a in agendamentos])
        else:
            resposta = "Nenhum agendamento encontrado."
        bot.send_message(message.chat.id, resposta)
