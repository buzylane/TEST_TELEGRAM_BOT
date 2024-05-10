from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your order monitoring bot.')

def handle_message(update: Update, context: CallbackContext):
    message_text = update.message.text
    if message_text.startswith('New Order Placed'):
        # Process the order here
        update.message.reply_text('Processing your order!')
        # Add your order processing logic here

def main():
    TOKEN = '6397079783:AAFDjNLUqcWn-ZiCaGQ3aaHqGE8DSXkrLv8'  # Replace with your bot's token
    bot = Bot(TOKEN)
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
