import os
import asyncio
import discord
from discord.ext import commands

class SystemComamnds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print("SystemCommands loaded.")

    @commands.command(name='reload', help="reload all Cogs")
    @commands.has_role('Admin')
    async def reload_cogs(self, ctx, cog=None):
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
                            
                            self.bot.unload_extension(f"cogs.{ext[:-3]}")
                            self.bot.load_extension(f"cogs.{ext[:-3]}")

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

def setup(bot):
    bot.add_cog(SystemComamnds(bot))