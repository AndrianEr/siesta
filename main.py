import telebot
from telebot import types

bot= telebot.TeleBot("5741874217:AAEh7eyrpu75SX7Sdgb2xnnY91B67LXsw6I")

@bot.message_handler(commands=['start', 'help' ,'site'])
def send_message(message):
    bot.send_message(message.chat.id, "Hello")

@bot.message_handler(commands=['button'])
def buttons_tel(message):
    markcup= types.ReplyKeyboardMarkup(resize_keyboard=True)
    tem1= types.KeyboardButton("global")
    tem2= types.KeyboardButton("site")
    tem3= types.KeyboardButton("info")
    tem4= types.KeyboardButton("help")
    markcup.add(tem1,row_width=10)
    markcup.add(tem2,row_width=10)
    markcup.add(tem3,row_width=10)
    markcup.add(tem4,row_width=10)

    bot.send_message(message.chat.id, 'What are you need?', reply_markup=markcup)



if __name__=="__main__":
    bot.infinity_polling()