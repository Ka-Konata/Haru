import discord, requests, typing
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors
from decouple import config as getenv
from datetime import datetime

modulos = configs.get_commands()


class Cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        
    @commands.hybrid_command(aliases=modulos['fun']['say'])
    @app_commands.describe(text='The text you want me to say')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def say(self, ctx, text : str):
        '''Make me say something'''
        if ctx.interaction != None:
            await ctx.send(text)
        else:
            pass
            copy = ctx.message.content
            text = copy.replace("h!say ", "")
            await ctx.send(text)
            await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(Cmd(bot))
 