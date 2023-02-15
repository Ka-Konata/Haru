import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, colors
from random import choice


modulos = configs.get_commands()


class Choose(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.hybrid_command(aliases=modulos['fun']['choose'])
    @app_commands.describe(
        choice1='listing all options...',
        choice2='listing all options...',
        choice3='listing all options...',
        choice4='listing all options...',
        choice5='listing all options...',
        choice6='listing all options...',
        choice7='listing all options...',
        choice8='listing all options...',
        choice9='listing all options...',
        choice10='listing all options...',
        choice12='listing all options...',
        choice13='listing all options...',
        choice14='listing all options...',
        choice15='listing all options...',
        choice16='listing all options...',
        choice17='listing all options...',
        choice18='listing all options...',
        choice19='listing all options...',
        choice20='listing all options...'
     )
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def choose(self, ctx, choice1, choice2, choice3 = None, choice4 = None, choice5 = None, choice6 = None, choice7 = None, choice8 = None, choice9 = None, choice10 = None, choice11 = None, choice12 = None, choice13 = None, choice14 = None, choice15 = None, choice16 = None, choice17 = None, choice18 = None, choice19 = None, choice20 = None):
        '''Description'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        if ctx.interaction == None:
            print(ctx.message.content)
            msg = ctx.message.content.split('$')
            print(msg, '\n')
            msg[0] = msg[0].split(' ', 1)[1]
            options = msg

            if len(options) == 1:
                raise commands.BadArgument
        else:
            _options = [choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9, choice10, choice11, choice12, choice13, choice14, choice15, choice16, choice17, choice18, choice19, choice20]
            options = []
            for op in _options:
                if op != None:
                    options.append(op)

        res = choice(options)

        embed = discord.Embed(title=lang['COMMAND']['CHOICE']['DESC'], description=f'\n{res}', color=colors.default)
        embed.set_author(name=lang['COMMAND']['CHOICE']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['CHOICE']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Choose(bot))
 