import discord
from discord.ext import commands


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def info(self, ctx, switch: str = None):
        try:

            embed: discord.Embed = discord.Embed(
                title="☁️ About Me", description="```Stay informed about the weather with WXify!\nThe all-in-one Discord client for weather updates, forecasts, and alerts. Get real-time weather conditions for any location, hourly and daily forecasts. WXify makes it easy to stay on top of the weather, no matter where you are in the world.```", color=self.eColor)

            embed.add_field(name="Language", value="> ```Python```", inline=True)
            embed.add_field(name="Wrapper", value="> ```discord.py (2.0)```", inline=True)
            embed.add_field(name="License", value="> ```MIT License```", inline=True)
            embed.add_field(name="GitHub*", value="> [```github/QAEZZ```](https://github.com/qaezz)", inline=True)
            embed.add_field(name="GitHub Repo*", value="> [```QAEZZ/wxify```](https://github.com/qaezz/wxify)", inline=True)
            embed.add_field(name="Creator", value="> ```Some Guy#2451```", inline=True)
            embed.set_footer(text="* value is a hyperlink (clickable)")

            await ctx.reply(embed=embed)

        except Exception as e:
            embed: discord.Embed = discord.Embed(
                title=f"``{e}``", color=discord.Color.from_rgb(255, 100, 100)
            )
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Info(bot))
