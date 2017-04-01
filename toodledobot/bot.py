from telegram.ext import CommandHandler, Updater, CallbackQueryHandler, RegexHandler, ConversationHandler, \
    MessageHandler, Filters

from .handlers import *


class ToodledoBot:
    def __init__(self, telegram_token):
        self.updater = Updater(token=telegram_token)

    def start(self):
        self.setup_handlers()
        self.updater.start_polling()

    def setup_handlers(self):
        dispatcher = self.updater.dispatcher
        dispatcher.add_handler(CommandHandler('start', start_handler))
        dispatcher.add_handler(CommandHandler('cal', calendar_handler))
        dispatcher.add_handler(CommandHandler('auth', auth_handler, pass_args=True))
        dispatcher.add_handler(CommandHandler('list', get_tasks_handler))
        dispatcher.add_handler(RegexHandler('#(\w+)', get_tasks_by_tag_handler, pass_groups=True))
        dispatcher.add_handler(CommandHandler('add', add_task_handler))
        dispatcher.add_handler(MessageHandler(Filters.reply & (Filters.text | Filters.command), task_edit_handler))
        dispatcher.add_error_handler(error_handler)
