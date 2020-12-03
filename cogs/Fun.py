import discord
from discord.ext import commands
import requests
import json
from utility import colors
from winter import cur_date, cur_time

class Fun(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def dailyfact(self, ctx):
        data = requests.get(url="https://uselessfacts.jsph.pl/today.json?language=en")
        x = json.loads(data.content)
        y = x["text"]
        embed = discord.Embed(
            title = "Fact of the day",
            description = f"``{y}``",
            color = colors.randomcolor()
        )
        embed.set_thumbnail(url="https://media.tenor.com/images/e00e9e6879fa0bfeb4c5012e4a95d3d0/tenor.gif")
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
        await ctx.send(embed=embed)

    @commands.command()
    async def randomfact(self, ctx):
        data = requests.get(url="https://uselessfacts.jsph.pl/random.json?language=en")
        x = json.loads(data.content)
        y = x["text"]
        embed = discord.Embed(
            title = "A random fact",
            description = f"``{y}``",
            color = colors.randomcolor()
        )
        embed.set_thumbnail(url="https://media.tenor.com/images/e00e9e6879fa0bfeb4c5012e4a95d3d0/tenor.gif")
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))