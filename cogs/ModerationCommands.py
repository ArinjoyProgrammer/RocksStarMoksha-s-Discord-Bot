from datetime import date, datetime
import discord
from discord.ext import commands


class ModerationCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    # FOR TEST ONLY COMMAND
    @commands.command()
    async def ping(self, ctx):
        await ctx.reply("Pong!")



    # KICK COMMAND
    @commands.command()
    # @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if reason == None:
            reason="No Reason has been provided"
        await ctx.guild.kick(member)
        await ctx.send(f"User {member.mention} has been kicked from {ctx.guild.name} | Reason: {reason}")


    # MUTE COMMAND
    @commands.command()
    # @commands.has_permissions(manage_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild.name
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        embed = discord.Embed(title="Mute Message", description=f"**{member.mention}** has been muted from **{ctx.guild.name}**", timestamp=datetime.utcnow(), color=discord.Color.red())
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send("You have been muted from **{ctx.guild.name}**")


    @commands.command()
    # @commands.has_permissions(manage_members=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await member.send(f"You have been unmuted from: {ctx.guild.name}")
        embed = discord.Embed(title="Unmute Message", description=f"{member.mention} has been Unmuted from {ctx.guild.name}", timestamp=datetime.utcnow(), color=discord.Color.green())
        embed.set_footer(text=f"{member} has been Unmuted from the server")

        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        await ctx.guild.ban(member, reason=reason)
        await member.send(f"You have been banned in {ctx.guild} for {reason}")
        await ctx.send(f"{member} has been successfully banned.")


    @commands.command()
    async def strike(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(title="Strike Message", description=f"{member.mention} has got STRIKE from {ctx.guild.name}\nReason: {reason}", timestamp=datetime.utcnow(), color=discord.Color.red())

        await member.send(f"You got STRIKE from {ctx.guild.name}")

        await ctx.send(embed=embed)


    @commands.command()
    async def report(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(title="Report Message", description=f"{member.mention}has been reported from {ctx.guild.name}\nReason: {reason}", timestamp=datetime.utcnow(), color=discord.Color.red())

        await member.send(f"You have got a **Report Message** from **{ctx.guild.name}**\nReason: {reason}")

        await ctx.send(embed=embed)


    @commands.command()
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(title="Warning Message", description=f"{member.mention} has been warned from {ctx.guild.name}\nReason: {reason}", timestamp=datetime.utcnow(), color=discord.Color.red())

        await member.send(f"You got a **Warning** from {ctx.guild.name}\nReason: {reason}")

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(ModerationCommands(client))
