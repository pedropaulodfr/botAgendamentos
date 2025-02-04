import telebot
from keyboards import menu_principal

def start(bot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, "Olá! Escolha uma opção:", reply_markup=menu_principal())
