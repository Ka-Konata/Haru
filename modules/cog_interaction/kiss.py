import discord, requests, typing
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors
from decouple import config as getenv
from datetime import datetime
from modules.cog_interaction.ui import base_view


modulos = configs.get_commands()


class Kiss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.hybrid_command(aliases=modulos['interaction']['kiss'])
    @app_commands.describe(user='The one you want to kiss')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def kiss(self, ctx, user: discord.User):
        '''Makes you kiss someone'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        embed = discord.Embed(title=lang['COMMAND']['DICE']['TITLE'], description=f':game_die: **{"res"}**', color=colors.default)
        embed.set_author(name=lang['COMMAND']['DICE']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['DICE']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Kiss(bot))
 