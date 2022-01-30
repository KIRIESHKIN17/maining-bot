import telebot
#from telebot import types


bot = telebot.Telebot('5259869971:AAG8E07VuKAU5RXgYgM8IJIoijDCkt0UZHA')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем могу помочь?")
    elif message.text =="/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif bot.send_message(message.from_user.id, " Я тебя не понимаю, напиши привет")
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я майнинг бот, средства не вывожу")
    elif message.text =="Какое у меня оборудование и сколько оно приносит в сутки?":
        bot.send_message(message.from_user.id, " У тебя nvidia gtx 1050ti доходность в сутки 1 доллар")
    elif message.text ==" Начать майнить ":
        bot.send_message(message.from_user.id, "Сколько долларов заработал?")
    elif message.text =="1 доллар":
        bot.send_message(message.from_user.id, "Продолжить майнить?")
    elif message.text == "продолжить майнить":
    elif message.text ==" 2 доллара":
        bot.send_message(message.from_user.id, " Ты можешь купить 1070ti, доходность в сутки 2 доллара")
        bot.send_message(message.from_user.id, " Купить 1070ti?")
    elif message.text ==" Да, купить":
        bot.send_message(message.from_user.id, "Сколько долларов заработал?")
    elif message.text ==" 3 доллара":
        bot.send_message(message.from_user.id, " Продолжить майнить?")
    elif message.text == "Продолжить майнить":
        bot.send_message(message.from_user.id, "Сколько долларов заработал?")
    elif message.text == " 6 доллара":
        bot.send_message(message.from_user.id, " Продолжить майнить?")
    elif message.text == "Продолжить майнить":
        bot.send_message(message.from_user.id, "Сколько долларов заработал?")
    elif message.text == " 9 долларов":
        bot.send_message(message.from_user.id, " Продолжить майнить?")
    elif message.text == "Продолжить майнить":
        bot.send_message(message.from_user.id, "Сколько долларов заработал?")
    elif message.text == " 12 долларов":
        bot.send_message(message.from_user.id, " Продолжить майнить?")
    elif message.text == "Продолжить майнить":
        bot.send_message(message.from_user.id, "Сколько долларов заработал?")
    elif message.text == " 15 долларов":
        bot.send_message(message.from_user.id, " Продолжить майнить?")
    elif message.text == "Продолжить майнить":
        bot.send_message(message.from_user.id, "Сколько долларов заработал?")
    elif message.text == " 18 долларов":
        bot.send_message(message.from_user.id, " Продолжить майнить?")
    elif message.text == "Продолжить майнить":
        bot.send_message(message.from_user.id, "Сколько долларов заработал?")
    elif message.text == " 21 доллар":
        bot.send_message(message.from_user.id, " Продолжить майнить?")
    elif message.text == "Продолжить майнить":
        bot.send_message(message.from_user.id, "Сколько долларов заработал?")
    elif message.text == " 24 доллара":
        bot.send_message(message.from_user.id, "Поздравляю, теперь ты можешь купить новую 2060ti, доходность в сутки 7 долларов ")
        bot.send_message(message.from_user.id, " Купить 2060ti?")
    elif message.text == "Да, купить":
        bot.send_message(message.from_user.id, "Поздравляю, теперь твоя доходность 7 долларов в сутки")
        bot.send_message(message.from_user.id, "Начать майнить?")
    elif message.text == "Начать майнить":
    elif message.text == "Магазин видеокарт":
        bot.send_message(message.from_user.id,"1050ti 1$ дохожность в сутки 1 доллар, 1070ti 2$ доходность в сутки 2 доллара, 1080ti 5$ доходность в сутки 3 доллара, 2060 ti 20$ доходнность в сутки 7 долларов, 2070 22$ доходность в сутки 8 долларов, 2070ti 24$ доходность в сутки 9 долларов, 2080 40$ доходность в сутки 10 долларов, 2090ti 70$ доходность в сутки 12 долларов")








bot.polling(none_stop=True, interyal=0)

