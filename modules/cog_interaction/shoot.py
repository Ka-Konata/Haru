import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs
from modules.cog_interaction.ui import base_view, generate_embed


modulos = configs.get_commands()


class Shoot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.hybrid_command(aliases=modulos['interaction']['shoot'])
    @app_commands.describe(user='The one you want to shoot')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def shoot(self, ctx, user: discord.User):
        '''Makes you shoot someone (not really)'''
        settings = configs.get_configs()
        lang     = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        gen = generate_embed.generate(type='shoot', lang=lang, settings=settings, user1=ctx.author, user2=user)
        view = base_view.BaseView(type='shoot', lang=lang, settings=settings, user1=ctx.author, user2=user)
        message = await ctx.reply(gen['title'], view=view, embed=gen['embed'], mention_author=False) 
        view.message = message


async def setup(bot):
    await bot.add_cog(Shoot(bot))
