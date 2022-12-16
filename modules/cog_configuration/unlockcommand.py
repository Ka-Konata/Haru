import typing
import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()
categories = {
    "help": ['view', 'command', 'module']
}


class Unlockcommand(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot

    
    @commands.hybrid_command(aliases=modulos['configuration']['unlockcommand'])
    @app_commands.describe(command='The command to be locked.')
    @commands.check(configs.Authentication.administrator)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def unlockcommand(self, ctx, command : str): #finder
        '''Unlocks the use of a command for everyone'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        for mod in modulos:
            if command in modulos[mod].keys():
                guild = configs.get_guild(ctx.guild.id, all=True)
                if command in guild[str(ctx.guild.id)]['lockedcommands']:
                    guild[str(ctx.guild.id)]['lockedcommands'].remove(command)
                    configs.save(guild, 'storage/guilds.json')

                embed = discord.Embed(description=lang['COMMAND']['UNLOCKCOMMAND']['DESCRIPTION'], color=colors.default)
                embed.set_author(name=lang['COMMAND']['UNLOCKCOMMAND']['NAME'], icon_url=settings['bot-icon'])
                embed.set_thumbnail(url=settings['app-icon'])
                embed.add_field(name=lang['COMMAND']['UNLOCKCOMMAND']['TITLE'], value='`'+command+'`', inline=True)
                embed.set_footer(text=lang['COMMAND']['UNLOCKCOMMAND']['FOOTER'])

                await ctx.reply(embed=embed, mention_author=False)

                return None
        raise errors.CommandDontExists


    @unlockcommand.autocomplete('command')
    async def unlockcommand_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for module in modulos.keys():
            for cmd in modulos[module].keys():
                if current.lower() in cmd.lower() and len(choice_list) < 25:
                    prefix = None
                    for category in categories.keys():
                        if cmd in categories[category]:
                            prefix = str(category) + ' '
                    if prefix != None:
                        choice_list.append(app_commands.Choice(name=prefix+cmd, value=cmd))
                    else:
                        choice_list.append(app_commands.Choice(name=cmd, value=cmd))
        return choice_list


async def setup(bot):
    await bot.add_cog(Unlockcommand(bot))
 