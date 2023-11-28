from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes, ConversationHandler

STATEONE: int = 0
TO_LANGUAGE: dict = {0: 'en'}


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
        await update.message.reply_text(text=f"سأبدأ بالترجمة إلى اللغة العربية!")
        TO_LANGUAGE[update.effective_user.id] = 'ar'
    elif user_response == 'English':
        await update.message.reply_text(text=f"I will start translating to English!")
        TO_LANGUAGE[update.effective_user.id] = 'en'
    elif user_response == 'Русский':
        await update.message.reply_text(text=f"Начну переводить на русский!")
        TO_LANGUAGE[update.effective_user.id] = 'ru'
    elif user_response == 'Español':
        await update.message.reply_text(text=f"¡Comenzaré a traducir al español!")
        TO_LANGUAGE[update.effective_user.id] = 'es'
    elif user_response == 'Français':
        await update.message.reply_text(text=f"Je vais commencer à traduire en français !")
        TO_LANGUAGE[update.effective_user.id] = 'fr'
    elif user_response == 'हिन्दी':
        await update.message.reply_text(text=f"मैं हिन्दी में अनुवाद करना शुरू करूँगा!")
        TO_LANGUAGE[update.effective_user.id] = 'hi'
    elif user_response == 'فارسی':
        await update.message.reply_text(text=f"من شروع به ترجمه به فارسی می کنم!")
        TO_LANGUAGE[update.effective_user.id] = 'fa'
        return STATEONE
    elif user_response == 'Português':
        await update.message.reply_text(text=f"Vou começar a traduzir para o Português!")
        TO_LANGUAGE[update.effective_user.id] = 'pt'
    elif user_response == 'Deutsch':
        await update.message.reply_text(text=f"Ik ga beginnen met vertalen naar het Duits!")
        TO_LANGUAGE[update.effective_user.id] = 'de'

    return ConversationHandler.END

