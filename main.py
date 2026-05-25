import telebot
from telebot import types

`API_TOKEN = '8718835672:AAE9L-dIaCzeWPNCQFkyaxadNE5-P1AQr0w'`
bot = telebot.TeleBot(API_TOKEN)

WEBAPP_URL = "https://tiiny.site" 

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name
    
    markup = types.InlineKeyboardMarkup()
    webapp_button = types.InlineKeyboardButton(
        text="🎰 Open Wow Bingo App", 
        web_app=types.WebAppInfo(url=WEBAPP_URL)
    )
    markup.add(webapp_button)
    
    welcome_text = (
        f"Welcome {user_name} to **Wow Bingo Auto**! 🎰\n\n"
        f"👤 **Account Owner Name:** ANANYA ADEFERS\n\n"
        f"💳 **How to Deposit (Telebirr):**\n"
        f"Send your game entry fee to one of these numbers:\n"
        f"1️⃣ Account 1: `0940403289`\n"
        f"2️⃣ Account 2: `0979152240`\n\n"
        f"⚠️ **IMPORTANT:** You MUST put your Telegram ID `{chat_id}` in the Telebirr 'Reference' field when sending money!\n\n"
        f"Once you sent the money, click the button below to start playing!"
    )
    bot.send_message(chat_id, welcome_text, parse_mode="Markdown", reply_markup=markup)

print("Wow Bingo Bot is running...")
bot.infinity_polling()
