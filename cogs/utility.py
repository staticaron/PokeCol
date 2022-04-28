from discord.ext import commands

class UtilityCog(commands.Cog):

    @commands.command(name="ping", description="Returns the bot's latency")
    async def ping(self, ctx:commands.Context):
        await ctx.send(f"Bot's Latency : **{round(ctx.bot.latency * 1000, 2)} ms**")


def setup(bot:commands.Bot):
    bot.add_cog(UtilityCog())