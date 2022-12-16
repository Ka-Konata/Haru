import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()
categories = {
    "help": ['view', 'command', 'module']
}


class Haru(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot


    @commands.hybrid_command(aliases=modulos['bot']['haru'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def haru(self, ctx):
        '''Basic informations about Haru'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        embed = discord.Embed(title=lang['COMMAND']['HARU']['TITLE'], description=lang['COMMAND']['HARU']['DESCRIPTION']+settings['bot-invite']+').', color=colors.default)
        embed.set_author(name=lang['COMMAND']['HARU']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.add_field(name=lang['COMMAND']['HARU']['COMMANDS']['NAME'], value=lang['COMMAND']['HARU']['COMMANDS']['VALUE'], inline=False)
        embed.add_field(name=lang['COMMAND']['HARU']['SERVER']['NAME'], value=lang['COMMAND']['HARU']['SERVER']['VALUE']+settings['bot-invite']+').', inline=False)
        embed.add_field(name=lang['COMMAND']['HARU']['SITE']['NAME'], value=lang['COMMAND']['HARU']['SITE']['VALUE']+settings['site']+').', inline=False)
        embed.set_footer(text=lang['COMMAND']['HARU']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Haru(bot))
 