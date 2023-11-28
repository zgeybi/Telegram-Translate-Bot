from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes, ConversationHandler

STATEONE: int = 0
TO_LANGUAGE: str = 'ru'


async def language_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("Dialogue..Language List")
    buttons = [[KeyboardButton("العربية")],
               [KeyboardButton("English")],
               [KeyboardButton("Русский")],
               [KeyboardButton("Español")],
               [KeyboardButton("Français")],
               [KeyboardButton("हिन्दी")],
               [KeyboardButton("فارسی")],
               [KeyboardButton("Português")],
               [KeyboardButton("Deutsch")]]

    await update.message.reply_text(text="Choose the language you want to translate to!",
                                    reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True,
                                                                     input_field_placeholder="Choose language"),
                                    )
    return STATEONE


async def first_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> False:
    global TO_LANGUAGE
    print("Dialogue..first_answer")
    user_response = update.message.text
    if user_response == 'العربية':
        await update.message.reply_text(text=f"I will start translating to العربية!")
        TO_LANGUAGE = 'ar'
    elif user_response == 'English':
        await update.message.reply_text(text=f"I will start translating to English!")
        TO_LANGUAGE = 'en'
    elif user_response == 'Русский':
        await update.message.reply_text(text=f"I will start translating to Русский!")
        TO_LANGUAGE = 'ru'
    elif user_response == 'Español':
        await update.message.reply_text(text=f"I will start translating to Español!")
        TO_LANGUAGE = 'es'
    elif user_response == 'Français':
        await update.message.reply_text(text=f"I will start translating to Français!")
        TO_LANGUAGE = 'fr'
    elif user_response == 'हिन्दी':
        await update.message.reply_text(text=f"I will start translating to हिन्दी!")
        TO_LANGUAGE = 'hi'
    elif user_response == 'فارسی':
        await update.message.reply_text(text=f"I will start translating to فارسی!")
        TO_LANGUAGE = 'fa'
        return STATEONE
    elif user_response == 'Português':
        await update.message.reply_text(text=f"I will start translating to Português!")
        TO_LANGUAGE = 'pt'
    elif user_response == 'Deutsch':
        await update.message.reply_text(text=f"I will start translating to Deutsch!")
        TO_LANGUAGE = 'de'

    return ConversationHandler.END

