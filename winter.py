import discord
from discord.ext import commands
import json
import time
from datetime import date, timedelta

# Config

with open("./setup/bot_config.json") as c:
    config = json.load(c)

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=config["prefix"],owner_id=config["id"], intents=intents)
client.remove_command("help")
start_time = time.time()

# Functions

def cur_time():
    t = time.localtime()
    n = time.strftime("%I:%H:%S %p",t)
    return n

def cur_date():
    today = date.today()
    return today

def cur_activity(name,mode):
    if mode == "watching":
        watching = discord.ActivityType.watching
        activity = discord.Activity(name=name, type=watching)
        return activity

    elif mode == "playing":
        playing = discord.ActivityType.playing
        activity = discord.Activity(name=name, type=playing)
        return activity

def cur_guilds():
    i = len(client.guilds)
    return i

def ping():
    l = round(client.latency*100)
    res = f"{l}ms"
    return res

def uptime():
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(timedelta(seconds=difference))
    return text

def version():
    v = config["version"]
    return v

# Login

@client.event
async def on_ready():
    me = await client.fetch_user(config["id"])
    print(f"Logged in at {cur_time()}")
    await me.send(f"``` Client Booted || No Error \n Time: {cur_time()} \n Date: {cur_date()}```")
    await client.change_presence(activity=cur_activity(f"$help | {cur_guilds()} Guilds","watching"))

# Kill Switch

@client.command()
@commands.is_owner()
async def kill(ctx):
    embed = discord.Embed()
    await ctx.send(embed=embed)

# Custom Activity

@client.command()
@commands.is_owner()
async def activity(ctx, content=None, type=None):
    if content and type != None:
        await client.change_presence(activity=cur_activity(content, type))

    elif content == "default":
        await client.change_presence(activity=cur_activity(f"$help | {cur_guilds()} Guilds","watching"))

    elif content == "None" and type == None:
        await ctx.send("Content and Type are required.")
     

# Cog Pre-Loader

initial_extensions = [
                        'cogs.Utility',
                        'cogs.Reddit',
                        'cogs.Meme',
                        'cogs.Animal_Images',
                        'cogs.Gif',
                        'cogs.Support',
                        'cogs.Errors',
                        'cogs.Wiki',
                        'cogs.Mod',
                        'cogs.Help',
                        'cogs.Fun',
                    ]

for extension in initial_extensions:
    client.load_extension(extension)

# Cog Manual Control

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    cog = f"cogs.{extension}"
    try:
        client.load_extension(cog)
        embed = discord.Embed(
            title = ":gear:  Cogs",
            description = f"``Loaded :`` **{extension}**",
            color = discord.Color.red()
        )
        await ctx.send(embed=embed)
    except Exception:
        if cog in initial_extensions:
            embed = discord.Embed(
                title = ":desktop:  Error",
                description = f"``Reason :`` **Cog {extension} is already loaded.**",
                color = discord.Color.green()
            )
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                title = ":desktop:  Error",
                description = f"``Reason :`` **Invalid Cog {extension}.**",
                color = discord.Color.green()
            )
            await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    cog = f"cogs.{extension}"
    try:
        client.unload_extension(cog)
        embed = discord.Embed(
            title = ":gear:  Cogs",
            description = f"``Unloaded :`` **{extension}**",
            color = discord.Color.red()
        )
        await ctx.send(embed=embed)
    except Exception:
        if cog in initial_extensions:
            embed = discord.Embed(
                title = ":desktop:  Error",
                description = f"``Reason :`` **Cog {extension} is not loaded.**",
                color = discord.Color.green()
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title = ":desktop:  Error",
                description = f"``Reason :`` **Invalid Cog {extension}.**",
                color = discord.Color.green()
            )
            await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    cog = f"cogs.{extension}"
    try:
        client.unload_extension(cog)
        client.load_extension(cog)
        embed = discord.Embed(
            title = ":gear:  Cogs",
            description = f"``Reloaded :`` **{extension}**",
            color = discord.Color.red()
        )
        await ctx.send(embed=embed)
    except Exception:
        if cog in initial_extensions:
            embed = discord.Embed(
                title = ":desktop:  Error",
                description = f"``Reason :`` **Cog {extension} is failed to reloaded.**",
                color = discord.Color.green()
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title = ":desktop:  Error",
                description = f"``Reason :`` **Invalid Cog {extension}.**",
                color = discord.Color.green()
            )
            await ctx.send(embed=embed)

client.run(config["token"])