import discord, requests, typing
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors
from decouple import config as getenv
from datetime import datetime


modulos = configs.get_commands()


class Mugistrong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.hybrid_command(aliases=modulos['fun']['mugistrong'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def mugistrong(self, ctx):
        '''Send a gif of Mugi-Strong'''
        await ctx.reply('https://i.imgur.com/9CcpvLY.gif')


async def setup(bot):
    await bot.add_cog(Mugistrong(bot))
