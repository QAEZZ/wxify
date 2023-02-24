import discord
from discord.ext import commands


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def info(self, ctx, switch: str = None):
        try:

            desc = f"""```Stay informed about the weather with WXify!\nThe all-in-one Discord client for weather updates, forecasts (kinda™), and alerts (soon™). Get real-time weather conditions for any location, hourly (soon™) and daily (soon™) forecasts. WXify makes it easy to stay on top of the weather, no matter where you are in the world.```
**__Information:__**
> **Language**
> **⤷** *[Python](https://python.org)* <:pythonlang:1014273896192671764>
> 
> **Wrapper**
> **⤷** *[discord.py (2.0)](https://github.com/Rapptz/discord.py)* <:discordpy:1077966607067906128>
> 
> **License**
> **⤷** *[MIT](https://opensource.org/license/mit/)* <:mitlicense:1077967201832812634>
> 
> **GitHub**
> **⤷** *[github/QAEZZ](https://github.com/qaezz)* <:github:1077967551360933919>
> 
> **GitHub Repository**
> **⤷** *[QAEZZ/wxify](https://github.com/qaezz/wxify)* <:github:1077967551360933919>
> 
> **Creator**
> **⤷** *Some Guy#2451* <:discord:1077968045789696010>
"""

            embed: discord.Embed = discord.Embed(
                title="☁️ About Me", description=desc, color=self.eColor)
            
            embed.set_footer(text="This bot is still in development, expect bugs.")

            await ctx.reply(embed=embed)

        except Exception as e:
            embed: discord.Embed = discord.Embed(
                title=f"``{e}``", color=discord.Color.from_rgb(255, 100, 100)
            )
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Info(bot))
