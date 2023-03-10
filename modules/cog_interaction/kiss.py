import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, colors
from random import randint
from modules.cog_interaction.ui import base_view, generate_embed


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
        lang     = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        gen = generate_embed.generate(type='kiss', lang=lang, settings=settings, user1=ctx.author, user2=user)
        view = base_view.BaseView(type='kiss', lang=lang, settings=settings, user1=ctx.author, user2=user)
        message = await ctx.reply(gen['title'], view=view, embed=gen['embed'], mention_author=False) 
        view.message = message


async def setup(bot):
    await bot.add_cog(Kiss(bot))
