import discord
from discord.ext import commands
import requests
import datetime
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
            """
            match ww_code:
                case 0:
                    emoji = "https://files.readme.io/48b265b-weather_icon_small_ic_clear3x.png"
                case 1:
                    emoji = "https://files.readme.io/c3d2596-weather_icon_small_ic_mostly_clear3x.png"
                case 2:
                    emoji = "https://files.readme.io/5ef9011-weather_icon_small_ic_partly_cloudy3x.png"
                case 3:
                    emoji = "https://files.readme.io/4042728-weather_icon_small_ic_cloudy3x.png"
                case 45, 48:
                    emoji = "https://files.readme.io/8d37852-weather_icon_small_ic_fog3x.png"
                case 51, 53, 55:
                    emoji = "https://files.readme.io/f22e925-weather_icon_small_ic_rain_drizzle3x.png"
                case 56:
                    emoji = "https://files.readme.io/43b5585-weather_icon_small_ic_freezing_rain_drizzle3x.png"
                case 57:
                    emoji = "https://files.readme.io/9d1a4dc-weather_icon_small_ic_freezing_rain_light3x.png"
                case 61:
                    emoji = "https://files.readme.io/ea98852-weather_icon_small_ic_rain_light3x.png"
                case 63:
                    emoji = "https://files.readme.io/aab8713-weather_icon_small_ic_rain3x.png"
                case 65, 80, 81, 82:
                    emoji = "https://files.readme.io/fdacbb8-weather_icon_small_ic_rain_heavy3x.png"
                case 66:
                    emoji = "https://files.readme.io/321062d-weather_icon_small_ic_freezing_rain3x.png"
                case 67:
                    emoji = "https://files.readme.io/2f614b7-weather_icon_small_ic_freezing_rain_heavy3x.png"
                case 71:
                    emoji = "https://files.readme.io/c736bc9-weather_icon_small_ic_snow_light3x.png"
                case 73, 85:
                    emoji = "https://files.readme.io/731a898-weather_icon_small_ic_snow3x.png"
                case 75, 86:
                    emoji = "https://files.readme.io/20c73b9-weather_icon_small_ic_snow_heavy3x.png"
                case 77:
                    emoji = "https://files.readme.io/8cde587-weather_icon_small_ic_ice_pellets_light3x.png"
                case 95, 96, 99:
                    emoji = "https://files.readme.io/39fb806-weather_icon_small_ic_tstorm3x.png"
                case _:
                    emoji = "MISSING"
            """
            desc = data[str(ww_code)]
            if ww_code == 0:
                emoji = "https://files.readme.io/48b265b-weather_icon_small_ic_clear3x.png"
            elif ww_code == 1:
                emoji = "https://files.readme.io/c3d2596-weather_icon_small_ic_mostly_clear3x.png"
            elif ww_code == 2:
                emoji = "https://files.readme.io/5ef9011-weather_icon_small_ic_partly_cloudy3x.png"
            elif ww_code == 3:
                emoji = "https://files.readme.io/4042728-weather_icon_small_ic_cloudy3x.png"
            elif "drizzle" in desc.lower():
                emoji = "https://files.readme.io/f22e925-weather_icon_small_ic_rain_drizzle3x.png"
            elif "snow" or "snowflakes" in desc.lower():
                emoji = "https://files.readme.io/731a898-weather_icon_small_ic_snow3x.png"
            elif "rain" or "shower" in desc.lower():
                emoji = "https://files.readme.io/aab8713-weather_icon_small_ic_rain3x.png"
            elif "fog" or "haze" or "mist" or "dust" or "sand" in desc.lower():
                emoji = "https://files.readme.io/8d37852-weather_icon_small_ic_fog3x.png"
            elif "thunderstorm" in desc.lower():
                emoji = "https://files.readme.io/39fb806-weather_icon_small_ic_tstorm3x.png"

            info = [f"(ww {ww_code}) {desc}", emoji]
            return info
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


                weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&hourly=relativehumidity_2m&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=kn&precipitation_unit=inch&timezone=GMT"

                resp = requests.get(weather_url)
                d = resp.content
                wdata = json.loads(d)


                elevation = wdata["elevation"] # meters above sea level

                current_temperature = wdata["current_weather"]["temperature"]
                current_windspeed = wdata["current_weather"]["windspeed"] # knots
                current_winddirection = wdata["current_weather"]["winddirection"]
                current_weathercode = wdata["current_weather"]["weathercode"]
                current_time = wdata["current_weather"]["time"]

                conditions = wwcheck(current_weathercode)
                conditions_str = conditions[0]
                conditions_emoji = conditions[1]

                counter = 0
                for i in wdata["hourly"]["time"]:
                    if i == current_time:
                        current_hour_key = counter
                    counter += 1
                
                current_humidity = wdata["hourly"]["relativehumidity_2m"][current_hour_key]


                desc = f"""
**Temperature:**
> ``{round(current_temperature)}°F | {round((current_temperature - 32)*.5556)}°C``
**Wind:**
> ``{round(current_winddirection)}° @ {round(current_windspeed)} kn | {round(current_windspeed * 1.151)} mph | {round(current_windspeed * 1.852)} kmh``
**Humidity:**
> ``{current_humidity}%``
**Elevation:**
> ``{elevation:.0f} meters``
**Current Conditions:**
> ``{conditions_str}``"""


                embed: discord.Embed = discord.Embed(
                        title = f"Current Weather in {city}{state}{country}\n({lat}, {lng})", description = desc, color=self.eColor, url=weather_url
                        )
                if conditions_emoji is not "MISSING":
                    embed.set_thumbnail(url=conditions_emoji)
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
