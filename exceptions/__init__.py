from discord.ext import commands

class UserBlacklisted(commands.CheckFailure):
    def __init__(self, message="User is blacklisted!"):
        self.message = message
        super().__init__(self.message)


class UserNotOwner(commands.CheckFailure):
    def __init__(self, message="User is not an owner of the bot!"):
        self.message = message
        super().__init__(self.message)
