from discord.ext import commands
from discord import Intents

from managers import mongo_manager
from config import TOKEN

class PokeCol(commands.Bot):

    intents:Intents = Intents.default()
    intents.message_content = True
    intents.members = True
    intents.presences = True

    initial_cogs = [
        "cogs.utility",
        "cogs.collection"
    ]

    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(">>"), case_insensitive=True, description="An easy-to-use, self hosted collection bot for pokemon players on discord.", intents=self.intents)

        for cog in self.initial_cogs:
            self.load_extension(cog)

    async def on_ready(self):
        db_reply = await mongo_manager.init_mongo()
        print(db_reply)

        print("Logged in as {}".format(self.user))

def main():

    try:
        bot = PokeCol()
        bot.run(TOKEN)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()