import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()
categories = {
    "help": ['view', 'command', 'module']
}


class Github(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot


    @commands.hybrid_command(aliases=modulos['bot']['github'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def github(self, ctx):
        '''Send Haru's repository link on github'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        
        embed = discord.Embed(description=lang['COMMAND']['GITHUB']['DESCRIPTION']+settings['server-invite']+').', color=colors.default)
        embed.set_author(name=lang['COMMAND']['GITHUB']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['GITHUB']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Github(bot))
 