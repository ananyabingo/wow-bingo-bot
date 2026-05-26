import telebot
from telebot import types

API_TOKEN = '8850948511:AAH8UiHe073d38byzo9cfdkpZA0F9_2OdJY'
bot = telebot.TeleBot(API_TOKEN)


bot.delete_webhook()

WEBAPP_URL = "https://tiiny.site"


def set_bot_commands():
    commands = [
        types.BotCommand("start", "Start Harar Bingo"),
        types.BotCommand("register", "Register your account"),
        types.BotCommand("play", "Play Bingo Game"),
        types.BotCommand("deposit", "Deposit Money"),
        types.BotCommand("balance", "Check Balance"),
        types.BotCommand("withdraw", "Withdraw Money"),
        types.BotCommand("transfer", "Transfer Balance"),
        types.BotCommand("invite", "Invite Friends"),
        types.BotCommand("instruction", "How to Play"),
        types.BotCommand("support", "Contact Support")
    ]
    bot.set_my_commands(commands)


def get_bingo_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # 10 ዋና ዋና የቢንጎ ቁልፎች ማውጫ
    btn_play = types.InlineKeyboardButton("Play 🎰", web_app=types.WebAppInfo(url=WEBAPP_URL))
    btn_register = types.InlineKeyboardButton("Register 📝", callback_data="btn_register")
    btn_balance = types.InlineKeyboardButton("Check Balance 💵", callback_data="btn_balance")
    btn_deposit = types.InlineKeyboardButton("Deposit 💰", callback_data="btn_deposit")
    btn_support = types.InlineKeyboardButton("Contact Support ☎️", callback_data="btn_support")
    btn_instruction = types.InlineKeyboardButton("Instruction 📖", callback_data="btn_instruction")
    btn_transfer = types.InlineKeyboardButton("Transfer 🎁", callback_data="btn_transfer")
    btn_withdraw = types.InlineKeyboardButton("Withdraw 🤑", callback_data="btn_withdraw")
    btn_invite = types.InlineKeyboardButton("Invite 🔗", callback_data="btn_invite")
    btn_bonus = types.InlineKeyboardButton("Convert Bonus 💎", callback_data="btn_bonus")
    
    markup.add(btn_play, btn_register)
    markup.add(btn_balance, btn_deposit)
    markup.add(btn_support, btn_instruction)
    markup.add(btn_transfer, btn_withdraw)
    markup.add(btn_invite, btn_bonus)
    
    return markup


@bot.message_handler(commands=['start', 'play', 'register', 'deposit', 'balance', 'withdraw', 'transfer', 'invite', 'instruction', 'support'])
def handle_commands(message):
    chat_id = message.chat.id
    welcome_text = (
        "👋 **Welcome to Harar Bingo! Choose an Option below.**\n\n"
        "🇪🇹 እንኳን ወደ ሀረር ቢንጎ በደህና መጡ! ከታች ካሉት አማራጮች አንዱን ይምረጡ።"
    )
    markup = get_bingo_markup()
    bot.send_message(chat_id, welcome_text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    chat_id = call.message.chat.id
    if call.data == "btn_register":
        bot.send_message(chat_id, "📝 **Registration**\nPlease enter your phone number to register.")
    elif call.data == "btn_balance":
        bot.send_message(chat_id, "💵 **Your Balance:** 0.00 ETB")
    elif call.data == "btn_deposit":
        bot.send_message(chat_id, "💰 **Deposit Info (Telebirr):**\nSend entry fee to one of the numbers and put your Telegram ID in remark.")
    elif call.data == "btn_support":
        bot.send_message(chat_id, "☎️ **Support:** Contact @Ananya_Adefers for help.")
    elif call.data == "btn_instruction":
        bot.send_message(chat_id, "📖 **Instruction:** Open the Web App, wait for numbers to be called out loud!")
    elif call.data == "btn_transfer":
        bot.send_message(chat_id, "🎁 **Transfer:** Enter the Telegram ID of the user you want to transfer money to.")
    elif call.data == "btn_withdraw":
        bot.send_message(chat_id, "🤑 **Withdrawal:** Enter the amount you want to withdraw to your Telebirr.")
    elif call.data == "btn_invite":
        bot.send_message(chat_id, f"🔗 **Your Invite Link:** https://t.me{bot.get_me().username}?start={chat_id}")
    elif call.data == "btn_bonus":
        bot.send_message(chat_id, "💎 **Bonus:** You don't have enough bonus points to convert yet.")
    bot.answer_callback_query(call.id)


if __name__ == '__main__':
    set_bot_commands()
    print("Harar Bingo Bot is running successfully...")
    bot.infinity_polling(skip_pending=True)
