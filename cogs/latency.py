import discord
from discord.ext import commands


class Latency(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def latency(self, ctx):
        embed: discord.Embed = discord.Embed(
            title=f"Ping: {round(self.bot.latency*1000)}ms", color=self.eColor
        )
        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Latency(bot))
