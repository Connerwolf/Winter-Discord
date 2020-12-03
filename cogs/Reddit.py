from winter import cur_time
import discord
from discord.ext import commands
from utility import reddit_api, colors

class Reddit(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reddit(self, ctx, query):
        try:
            get = reddit_api.praw_get(query)
            embed = discord.Embed(
                title = f"``Title :`` {get.title}",
                color = colors.randomcolor()
            )
            embed.set_image(url=get.url)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Ups: {get.ups} || Credits: Reddit")
            await ctx.send(embed=embed)
        except Exception:
            emote = "<:error:779707707552038932>"
            embed = discord.Embed(
                title = f"{emote} Error",
                description = "``Result :`` No Results Found",
                color = colors.randomcolor()
            )
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Timestamp: {cur_time}")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Reddit(client))