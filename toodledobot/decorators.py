from toodledo import NotAuthorizingError


def not_authorized_wrapper(func):
    def wrap(bot, update, *args, **kwargs):
        try:
            return func(bot, update, *args, **kwargs)
        except NotAuthorizingError:
            bot.sendMessage(chat_id=extract_user_id(update),
                            text="Not authorized\nAuthorize by /auth "
                                 "and follow the instructions",
                            disable_web_page_preview=True)
    return wrap


def add_user_id(func):
    def wrapped(bot, update, *args, **kwargs):
        uid = extract_user_id(update)
        res = func(bot, update, *args, uid=uid, **kwargs)
        return res
    return wrapped


def extract_user_id(update):
    getters = (lambda u: u.message.from_user.id,
               lambda u: u.inline_query.from_user.id,
               lambda u: u.chosen_inline_result.from_user.id,
               lambda u: u.callback_query.from_user.id)

    for get_uid in getters:
        try:
            return get_uid(update)
        except (NameError, AttributeError):
            continue
    return None
