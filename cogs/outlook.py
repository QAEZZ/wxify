import discord
from discord.ext import commands
import requests 
from bs4 import BeautifulSoup

def getdata(url): 
    r = requests.get(url) 
    return r.text 


class Outlook(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def outlook(self, ctx, day):
        try:
            try:
                day = int(day)
            except ValueError:
                await ctx.reply("Please give an integer thats not greater than 3! (1-3)")
                return
            if day > 3 or day == 0:
                await ctx.reply("Please give an integer thats not greater than 3! (1-3)")
            else:
                htmldata = getdata(f"https://www.spc.noaa.gov/products/outlook/day{day}otlk.html") 
                soup = BeautifulSoup(htmldata, 'html.parser')
                tds = soup.find_all('td', class_="rpttext")

                htmldata = str(tds[0])

                soup = BeautifulSoup(htmldata, 'html.parser')

                anchors = soup.find_all('a', href=True)

                for value in anchors:
                    if "Print Version" in value:
                        url = f"https://www.spc.noaa.gov/products/outlook/{value['href']}"
                        htmldata = getdata(url)
                        soup = BeautifulSoup(htmldata, 'html.parser')
                        imgs = soup.find_all('img')
                        embed_list = []


                        for i in imgs:
                            if "gif" in str(i):
                                image_url = f"https://www.spc.noaa.gov/products/outlook/{i['src']}"

                                embed: discord.Embed = discord.Embed(
                                    title=f"Day {day} Convective Outlook", color=self.eColor, url=f"https://www.spc.noaa.gov/products/outlook/day{day}otlk.html"
                                )
                                
                                embed.set_image(url=image_url)

                                embed_list.append(embed)
                        
                        await ctx.reply(embeds=embed_list)
            

        except Exception as e:
            embed: discord.Embed = discord.Embed(
                title=f"``{e}``", color=discord.Color.from_rgb(255, 100, 100)
            )
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Outlook(bot))
