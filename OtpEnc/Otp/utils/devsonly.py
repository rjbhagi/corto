from .. import ADMINS


def is_admin(f):
    async def wrapper(client, message):
        if message.from_user.id in ADMINS:
            return await f(client, message)
        return
    return wrapper