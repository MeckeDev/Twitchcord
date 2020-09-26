# bot.py
import os
import random
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='reload', help="reload all Cogs")
@commands.has_role('Admin')
async def reload_cogs(ctx, cog=None):
    if not cog:
        async with ctx.typing():

            embed = discord.Embed(
                title="Reloading all Cogs!",
                color = 0x808080,
                timestamp = ctx.message.created_at
            )

            for ext in os.listdir("./cogs/"):

                if ext.endswith(".py") and not ext.startswith("_"):

                    try:
                        
                        bot.unload_extension(f"cogs.{ext[:-3]}")
                        bot.load_extension(f"cogs.{ext[:-3]}")

                        embed.add_field(
                            name = f"Reloaded: {ext}",
                            value = '\uFEFF',
                            inline=False
                        )

                    except Exception as e:
                        embed.add_field(
                            name = f"Failed to reload: `{ext}`",
                            value=e,
                            inline=False
                        )

                    await asyncio.sleep(0.5)
            
            await ctx.send(embed=embed)

for file in os.listdir("./cogs/"):
    if file.endswith(".py") and not file.startswith("_"):
        bot.load_extension(f'cogs.{file[:-3]}')

bot.run(TOKEN)