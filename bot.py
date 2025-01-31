import telebot

TOKEN = "7547292799:AAHVAy0b2qyj0G05Z3z3aXIBigRTDq0XnIA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['foto'])
def send_photo(message):
    photo_url = "http://configplus.ct.ws/surat/hemmesine.jpg"  # Замени на свою ссылку
    caption_text = "ine pubg surat gorkany, gordinmi? indi gormisen ohoh FRONZY 3.6 TDM SETİ V1 CONFİG : TDM ÜST ETİ : TDM EŞORTMANEYTAN BOYNUZ: GÖZ BANDI: GLOBAL/ KORE : 32 + 64 BİT GEÇE ÇALIŞMASI İÇİN GİYMENİZ GEREKEN  KIYAFETLER https://t.me/fronzyhack/10KURULUM ttps://t.me/fronzykurulum/28tps://t.me/addlist/VYfCaZ45zU40MmRk"
    bot.send_photo(message.chat.id, photo_url, caption=caption_text)

@bot.message_handler(commands=['start'])
def start_command(message):
    text = "Привет! Вот список команд:\n"
    text += "/mensen - Информация о пользователе\n"
    text += "/videolar - Список цифр\n"
    text += "/pubguc - Ввод PUBG ID и email"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['mensen'])
def mensen_command(message):
    user = message.from_user
    info = f"👤 Имя: {user.full_name}\n🆔 ID: {user.id}\n💬 Юзернейм: @{user.username if user.username else 'Нет'}"
    bot.send_message(message.chat.id, info)

@bot.message_handler(commands=['videolar'])
def videolar_command(message):
    text = "Выберите номер:\n/58\n/59"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['58', '59'])
def number_command(message):
    bot.send_message(message.chat.id, f"Вы выбрали: {message.text}")

@bot.message_handler(commands=['pubguc'])
def pubguc_command(message):
    bot.send_message(message.chat.id, "Отправьте ваш PUBG ID и email (example@gmail.com):")

@bot.message_handler(func=lambda message: "@" in message.text and "." in message.text)
def handle_pubg_data(message):
    data = message.text.split()
    if len(data) == 2 and data[1].endswith("@gmail.com") and data[0].isdigit():
        bot.send_message(message.chat.id, "✅ Данные приняты!")
    else:
        bot.send_message(message.chat.id, "❌ Неверный формат! Введите PUBG ID и email (@gmail.com) через пробел.")

bot.polling()