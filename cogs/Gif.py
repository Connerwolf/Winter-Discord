import discord
import random
from utility.colors import randomcolor
from utility.tenor_api import tenor
from discord.ext import commands
from winter import cur_time, cur_date


class Gif(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gif(self, ctx, *,query):
        img = tenor(query)
        embed = discord.Embed(
            title = f"``Result:`` {query}",
            color = randomcolor()
        )
        embed.set_image(url=img)
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
        await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, user:discord.Member=None):
        img = tenor("animeslap")
        if user == None:
            embed = discord.Embed(
                title = f"{ctx.author.name} slapped themself",
                color = randomcolor()
            )
            embed.set_image(url=img)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                title = f"{ctx.author.name} slapped {user.name}",
                color = randomcolor()
            )
            embed.set_image(url=img)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Gif(client))

