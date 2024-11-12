from ..modules.database.main_db import BlackList






def detect_flood(func):
    def wrapper(*args, **kwargs):
        # Do something here
        return func(*args, **kwargs)
    return wrapper

def blacklist(func):
    async def wrapper(bot, m, *args, **kwargs):
        for i in BlackList().get_all_users():
            try:
                if i[0] == m.from_user.id:
                    return await m.reply_text("You are blacklisted")
            except:
                return await func(bot, m, *args, **kwargs)
        return await func(bot, m, *args, **kwargs)
    return wrapper