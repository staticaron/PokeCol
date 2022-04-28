from discord.ext import commands
from discord import Intents, Message, Embed
from datetime import datetime

from managers import mongo_manager
from managers import cache_manager
from helpers import general_helper
from config import TOKEN, NORMAL_COLOR
import config

def get_prefix(bot, message):
    return ["<@968502660862988368> ", "<@!968502660862988368> ", config.PREFIX]

class PokeCol(commands.Bot):

    intents:Intents = Intents.default()
    intents.message_content = True
    intents.members = True
    intents.presences = True

    initial_cogs = [
        "cogs.utility",
        "cogs.collection"
    ]

    def __init__(self, prefix:str):
        super().__init__(command_prefix=get_prefix, case_insensitive=True, description="An easy-to-use, self hosted collection bot for pokemon players on discord.", intents=self.intents)

        for cog in self.initial_cogs:
            self.load_extension(cog)

    async def on_ready(self):
        print("Logged in as {}".format(self.user))

    async def on_message(self, message:Message):

        if message.content.strip() == "<@968502660862988368>" or message.content.strip() == "<@!968502660862988368>":
            ping_reply = Embed(title=f"Alola :wave:, I am {self.user.name}", color=NORMAL_COLOR, description=f"**Prefix** : {config.PREFIX}\n**Latency** : {round(self.latency * 1000, 2)} ms \n\n**Try** {config.PREFIX}help")
            ping_reply.set_footer(text=f"Requested by {message.author.name}", icon_url=message.author.avatar.url)
            ping_reply.timestamp = datetime.now()
            await message.channel.send(embed=ping_reply)

        await self.process_commands(message)

def main():

    """Cache static data"""
    cache_reply = cache_manager.cache_data()
    print(cache_reply)

    """Load Mongo Manager"""
    db_reply = mongo_manager.init_mongo()
    print(db_reply)

    """Load Prefix and timer values"""
    prefix, timer, max = general_helper.get_prefix_timer_max()

    config.modify_prefix_timer_max(prefix, int(timer), int(max))

    try:
        bot = PokeCol(config.PREFIX)
        bot.run(TOKEN)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()