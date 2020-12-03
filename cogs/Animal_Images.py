import discord
from discord.ext import commands
from utility import reddit_api, colors

class Animal_Images(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cat(self, ctx):
        get = reddit_api.praw_get("catpictures")
        embed = discord.Embed(
                title = f"``Title :`` {get.title}",
                color = colors.randomcolor()
            )
        embed.set_image(url=get.url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Ups: {get.ups} || Credits: Reddit")
        await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        get = reddit_api.praw_get("dogpictures")
        embed = discord.Embed(
                title = f"``Title :`` {get.title}",
                color = colors.randomcolor()
            )
        embed.set_image(url=get.url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Ups: {get.ups} || Credits: Reddit")
        await ctx.send(embed=embed)
            

def setup(client):
    client.add_cog(Animal_Images(client))