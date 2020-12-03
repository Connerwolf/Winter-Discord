import discord
from cogs import Gif
from discord.ext import commands
from utility.wiki_api import wiki, wiki_suggest
from utility.tenor_api import tenor

class Wiki(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def wiki(self, ctx, *,search):
        emote = "<:error:779707707552038932>"
        try:
            data = wiki(search=search,lenght=1)
            if data != None:
                embed = discord.Embed(
                    title = f"``Result :`` {search}",
                    description = f"**{data}**",
                    color = discord.Colour.gold()
                )
                embed.set_thumbnail(url=tenor(search))
                await ctx.send(embed=embed)
            else:
                data = wiki_suggest(search=search)
                embed = discord.Embed(
                    title = f"{emote} No Match Found",
                    description = f"**Suggestion :** ___{data}___",
                    color = discord.Colour.gold()
                )
                embed.set_thumbnail(url='https://cdn.dribbble.com/users/1880522/screenshots/7117744/media/79c3c0f284c29d12ee50405f11c930f5.gif')
                await ctx.send(embed=embed)
        except Exception as e:
            print(f"Error:{e}")

def setup(client):
    client.add_cog(Wiki(client))
