import discord
from discord.ext import commands

class SystemComamnds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print("SystemCommands loaded.")

def setup(bot):
    bot.add_cog(SystemComamnds(bot))