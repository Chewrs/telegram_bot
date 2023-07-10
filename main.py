import responses as R
from telegram.ext import *

API_KEY = "6042456865:AAFVh7YUbkrmzkDqYsU2DbhS4NAlkWv57vA"
print("bot started...")


def start_command(update, context):
    update.message.reply_text("type something random to get started!")


def help_command(update, context):
    update.message.reply_text("if you need help! dm +66 9 8264 1974")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)


def error(update, context):
    print(f"update {update} caused error {context.error}")


def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
