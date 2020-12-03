from random import random
import discord
from discord.ext import commands
from utility import reddit_api, colors

class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        get = reddit_api.praw_get("meme")
        embed = discord.Embed(
            title = f"``Title :`` {get.title}",
            color = colors.randomcolor()
        )
        embed.set_image(url=get.url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Ups: {get.ups} || Credits: Reddit")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Meme(client))