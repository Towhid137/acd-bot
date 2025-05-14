from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

TOKEN = os.getenv("BOT_TOKEN")  # Railway-তে ENV var থেকে টোকেন নেবে

# ইউজারদের স্ট্যাটাস ট্র্যাকিং
user_status = {}

def start(update, context):
    user_id = update.effective_user.id
    user_status[user_id] = 'started'
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="স্বাগতম! আপনি একটি ছবি পাঠালে আমরা রিপ্লাই দিবো।")

def handle_photo(update, context):
    user_id = update.effective_user.id
    if user_status.get(user_id) == 'started':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="ধন্যবাদ! আমরা আপনার ছবি পেয়েছি।")
        user_status[user_id] = 'done'

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
