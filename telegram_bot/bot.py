from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (Updater, CallbackQueryHandler, CallbackContext, )
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.commandhandler import CommandHandler
from src.input_username import validate_input, take_input
from database import get_saved_info, get_player_name
from src.config import get_soup
from src.last_updated import update_results, last_updated

# from main import main

from database import collection

updater = Updater("",
                  use_context=True)

input = []


def check_player(update: Update, context: CallbackContext):
    text = update.message.text
    # print(text)
    if '#' in text:
        input.append(text)

        keyboard = [
            [
                InlineKeyboardButton("Match History 30 Matches", callback_data='1'),
                InlineKeyboardButton("Statistics", callback_data='2'),
            ],
            [InlineKeyboardButton("Get Notified", callback_data='3')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Please choose:', reply_markup=reply_markup)


input_query = []


def button(update: Update, context: CallbackContext):
    """Parses the CallbackQuery and updates the message text."""

    query = update.callback_query
    query.edit_message_text(f"Hi {input[0].split('#')[0]}")

    query.answer()
    # print(query.data)
    input_query.append(query.data)
    # query.edit_message_text(text=f"Selected option: {query.data}")
    # print(input)
    print(input_query)
    if query.data == '1':
        print(input[0])

        url = take_input(input[0])[0]
        print(url)
        player_name = get_player_name(input[0])[0]
        print(player_name, url)
        soup = get_soup(url)
        if not validate_input(soup):
            # update.message.reply_text('fdfd')
            send_message(update,context,  data=query.data)
            # update.callback_query.message.edit_text('Username is correct')
            # update.callback_query.message.edit_text('Shadows travelling')
            # update.callback_query.message.edit_text('Updating results')
            # if update_results(url):
            #     update.callback_query.message.edit_text('Updating results')

        # print(input)

        # t = collection.find({'player_name': input[0].replace('#', '-')})
        # print(t)


def send_message(update: Update, context: CallbackContext, data):
    update.message.reply_text('Username is correct')
    update.message.reply_text('Shadows travelling')
    update.message.reply_text(data)

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(MessageHandler(Filters.text, check_player))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(MessageHandler(Filters.text, send_message))
updater.dispatcher.add_handler(MessageHandler(Filters.text, button))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, check_player))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

print('Bot running')
updater.start_polling()
updater.idle()
