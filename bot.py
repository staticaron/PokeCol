from discord.ext import commands
from discord import Intents

from managers import mongo_manager
from managers import cache_manager
from helpers import general_helper
from config import TOKEN
import config

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
        
        """Cache static data"""
        cache_reply = await cache_manager.cache_data()
        print(cache_reply)

        """Load Mongo Manager"""
        db_reply = await mongo_manager.init_mongo()
        print(db_reply)

        """Load Prefix and timer values"""
        prefix, timer = await general_helper.get_prefix_and_timer()
        config.modify_prefix_and_timer(prefix, timer)

        print("Logged in as {}".format(self.user))

def main():

    try:
        bot = PokeCol()
        bot.run(TOKEN)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()