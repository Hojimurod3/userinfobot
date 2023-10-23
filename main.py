from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    user_id = user.id
    user_first_name = user.first_name
    user_last_name = user.last_name
    user_username = user.username
    update.message.reply_text(f"User ID: {user_id}\nFirst Name: {user_first_name}\nLast Name: {user_last_name}\nUsername: {user_username}")

def main():
    updater = Updater(token='6460684839:AAHps-3sFzzDuDdb4SPiLfdvAjvri83zS7M', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
