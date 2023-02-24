import discord
from discord.ext import commands


class Credits(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def credits(self, ctx, switch: str = None):
        try:
            desc = f"""**__APIs:__**
> **[open-meteo](https://open-meteo.com/)**
> **⤷** *Used to obtain weather data.*
> 
> **[geoapify](https://geoapify.com)**
> **⤷** *Used to geocode the location to lat/lng.*
> 
> **[tomorrow](https://docs.tomorrow.io/reference/data-layers-weather-codes)**
> **⤷** *Used for the weather icons.*

**__Other Resources:__**
> **[WMO CODE TABLE 4677](https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM)**
> **⤷** *Used to translate the weather code from [open-meteo](https://open-meteo.com/).*
"""

            embed: discord.Embed = discord.Embed(
                title="☁️ Credits", description=desc, color=self.eColor)

            await ctx.reply(embed=embed)

        except Exception as e:
            embed: discord.Embed = discord.Embed(
                title=f"``{e}``", color=discord.Color.from_rgb(255, 100, 100)
            )
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Credits(bot))
