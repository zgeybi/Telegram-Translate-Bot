from telegram.ext import ContextTypes, ConversationHandler
from telegram import Update
import dialogue
import API


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dialogue.TO_LANGUAGE[update.effective_user.id] = 'en'
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""Hey! Welcome to Yandex Translate bot!
Here you can translate text from any language to a language of your choice!
You don't need to specify source language, Yandex API will identify the language on its own :)
The bot translates to English by default.
Use /help to get more help!""")


async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in dialogue.TO_LANGUAGE.keys():

        await update.message.reply_text(text=
                                        f"{API.translate(dialogue.TO_LANGUAGE[0], update.message.text)}")
    else:
        await update.message.reply_text(text=
                                        f"{API.translate(dialogue.TO_LANGUAGE[update.effective_user.id], update.message.text)}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="""Available commands:
    1. /start - Restart the bot
    2. /choose_language - choose target language (the one you want to translate to)
    3. /help - Print this help message
    4. /cancel - To cancel choosing a language
No need to choose source language because I can identify the language on my own :)
By default, I translate to English.
To Translate text it's enough to send me a message with the text you need to translate.""")


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(text="Canceled")
    return ConversationHandler.END
