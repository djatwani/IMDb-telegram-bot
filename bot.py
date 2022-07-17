from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, updater
from scraper import scrape_movie


bot_token = "1739805317:AAHwFRSOdL_wBqbOXweplBjNnxfZOEXR_3Q"

keys = ["title", "rating", "duration"]

# ECHO BOT


""" def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi!")


def message(update, context):
    msg = update.message.text
    update.message.reply_text(msg)


def run_bot():
    updater = Updater(bot_token)
    dp = updater.dispatcher
    start_command_handler = CommandHandler("start", start)
    message_handler = MessageHandler(Filters.text, message)
    dp.add_handler(start_command_handler)
    dp.add_handler(message_handler)
    updater.start_polling()
    updater.idle() """


# TELEGRAM BOT


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi! I can help you search movies on IMDB.\nPlease enter /movie to get started",
    )


def movie(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Please enter the name of the movie you wish to search for!",
    )


def search_movie(update, context):
    movie_name = update.message.text
    update.message.reply_text("Searching for details of " + movie_name)
    print(movie_name)
    movie_info = scrape_movie(movie_name=movie_name)
    for key in keys:
        update.message.reply_text("The " + key + " of the movie is " + movie_info[key])
    update.message.reply_text("There you go!")


def run_bot():
    updater = Updater(bot_token)
    dp = updater.dispatcher
    # Add command handler
    start_command_handler = CommandHandler("start", start)
    movie_command_handler = CommandHandler("movie", movie)
    # Add message handler
    movie_handler = MessageHandler(Filters.text, search_movie)
    dp.add_handler(start_command_handler)
    dp.add_handler(movie_command_handler)
    dp.add_handler(movie_handler)
    updater.start_polling()
    updater.idle()


run_bot()
