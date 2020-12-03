from os import execle
import discord
from discord.ext import commands
from winter import cur_date, cur_time, ping, uptime, version

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def stats(self,ctx):
        user = await self.client.fetch_user(450223497021489163)
        stats = discord.Embed(
            title = ":desktop: Status",
            description = f":satellite: ``Ping :`` **{ping()}** \n :alarm_clock: ``Uptime :`` **{uptime()}** \n :keyboard: ``Version :`` **{version()}**\n\n:keyboard: ``Developer`` : **{user}**",
            color = discord.Color.green()
        )
        stats.set_thumbnail(url=self.client.user.avatar_url)
        stats.set_footer(text=f"Timestamp: {cur_time()} || {cur_date()}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=stats)

def setup(client):
    client.add_cog(Utility(client))

