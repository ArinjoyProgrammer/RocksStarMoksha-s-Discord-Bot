import discord
from discord import member
from discord.ext import commands
import os
from datetime import datetime
from discord_slash import SlashCommand


prefixes = '.', 'RM.', 'rm.'
intents = discord.Intents.all()


client = commands.Bot(command_prefix=prefixes, intents=intents)
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print("Bot is ready")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run('OTI4MTY1MjEyNDQ2NjYyNjc2.YdUzNw.6aT7LLAE4XzMzJY13CqgEn9QZts')
