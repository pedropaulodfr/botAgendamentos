import telebot
from keyboards import menu_principal

def start(bot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, f"Olá, {message.from_user.first_name}! Escolha uma opção:", reply_markup=menu_principal())
