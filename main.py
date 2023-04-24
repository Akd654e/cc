import telebot
bot=telebot.TeleBot("6256388095:AAGmD_2kTGga47-do_NhNxrcEZsgp-6_Kqc")
@bot.message_handler(commands=["start"])
def start(message):
    s=bot.send_message(chat_id=message.chat.id,text="حسنا عزيزي ارسل رقم الصورة")
    bot.register_next_step_handler(s,testing)
@bot.message_handler(func=lambda m:True)
def testing(message):
    try:
        pot=int(message.text)
    except:
        bot.send_message(message.chat.id,"ارسل رقم فقط")
    bot.send_photo(message.chat.id,f"https://raw.githubusercontent.com/maknon/Quran/main/pages-douri/{pot}.png")
bot.infinity_polling()