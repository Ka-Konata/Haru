import typing
import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()
categories = {
    "help": ['view', 'command', 'module']
}


class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot


async def setup(bot):
    await bot.add_cog(Bot(bot))
 