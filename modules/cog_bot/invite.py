import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()
categories = {
    "help": ['view', 'command', 'module']
}


class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot


    @commands.hybrid_command(aliases=modulos['bot']['invite'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def invite(self, ctx):
        '''Send the bot invite link'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        
        embed = discord.Embed(description=lang['COMMAND']['INVITE']['DESCRIPTION']+settings['bot-invite']+').', color=colors.default)
        embed.set_author(name=lang['COMMAND']['INVITE']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['INVITE']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Invite(bot))
 