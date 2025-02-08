import telebot
from config import TOKEN
from handlers.start import start
from handlers.agendamento import agendamento_handlers
from handlers.visualizar import visualizar_handlers
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    None

bot = telebot.TeleBot(TOKEN)

# Registrar handlers
start(bot)
agendamento_handlers(bot)
visualizar_handlers(bot)

print("Bot está rodando...")
bot.polling()

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))