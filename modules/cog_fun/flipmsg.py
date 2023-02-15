import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class Flipmsg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(aliases=modulos['fun']['flipmsg'])
    @app_commands.describe(text='The text to be fliped')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def flipmsg(self, ctx, text: str):
        '''Reverses the position of letters in a text'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
    
        if ctx.interaction == None:
            txt = ctx.message.content.split()[1:]
            text  = ''
            for a in txt:
                text += ' ' + a

        inverted = ''
        for char in text[::-1]:
            inverted += char
        
        embed = discord.Embed(description=lang['COMMAND']['FLIPMSG']['DESC']+f'\n```{inverted}```', color=colors.default)
        embed.set_author(name=lang['COMMAND']['FLIPMSG']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['FLIPMSG']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot): 
    await bot.add_cog(Flipmsg(bot))
 