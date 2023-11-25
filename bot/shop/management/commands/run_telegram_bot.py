from django.core.management.base import BaseCommand

import telebot
from shop.models import Games

bot = telebot.TeleBot("6918185061:AAGm8cQud20udcZK4DYpPmDTrlb33KXq4eY")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello World")


@bot.message_handler(commands=['games'])
def games(message):
    games = Games.objects.all()
    for game in games:
        bot.send_message(message.chat.id, f"games:{game.name},price:{game.price}")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f"help: /start, /games")

@bot.message_handler(commands=['add'])
def add(message):
    bot.send_message(message.from_user.id, "Введи название")
    bot.register_next_step_handler(message, title_handler)

def title_handler(message):
    global title
    title = message.text

    bot.send_message(message.chat.id, "Напиши цену")
    bot.register_next_step_handler(message, price_handler)

def price_handler(message):
    global price
    price = message.text
    bot.send_message(message.chat.id, f"Ураааа")
    new_game = Games.objects.create(name=title, price=price)

    


#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
    #bot.reply_to(message, message.text)
        


class Command(BaseCommand):
   def handle(self, *args, **options):
       print("Starting bot...")
       bot.polling()
       print("Bot stopped")
   