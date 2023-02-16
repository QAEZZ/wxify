import discord
from discord.ext import commands


"""
WXify help
    help                        :   Shows this
    info                        :   Shows information about the client
    latency                     :   Replies with the latency of the client
"""


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def help(self, ctx, switch: str = None):
        try:

            embed: discord.Embed = discord.Embed(
                title="WXify Help", description="```<required>\n[optional]\n\nTypes of parameters\nstr - all characters\ninteger - numbers only\nbool - true/false```", color=self.eColor)

            embed.add_field(name="help", value="```Shows this```", inline=True)
            embed.add_field(name="latency", value="```Replies with the latency of the client```", inline=True)
            embed.add_field(name="info", value="```Shows information about the client```", inline=True)

            await ctx.reply(embed=embed)

        except Exception as e:
            embed: discord.Embed = discord.Embed(
                title=f"``{e}``", color=discord.Color.from_rgb(255, 100, 100)
            )
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))
