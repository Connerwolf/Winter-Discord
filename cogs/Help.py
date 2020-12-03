import discord
from winter import cur_time, cur_date
from discord import client
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    def check(ctx, user):
        return user.id == ctx.author.id 

    @commands.command()
    async def help(self, ctx, *, category=None):
        if category == None:
            embed = discord.Embed(
                title = ':ledger: Help Menu',
                description = ":tv: ``Media Commands`` : **$help media**\n:hammer_pick: ``Moderation Commands`` : **$help moderation**\n:piñata: ``Fun commands``: **$help fun**\n:wrench: ``Utility Commands`` : **$help utility**\n\n:robot: **Bot Help**\n\n:calling: ``Bot Invite`` : **$invite**\n:envelope_with_arrow: ``Bot Support`` : **$support**",
                color = discord.Color.green()
            )
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed)

        elif category == "media":
            embed = discord.Embed(
                title = '<:media:779953770154819605> Media Commands',
                description = "``$meme`` : **Returns a Meme**\n``$dog`` : **Returns a Dog Image**\n``$cat`` : **Returns a Cat Image**\n``$reddit`` : **Returns the results from Reddit [Beta/Buggy]**\n__Usage__ :  **$reddit <query>**\n``$gif`` : Returns a gif\n__Usage__ : **$gif <query>**",
                color = discord.Color.green()
            )
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed)

        elif category == "moderation":
            embed = discord.Embed(
                title = '<:admin:779954884719018004> Moderation Commands',
                description = "``$kick`` : **Kicks the User from the Server**\n__Usage__ : **$kick <user>**\n``$ban`` : **Bans the User from the Server**\n__Usage__ : **$ban <user>**\n``$unban`` : **Unbans User from the Server**\n__Usage__ : **$unban <user's id>**\n``$mute`` : **Mutes the user**\n__Usage__ : **$mute <time in mins> <user>**\n``$unmute`` : **Unmutes the user from the Server**\n__Usage__ : **$unmute <user>**\n``$clear`` : **Clears a number of messages from said channel [default 10]**\n__Usage__ : **$clear <amount>**",
                color = discord.Color.green()
            )
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed)

        elif category == "fun":
            embed = discord.Embed(
                title = '<:fun:779957833902456843> Fun Commands',
                description = "``$slap`` : **Slaps you or the mentioned user**\n__Usage__ : **slap <user> [slaps you if none mentioned]**\n``$randomfact`` : **Returns a random useless fact**\n``$dailyfact`` : **Returns the useless fact of the day**",
                color = discord.Color.green()
            )
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed)   

        elif category == "utility":
            embed = discord.Embed(
                title = '<:utility:779959486638981141> Utility Commands',
                description = "``$stats`` : **Returns bot status**\n``$server`` : **Posts user join-leave logs**\n__Usage__ : **$server <enable/disable> memberlog <True> [if u want channel private]**",
                color = discord.Color.green()
            )
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed) 

    @commands.command()
    async def invite(self, ctx):
        await ctx.send("**Link** : https://discord.com/oauth2/authorize?client_id=586553956843388942&scope=bot&permissions=8")

    @commands.command()
    async def support(self, ctx):
        await ctx.send("**Link** : https://discord.gg/zAhDxAVTXu")

def setup(client):
    client.add_cog(Help(client))