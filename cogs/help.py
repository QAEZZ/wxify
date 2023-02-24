import discord
from discord.ext import commands


"""
WXify help
    help                        :   Shows this
    info                        :   Shows information about the client
    latency                     :   Replies with the latency of the client
    outlook <day: int>          :   Shows SPC's day X outlook
    weather <place: str>        :   Shows current weather for the specified place
"""


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def help(self, ctx, switch: str = None):
        try:
            desc = f"""**<required>**
**[optional]**

**__Types of parameters:__**
> **str** - all characters
> **int** - numbers only
> **bool** - true/false

**__Commands:__**
> **help**
> **⤷** *Shows this.*
> 
> **info**
> **⤷** *Shows information about the client.*
> 
> **credits**
> **⤷** *Shows APIs and resources the client uses.*
> 
> **latency**
> **⤷** *Replies with the latency of the client.*
> 
> **outlook <day: int>**
> **⤷** *Shows SPC's day X outlook
>   Ex. wx/outlook 1*
> 
> **weather [place: str] (Default location is Chicago)**
> **⤷** *Shows current weather for the specified place.
>   Ex. wx/weather new york city*
"""

            embed: discord.Embed = discord.Embed( # ⤷
                title="☁️ Help", description=desc, color=self.eColor)

            await ctx.reply(embed=embed)

        except Exception as e:
            embed: discord.Embed = discord.Embed(
                title=f"``{e}``", color=discord.Color.from_rgb(255, 100, 100)
            )
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))
