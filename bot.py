import telebot
from telebot import types

BOT_TOKEN = '7546666892:AAFdCCYAexVEdOLaRA2i4WlSEOTp5ugQ8BI'
WEBAPP_URL = 'https://mikeymouse0.github.io/MikeyMouse0-/'  # Замените на ваш URL

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo(WEBAPP_URL)
    markup.add(types.InlineKeyboardButton("Открыть Web App", web_app=web_app))
    bot.send_message(message.chat.id, "Нажмите кнопку для открытия Web App:", reply_markup=markup)

@bot.message_handler(content_types=['web_app_data'])
def web_app_data(message):
    bot.send_message(message.chat.id, f"Вы отправили из Web App: {message.web_app_data.data}")

if __name__ == '__main__':
    bot.polling() 
