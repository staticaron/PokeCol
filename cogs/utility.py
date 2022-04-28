from discord.ext import commands
from discord import Member

from managers import mongo_manager
from config import SERVER_COL_NAME
import config

class UtilityCog(commands.Cog):

    @commands.command(name="ping", description="Returns the bot's latency")
    async def ping(self, ctx:commands.Context):
        await ctx.send(f"Bot's Latency : **{round(ctx.bot.latency * 1000, 2)} ms**")

    @commands.command(name="prefix", description="Sets the prefix of the bot")
    async def prefix(self, ctx:commands.Context, prefix:str=None):

        if prefix is None:
            return await ctx.reply(f"Current Prefix is {config.PREFIX}")

        try:
            if not ctx.author.guild_permissions.administrator:
                return await ctx.reply("You need administrator privilages to update the guild prefix.")

            updated_data = {"prefix" : prefix}

            mongo_manager.manager.update_all_data(SERVER_COL_NAME, {}, updated_data)
            config.modify_prefix_timer_max(prefix=prefix, timer=None, max=None)

            return await ctx.reply(f"Prefix changed to **{prefix}**")
        except Exception as e:
            return await ctx.reply(f"Error occured while changing the prefix. \n```{e}```")

    @commands.command(name="max", description="Sets the max collection size limit")
    async def max(self, ctx:commands.Context, max:int=None):
        
        if max is None:
            return await ctx.reply(f"Maximum Collection Size is **{config.MAX}**")

        try:
            if not ctx.author.guild_permissions.administrator:
                return await ctx.reply("You need administrator privilages to update collection max.")

            updated_data = {"max" : max}

            mongo_manager.manager.update_all_data(SERVER_COL_NAME, {}, updated_data)
            config.modify_prefix_timer_max(prefix=None, timer=None, max=int(max))

            return await ctx.reply(f"New Collection Max is set to **{max}**")
        except Exception as e:
            await ctx.reply(f"Error occured while trying to update the collection max. \n```{e}```")

def setup(bot:commands.Bot):
    bot.add_cog(UtilityCog())