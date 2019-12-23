from main_func import gen_char
import telebot;
bot = telebot.TeleBot('1043487914:AAEwGtxepUu_vMtpLYiy9WbrYEIm5om_Z44');
from telebot import types

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    # Если написали «Привет»

    if message.text == "Привет":

        # Пишем приветствие

        bot.send_message(message.from_user.id, "Привет, сейчас я создам тебе персонажа для DnD:")

        # Готовим кнопки

        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик для каждого знака зодиака

        key_char = types.InlineKeyboardButton(text='Создать', callback_data='zodiac')

        # И добавляем кнопку на экран

        keyboard.add(key_char)


        # Показываем все кнопки сразу и пишем сообщение о выборе

        bot.send_message(message.from_user.id, text='Нажмите чтобы создать персонажа:', reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши Привет")

    else:

        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

 
# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):

    # Если нажали на одну из 12 кнопок — выводим гороскоп

    if call.data == "zodiac": 

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, gen_char)


	
bot.polling(none_stop=True, interval=0)
