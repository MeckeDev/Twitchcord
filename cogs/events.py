import discord
from discord.ext import commands

class CommandEvents(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print("CommandEvents loaded")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} has connected to Discord!')

        game = discord.Game("working hard..")
        await self.bot.change_presence(status=discord.Status.online, activity=game)

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.author.name)
        if message.author.name == self.bot.user.name:
            pass

        else:
            await self.bot.process_commands(message)


def setup(bot):
    bot.add_cog(CommandEvents(bot))