import discord, typing
from discord import app_commands
from discord.ext import commands
from scripts import configs, colors


modulos = configs.get_commands()


class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.hybrid_command(aliases=modulos['fun']['coinflip'])
    @app_commands.describe(predict='the result you are waiting for')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def coinflip(self, ctx, predict: str):
        '''I toss a coin and tell you the result'''
        from random import choice
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        choices = lang['COMMAND']['COINFLIP']['CHOICES']
        if not predict in choices:
            raise commands.errors.BadArgument
        res = choice(choices)
        if predict.lower() == res:
            res_str = lang['COMMAND']['COINFLIP']['WIN']
        else:
            res_str = lang['COMMAND']['COINFLIP']['LOSE']

        embed = discord.Embed(description=lang['COMMAND']['COINFLIP']['CHOSED']+predict+'**, '+lang['COMMAND']['COINFLIP']['RESULT']+res+'**\n'+res_str, color=colors.default)
        embed.set_author(name=lang['COMMAND']['COINFLIP']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['COINFLIP']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


    @coinflip.autocomplete('predict')
    async def module_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        lang        = configs.lang[configs.get_guild(interaction.guild_id)['language']]
        choice_list = []
        for op in lang['COMMAND']['COINFLIP']['CHOICES']:
            if current.lower() in op:
                choice_list.append(app_commands.Choice(name=op, value=op))
        return choice_list


async def setup(bot):
    await bot.add_cog(Coinflip(bot))
 