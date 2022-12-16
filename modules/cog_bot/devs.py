import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()
categories = {
    "help": ['view', 'command', 'module']
}


class Devs(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot


    @commands.hybrid_command(aliases=modulos['bot']['devs'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def devs(self, ctx):
        '''Informations about the bot development team'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        devs_count = len(settings['developer-list'])
        devs_str = ''
        for dev in settings['developer-list']:
            devs_str += f'{ctx.bot.get_user(dev).mention}\n'

        managers_count = len(settings['manager-list'])
        managers_str = ''
        for manager in settings['manager-list']:
            managers_str += f'{ctx.bot.get_user(manager).mention}\n'

        embed = discord.Embed(description=lang['COMMAND']['DEVS']['DESCRIPTION']+str(devs_count + managers_count)+'`.', color=colors.default)
        embed.add_field(name=lang['COMMAND']['DEVS']['LIST DEVS']['TITLE'], value=devs_str if devs_str != '' else lang['COMMAND']['DEVS']['LIST DEVS']['VALUE'])
        embed.add_field(name=lang['COMMAND']['DEVS']['LIST MANAGERS']['TITLE'], value=managers_str if managers_str != '' else lang['COMMAND']['DEVS']['LIST MANAGERS']['VALUE'])
        embed.set_author(name=lang['COMMAND']['DEVS']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['DEVS']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Devs(bot))
 