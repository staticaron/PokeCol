from discord.ext import commands

from helpers import collection_helper

class CollectionCog(commands.Cog):

    @commands.group(name="col")
    async def col(self, ctx:commands.Context):
        if ctx.subcommand_passed == None:
            await ctx.reply("Please provide a valid sub command")

    @col.command(name="add", description="Add Pokemons to your collection")
    async def add(self, ctx:commands.Context, pokemon:str):
        
        reply = await collection_helper.register_collection(ctx.author, pokemon)

        await ctx.reply(reply)


def setup(bot:commands.Bot):
    bot.add_cog(CollectionCog())