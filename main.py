import os
import threading
import telebot
from config import TOKEN
from handlers.start import start
from handlers.agendamento import agendamento_handlers
from handlers.visualizar import visualizar_handlers
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot está rodando!"

bot = telebot.TeleBot(TOKEN)

# Registrar handlers
start(bot)
agendamento_handlers(bot)
visualizar_handlers(bot)

def run_bot():
    print("Bot está rodando...")
    bot.infinity_polling()  # Usa infinity_polling() para evitar falhas

# Iniciar o bot em uma thread separada
bot_thread = threading.Thread(target=run_bot, daemon=True)
bot_thread.start()

# Iniciar o servidor Flask
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
