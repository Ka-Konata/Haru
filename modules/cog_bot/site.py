import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()
categories = {
    "help": ['view', 'command', 'module']
}


class Site(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot


    @commands.hybrid_command(aliases=modulos['bot']['site'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def site(self, ctx):
        '''Send the bot's official website link'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        
        embed = discord.Embed(description=lang['COMMAND']['SITE']['DESCRIPTION']+settings['site']+').', color=colors.default)
        embed.set_author(name=lang['COMMAND']['SITE']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['SITE']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Site(bot))
 