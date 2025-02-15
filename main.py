import telebot
from config import TOKEN
from handlers.start import start
from handlers.agendamento import agendamento_handlers
from handlers.visualizar import visualizar_handlers

bot = telebot.TeleBot(TOKEN)

# Registrar handlers
start(bot)
agendamento_handlers(bot)
visualizar_handlers(bot)

print("Bot está rodando...")
bot.remove_webhook()
bot.infinity_polling()