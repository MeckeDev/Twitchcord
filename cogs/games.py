import random
from discord.ext import commands

class Minigames(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print("Minigames loaded.")

    @commands.command(name='roll_dice', help='Simulates rolling dice.')
    async def roll(ctx, number_of_dice: int, number_of_sides: int):
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice))

def setup(bot):
    bot.add_cog(Minigames(bot))