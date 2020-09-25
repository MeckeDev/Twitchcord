# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='load', help="load a Cog")
@commands.has_role('Admin')
async def create_channel(self, ctx, cog):
    bot.load_extension(f"cogs.{cog}")


for file in os.listdir("./cogs/"):
    if file.endswith(".py") and not file.startswith("_"):
        bot.load_extension(f'cogs.{file[:-3]}')

bot.run(TOKEN)