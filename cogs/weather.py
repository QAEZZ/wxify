import discord
from discord.ext import commands
import requests
import json


"""
WMO Weather interpretation codes (WW)
Code 	        Description
0 	            Clear sky
1, 2, 3 	    Mainly clear, partly cloudy, and overcast
45, 48 	        Fog and depositing rime fog
51, 53, 55 	    Drizzle: Light, moderate, and dense intensity
56, 57 	        Freezing Drizzle: Light and dense intensity
61, 63, 65 	    Rain: Slight, moderate and heavy intensity
66, 67 	        Freezing Rain: Light and heavy intensity
71, 73, 75 	    Snow fall: Slight, moderate, and heavy intensity
77 	            Snow grains
80, 81, 82 	    Rain showers: Slight, moderate, and violent
85, 86 	        Snow showers slight and heavy
95 * 	        Thunderstorm: Slight or moderate
96, 99 * 	    Thunderstorm with slight and heavy hail

(*) Thunderstorm forecast with hail is only available in Central Europe
"""

    
def wwcheck(ww_code = "MISSING"):
    ww_code = ww_code
    if ww_code == "MISSING":
        return f"ww_code is MISSING"

    with open("cogs/ww.json", "r") as f:
        data = json.loads(f.read())
        if data[str(ww_code)]:
            return f"(ww {ww_code}) {data[str(ww_code)]}"
        else:
            return "not found!"
        


class Weather(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def weather(self, ctx, *, place = "chicago"):
        try:
            f = open("./keys/geocode.key", "r")
            api_key = f.read()
            url = f"https://api.geoapify.com/v1/geocode/search?text={place}&apiKey={api_key}"

            response = requests.get(url)

            if response.status_code == requests.codes.ok:
                data = json.loads(response.content)

                lat = data['features'][0]['properties']['lat']
                lng = data['features'][0]['properties']['lon']
                
                result_type = data['features'][0]['properties']['result_type']

                if result_type == "country":
                    country = data['features'][0]['properties']['country']
                    city = ""
                    state = ""
                elif result_type == "amenity":
                    city = f"{data['features'][0]['properties']['city']}, "
                    country = data['features'][0]['properties']['country']
                    state = f"{data['features'][0]['properties']['district']}, "
                elif result_type == "city" or result_type == "district":
                    city = f"{data['features'][0]['properties']['city']}, "
                    country = data['features'][0]['properties']['country']
                    if "state" in data['features'][0]['properties']:
                        state = f"{data['features'][0]['properties']['state']}, "
                    else:
                        state = ""
                elif result_type == "state":
                    city = ""
                    country = data['features'][0]['properties']['country']
                    state = f"{data['features'][0]['properties']['state']}, "
                else:
                    await ctx.reply(f"**Please DM `Some Guy#2451` with the `result_type`, `result_type` = `{result_type}`**")


                weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=kn&precipitation_unit=inch&timezone=GMT"

                resp = requests.get(weather_url)
                d = resp.content
                wdata = json.loads(d)


                elevation = wdata["elevation"] # meters above sea level

                current_temperature = wdata["current_weather"]["temperature"]
                current_windspeed = wdata["current_weather"]["windspeed"] # knots
                current_winddirection = wdata["current_weather"]["winddirection"]
                current_weathercode = wdata["current_weather"]["weathercode"]

                desc = f"""
**Temperature:**
> ``{round(current_temperature)}°F | {round((current_temperature - 32)*.5556)}°C``
**Wind:**
> ``{round(current_winddirection)}° @ {round(current_windspeed)} kn | {round(current_windspeed * 1.151)} mph | {round(current_windspeed * 1.852)} kmh``
**Elevation:**
> ``{elevation:.0f} meters``
**Current Conditions:**
> ``{wwcheck(current_weathercode)}``"""

                # subtract 32 and multiply by .5556
                embed: discord.Embed = discord.Embed(
                        title = f"Current Weather in {city}{state}{country}\n({lat}, {lng})", description = desc, color=self.eColor
                        )
                await ctx.reply(embed=embed)
                
            else:
                embed: discord.Embed = discord.Embed(
                        title=f"{response.status_code} (Geocoding)", description = f"```{response.text}```", color = discord.Color.from_rgb(250, 100, 100)
                        )
                await ctx.reply(embed=embed)
        except Exception as e:
            embed: discord.Embed = discord.Embed(
                    description = f"**``{e}``**", color = discord.Color.from_rgb(250, 100, 100)
                    )
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Weather(bot))

"""
WMO Weather interpretation codes (WW)
Code 	        Description
0 	            Clear sky
1, 2, 3 	    Mainly clear, partly cloudy, and overcast
45, 48 	        Fog and depositing rime fog
51, 53, 55 	    Drizzle: Light, moderate, and dense intensity
56, 57 	        Freezing Drizzle: Light and dense intensity
61, 63, 65 	    Rain: Slight, moderate and heavy intensity
66, 67 	        Freezing Rain: Light and heavy intensity
71, 73, 75 	    Snow fall: Slight, moderate, and heavy intensity
77 	            Snow grains
80, 81, 82 	    Rain showers: Slight, moderate, and violent
85, 86 	        Snow showers slight and heavy
95 * 	        Thunderstorm: Slight or moderate
96, 99 * 	    Thunderstorm with slight and heavy hail

(*) Thunderstorm forecast with hail is only available in Central Europe
"""
