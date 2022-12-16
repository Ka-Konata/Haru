import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot

    
    @commands.hybrid_command(aliases=modulos['configuration']['settings'])
    @commands.check(configs.Authentication.moderator)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def settings(self, ctx): #finder
        '''Send all guild settings'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        guild = configs.get_guild(ctx.guild.id)

        prefix   = '`'+guild['prefix']+'`'
        language = '`'+guild['language']+' '+lang['COMMAND']['SETTINGS']['LANGUAGE VALUE']+'`'
        lockedcommands = ''
        for cmd in guild['lockedcommands']:
            lockedcommands = lockedcommands+'`'+cmd+'`\t'
        if len(guild['lockedcommands']) == 0:
            lockedcommands = '`'+lang['COMMAND']['SETTINGS']['NONE']+'`'

        embed = discord.Embed(description=lang['COMMAND']['SETTINGS']['DESCRIPTION'], color=colors.default)
        embed.set_author(name=lang['COMMAND']['SETTINGS']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.add_field(name=lang['COMMAND']['SETTINGS']['PREFIX'], value=prefix, inline=True)
        embed.add_field(name=lang['COMMAND']['SETTINGS']['LANGUAGE'], value=language, inline=True)
        embed.add_field(name=lang['COMMAND']['SETTINGS']['LOCKEDCOMMANDS'], value=lockedcommands, inline=False)
        embed.set_footer(text=lang['COMMAND']['SETTINGS']['FOOTER'])

        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Settings(bot))
 