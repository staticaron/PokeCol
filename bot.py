from discord.ext import commands
from discord import Intents

from config import TOKEN

def get_command_prefix(bot, message):
    return [">"]

class PokeCol(commands.Bot):

    intents:Intents = Intents.default()
    intents.message_content = True
    intents.members = True
    intents.presences = True

    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(">"), case_insensitive=True, description="An easy-to-use, self hosted collection bot for pokemon players on discord.", intents=self.intents)

    async def on_ready(self):
        print("Logged in as {}".format(self.user))

def main():

    try:
        bot = PokeCol()
        bot.run(TOKEN)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()