from os import name
import discord
import asyncio
from discord import guild
from discord.ext import commands
from winter import cur_date, cur_time

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["k"])
    @commands.has_permissions()
    async def kick(self, ctx, member: discord.Member=None, *, reason=None):
        if not member:
            embed = discord.Embed(
                title = ':gear: Error',
                description = f'``Reason :`` **Member is an required argument.**',
                color = discord.Color.green()
            )
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
            title = f':boot: Kicked',
            description = f"``User :`` **{member}**\n``User ID :`` **{member.id}**\n``Moderator:`` **{ctx.author}**\n``Reason :`` **{reason}**",
            color = discord.Color.green()
            )
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await member.kick(reason=reason)
            await ctx.send(embed=embed) 
    
    @commands.command(aliases=["b"])
    @commands.has_permissions()
    async def ban(self, ctx, member: discord.Member=None, *, reason=None):
        if not member:
            embed = discord.Embed(
                title = ':gear: Error',
                description = f'``Reason :`` **Member is an required argument.**',
                color = discord.Color.green()
            )
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
            title = f':lock: Banned',
            description = f"``User :`` **{member}**\n``User ID :`` **{member.id}**\n``Moderator:`` **{ctx.author}**\n``Reason :`` **{reason}**",
            color = discord.Color.green()
            )
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await member.ban(reason=reason)
            await ctx.send(embed=embed)

    @commands.command(aliases=["ub"])
    @commands.has_permissions()
    async def unban(self, ctx, id:int=None, *, reason=None):
        if not id:
            embed = discord.Embed(
                title = ':gear: Error',
                description = f"``Reason :`` **Member's ID is an required argument.**",
                color = discord.Color.green()
            )
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed)
        else:
            member = await self.client.fetch_user(id)
            await ctx.guild.unban(member,reason=reason)
            embed = discord.Embed(
            title = f':unlock: Unbanned',
            description = f"``User :`` **{member}**\n``User ID :`` **{member.id}**\n``Moderator:`` **{ctx.author}**\n``Reason :`` **{reason}**",
            color = discord.Color.green()
            )
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed)

    @commands.command(aliases=['m'])
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member=None, mute_minutes=0, *,reason=None):
        for role in ctx.guild.roles:
            if "Muted" not in role:    
                try:
                    guild = ctx.guild
                    await guild.create_role(name="Muted")
                    role = discord.utils.get(ctx.guild.roles, name="Muted")
                    for channel in guild.text_channels:
                        await channel.set_permissions(role, send_messages=False)
                        
                except Exception as e:
                    print(e)

            try:
                role = discord.utils.get(ctx.guild.roles, name='Muted')
                if not member:
                    embed = discord.Embed(
                        title = ':gear: Error',
                        description = '``Reason :`` Please specify a member to Mute.',
                        color = discord.Color.green()
                    )
                    embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
                    await ctx.send(embed=embed)
                else:
                    await member.add_roles(role,reason=reason)
                    mute = discord.Embed(
                    title = ':mute: Muted',
                    description = f"``User :`` **{member}**\n``ID :``**{member.id}**\n``Duration :``**{mute_minutes} Mins**\n``Reason :``**{reason}**",
                    color = discord.Color.green()
                    )
                    mute.set_thumbnail(url=member.avatar_url)
                    mute.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
                    await ctx.send(embed=mute)

                    if mute_minutes > 0:
                        await asyncio.sleep(mute_minutes * 60)
                        await member.remove_roles(role,reason='Auto Unmute')
                        unmute = discord.Embed(
                            title = ':speaker: Unmuted',
                            description = f"``User :`` **{member}**\n``ID :`` **{member.id}**\n``Duration :`` **{mute_minutes} Mins**\n``Reason :`` **{reason}**",
                            color = discord.Color.green()
                        )
                        unmute.set_thumbnail(url=member.avatar_url)
                        unmute.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
                        await ctx.send(embed=unmute)

            except Exception:
                embed = discord.Embed(
                        title = ':gear: Error',
                        description = '``Reason :`` This Command needs a mute role setup on the server',
                        color = discord.Color.green()
                    )
                embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
                await ctx.send(embed=embed)

    @commands.command(aliases=['um'])
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member=None, *,reason=None):
        try:
            role = discord.utils.get(ctx.guild.roles, name='Muted')
            if not member:
                embed = discord.Embed(
                    title = ':gear: Error',
                    description = '``Reason :`` Please specify a member to Unmute.',
                    color = discord.Color.green()
                )
                embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
                await ctx.send(embed=embed)
            else:
                await member.remove_roles(role,reason='Auto Unmute')
                unmute = discord.Embed(
                    title = ':speaker: Unmuted',
                    description = f"``User :`` **{member}**\n``ID :`` **{member.id}**\n``Reason :`` **{reason}**",
                    color = discord.Color.green()
                )
                unmute.set_thumbnail(url=member.avatar_url)
                unmute.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
                await ctx.send(embed=unmute)
        except Exception:
            embed = discord.Embed(
                    title = ':gear: Error',
                    description = '``Reason :`` This Command needs a mute role setup on the server',
                    color = discord.Color.green()
                )
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
            await ctx.send(embed=embed)

    @commands.command(aliases=['c'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=1)
        await ctx.channel.purge(limit=amount)       
        embed = discord.Embed(
        title = ':broom: Cleared',
        description = f'``Moderator :`` **{ctx.author}**\n``Amount :`` **{amount}**',
        color = discord.Color.green()
        )
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Timestamp: {cur_time()} || {cur_date()}')
        await ctx.send(embed=embed,delete_after=3)

def setup(client):
    client.add_cog(Moderation(client))
