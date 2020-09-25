import discord
from discord.ext import commands

class CommandEvents(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} has connected to Discord!')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.name == self.bot.user.name:
            return

        else:
            await self.bot.process_commands(message)


def setup(bot):
    bot.add_cog(CommandEvents(bot))