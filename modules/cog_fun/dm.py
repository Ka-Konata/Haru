import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors


modulos = configs.get_commands()


class Dm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.hybrid_command(aliases=modulos['fun']['dm'])
    @app_commands.describe(text='The user I should send the message to')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def dm(self, ctx, user: discord.User, text: str):
        '''Make me dm someone'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        await user.send(text)
        await ctx.reply('mensagem enviada.', mention_author=False)


    @dm.error
    async def pretix_error(self, ctx, error):
        if isinstance(error, commands.errors.HybridCommandError):
            lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
            embed = errors.get_error_embed(lang, lang['ERROR']['HybridCommandError']['TYPE'])
        else:
            return None
        await ctx.reply(embed=embed, mention_author=False)



async def setup(bot):
    await bot.add_cog(Dm(bot))
