from discord.ext import commands

from helpers import collection_helper

class CollectionCog(commands.Cog):

    @commands.group(name="col")
    async def col(self, ctx:commands.Context):
        if ctx.subcommand_passed == None:
            await ctx.reply("Please provide a valid sub command")

    """Add Pokemons to your collection"""

    @col.command(name="add", description="Adds a pokemons to your collection")
    async def add(self, ctx:commands.Context, pokemon:str):
        
        reply = await collection_helper.register_collection(ctx.author, pokemon)

        await ctx.reply(reply)

    """Remove Pokemons from your collection"""

    @col.command(name="remove", description="Removes a pokemon from your collection")
    async def remove(self, ctx:commands.Context, pokemon:str):

        reply = await collection_helper.remove_pokemon(ctx.author, pokemon)

        await ctx.reply(reply)

    """View your collection list"""

    @col.command(name="show", description="View your collection")
    async def show(self, ctx:commands.Context):

        reply = await collection_helper.get_collection(ctx.author)

        if reply is None:
            await ctx.reply(f"You don't have collections, add pokemons to your collection using ```{ctx.prefix}col add pokemon```")
        else:
            await reply.send(ctx)

    @commands.command(name="cp", description="Pings the collector of a specific pokemon")
    async def collector_ping(self, ctx:commands.Context, pokemon:str):

        reply = await collection_helper.get_collector_pings(pokemon)

        await ctx.send(reply)

def setup(bot:commands.Bot):
    bot.add_cog(CollectionCog())