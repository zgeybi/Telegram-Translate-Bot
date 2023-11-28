import logging
from typing import Final
from telegram.ext import MessageHandler, ConversationHandler, CommandHandler, ApplicationBuilder, filters
from dialogue import STATEONE, first_answer, language_list
import commands

TOKEN: Final = '6323445519:AAEvIc1VCDWdq6OHCsV5ai-fvsV1JlEpd-I'
BOT_USERNAME: Final = '@yandex_translate_mipt_bot'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


if __name__ == '__main__':
    print("connecting to bot")
    application = ApplicationBuilder().token(TOKEN).build()
    help_handler = CommandHandler('help', commands.help_command)
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('list_languages', language_list)],
        states={
            STATEONE: [MessageHandler(filters.Regex(
                                        "^(العربية|English|Русский|Español|Français|हिन्दी|فارسی|Português|Deutsch)$"),
                       first_answer)],
        },
        fallbacks=[CommandHandler("cancel", commands.cancel)]
    )

    application.add_handler(CommandHandler('start', commands.start))
    application.add_handler(conversation_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, commands.translate))
    application.add_handler(help_handler)
    application.run_polling()
    print("stopped polling")
