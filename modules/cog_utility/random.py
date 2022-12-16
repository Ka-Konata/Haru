import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors

modulos = configs.get_commands()


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(aliases=modulos['utility']['random'])
    @app_commands.describe(until_num='Until the number', from_num='From the number')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def random(self, ctx, from_num : int = 0, until_num : int = 100):
        '''Get a random number'''
        from random import randint
        if from_num >= until_num:
            raise errors.StartBiggerThanEnd

        num = randint(from_num, until_num)
        await ctx.reply(f'`{num}`', mention_author=False)


    @random.error
    async def random_error(self, ctx, error):
        if isinstance(error, errors.StartBiggerThanEnd):
            lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
            embed = errors.get_error_embed(lang, lang['ERROR']['StartBiggerThanEnd']['TYPE'], reason=lang['ERROR']['StartBiggerThanEnd']['REASON'])
        else:
            return None
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Random(bot))
 