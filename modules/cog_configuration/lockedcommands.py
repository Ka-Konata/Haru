import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class Lockedcommands(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot

    
    @commands.hybrid_command(aliases=modulos['configuration']['lockedcommands'])
    @commands.check(configs.Authentication.moderator)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def lockedcommands(self, ctx): #finder
        '''Sends a list of all locked commands on this guild'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        guild = configs.get_guild(ctx.guild.id)

        cmd_list = guild['lockedcommands']

        cmds_str = ''
        for cmd in cmd_list:
            cmds_str = cmds_str+'`'+cmd+'`\t'
        if len(cmd_list) == 0:
            cmds_str = '`'+lang['COMMAND']['LOCKEDCOMMANDS']['NONE']+'`'

        embed = discord.Embed(description=lang['COMMAND']['LOCKEDCOMMANDS']['DESCRIPTION'], color=colors.default)
        embed.set_author(name=lang['COMMAND']['LOCKEDCOMMANDS']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.add_field(name=lang['COMMAND']['LOCKEDCOMMANDS']['TITLE'], value=cmds_str, inline=True)
        embed.set_footer(text=lang['COMMAND']['LOCKEDCOMMANDS']['FOOTER'])

        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Lockedcommands(bot))
 