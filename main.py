#!/usr/bin/env python3

import discord
import sys
import os
import asyncio
import time

from discord.ext import commands


class wxify(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix="wx/",
            intents=discord.Intents.all(),
            application_id="1075850206639292506",
            help_command=None,
            activity=discord.Game("with weather...")
        )

    async def on_ready(self):
        self.remove_command("help")
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                print(f"found {filename}")
                await client.load_extension(f"cogs.{filename[:-3]}")
                print(f"loaded {filename}")

        print(f"logged in as {self.user}\nI am in {len(client.guilds)} server(s)!\n\ndiscord.py == {discord.__version__}\npython == {sys.version}\n\n")


client = wxify()

modList = [755115465038233630]


def checkID(ctx):
    if ctx.author.id in modList:
        return ctx.author.id in modList


@client.command()
@commands.check(checkID)
async def load(ctx, extension):
    try:
        if extension.lower() == "all":
            embed: discord.Embed = discord.Embed(
                title="Log",
                color=discord.Color.from_rgb(47, 49, 54)
            )
            msg = await ctx.reply(embed=embed)

            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):
                    print(f"found {filename}")
                    try:
                        await client.load_extension(f"cogs.{filename[:-3]}")
                        embed.add_field(name="✅", value=f"```Extension 'cogs.{filename[:-3]}' is loaded.```", inline=False)
                        time.sleep(1)
                        await msg.edit(embed=embed)
                    except Exception as e:
                        embed.add_field(name="⛔", value=f"```{e}```", inline=False)
                        time.sleep(1)
                        await msg.edit(embed=embed)
                    print(f"loaded {filename}")
            embed.set_footer(text="done.")
            await msg.edit(embed=embed)

        else:
            await client.load_extension(f'cogs.{extension}')
            message = await ctx.reply(f'__Loading:__ ``cogs.{extension}``')
            await message.edit(content=f'``cogs.{extension}`` __Was Successfully Loaded__')
            print(f'Loaded cogs.{extension}, {ctx.author}')
    except Exception as e:
        embed: discord.Embed = discord.Embed(
                title=f"``{e}``", color=discord.Color.from_rgb(255, 100, 100)
        )
        await ctx.reply(embed=embed)


@client.command()
@commands.check(checkID)
async def unload(ctx, extension):
    try:
        if extension.lower() == "all":
            embed: discord.Embed = discord.Embed(
                title="Log",
                color=discord.Color.from_rgb(47, 49, 54)
            )
            msg = await ctx.reply(embed=embed)

            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):
                    print(f"found {filename}")
                    try:
                        await client.unload_extension(f"cogs.{filename[:-3]}")
                        embed.add_field(name="✅", value=f"```Extension 'cogs.{filename[:-3]}' is unloaded.```", inline=False)
                        time.sleep(1)
                        await msg.edit(embed=embed)
                    except Exception as e:
                        embed.add_field(name="⛔", value=f"```{e}```", inline=False)
                        time.sleep(1)
                        await msg.edit(embed=embed)
                    print(f"loaded {filename}")
            embed.set_footer(text="done.")
            await msg.edit(embed=embed)

        else:
            await client.unload_extension(f'cogs.{extension}')
            message = await ctx.reply(f'__Unloading:__ ``cogs.{extension}``')
            await message.edit(content=f'``cogs.{extension}`` __Was Successfully Unloaded__')
            print(f'Unloaded cogs.{extension}, {ctx.author}')
    except Exception as e:
        embed: discord.Embed = discord.Embed(
                title=f"``{e}``", color=discord.Color.from_rgb(255, 100, 100)
        )
        await ctx.reply(embed=embed)


@client.command()
@commands.check(checkID)
async def reload(ctx, extension):
    try:
        if extension.lower() == "all":
            embed: discord.Embed = discord.Embed(
                title="Log",
                color=discord.Color.from_rgb(47, 49, 54)
            )
            msg = await ctx.reply(embed=embed)

            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):
                    print(f"found {filename}")
                    try:
                        await client.unload_extension(f'cogs.{filename[:-3]}')
                        await client.load_extension(f"cogs.{filename[:-3]}")
                        embed.add_field(name="✅", value=f"```Extension 'cogs.{filename[:-3]}' reloaded.```", inline=False)
                        time.sleep(1)
                        await msg.edit(embed=embed)
                    except Exception as e:
                        embed.add_field(name="⛔", value=f"```{e}```", inline=False)
                        time.sleep(1)
                        await msg.edit(embed=embed)
                    print(f"loaded {filename}")
            embed.set_footer(text="done.")
            await msg.edit(embed=embed)

        else:
            await client.unload_extension(f'cogs.{extension}')
            message = await ctx.reply(f'__Reloading:__ ``cogs.{extension}``')
            await client.load_extension(f'cogs.{extension}')
            await message.edit(content=f'``cogs.{extension}`` __Was Successfully Reloaded__')
            print(f'Reloaded cogs.{extension}, {ctx.author}')
    except Exception as e:
        embed: discord.Embed = discord.Embed(
                title=f"``{e}``", color=discord.Color.from_rgb(255, 100, 100)
        )
        await ctx.reply(embed=embed)


@client.command()
@commands.check(checkID)
async def kill(ctx):
    await ctx.reply("``Bot Dead`` \n ||<@755115465038233630>||")
    print(f'-------KILLED by, {ctx.author}-------')
    exit()


@client.command()
@commands.check(checkID)
async def lscogs(ctx):
    try:
        for filename in os.listdir('./cogs'):
            await ctx.send(f"``./{filename}``")
    except Exception as e:
        embed: discord.Embed = discord.Embed(
                title=f"``{e}``", color=discord.Color.from_rgb(255, 100, 100)
        )
        await ctx.reply(embed=embed)


@client.command()
@commands.check(checkID)
async def ls(ctx):
    try:
        for filename in os.listdir('./'):
            await ctx.send(f"``./{filename}``")
    except Exception as e:
        embed: discord.Embed = discord.Embed(
                title=f"``{e}``", color=discord.Color.from_rgb(255, 100, 100)
        )
        await ctx.reply(embed=embed)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed: discord.Embed = discord.Embed(
            title="Slow down!", description=f"{round(error.retry_after, 2)} seconds left", color=discord.Color.from_rgb(255, 100, 100)
        )
        await ctx.reply(embed=embed)


async def main():
    with open("./keys/token.key", "r") as f:
        TOKEN = f.read()

    await client.start(TOKEN)


asyncio.run(main())
