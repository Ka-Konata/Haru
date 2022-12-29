import discord
from discord.ext import commands
from scripts import configs, errors, colors

class Interaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Interaction(bot))
 