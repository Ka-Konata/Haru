import typing
import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()
categories = {
    "help": ['view', 'command', 'module']
}


class Lockcommand(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot

    
    @commands.hybrid_command(aliases=modulos['configuration']['lockcommand'])
    @app_commands.describe(command='A command to be locked.')
    @commands.check(configs.Authentication.administrator)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def lockcommand(self, ctx, command : str):
        '''Blocks the use of a command for everyone'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        for mod in modulos:
            if command in modulos[mod].keys():
                if mod in ['configuration']:
                    print('cannot', mod)
                    raise errors.CannotBeLocked

                guild = configs.get_guild(ctx.guild.id, all=True)
                if not command in guild[str(ctx.guild.id)]['lockedcommands']:
                    guild[str(ctx.guild.id)]['lockedcommands'].append(command)
                    configs.save(guild, 'storage/guilds.json')

                embed = discord.Embed(description=lang['COMMAND']['LOCKCOMMAND']['DESCRIPTION'], color=colors.default)
                embed.set_author(name=lang['COMMAND']['LOCKCOMMAND']['NAME'], icon_url=settings['bot-icon'])
                embed.set_thumbnail(url=settings['app-icon'])
                embed.add_field(name=lang['COMMAND']['LOCKCOMMAND']['TITLE'], value='`'+command+'`', inline=True)
                embed.set_footer(text=lang['COMMAND']['LOCKCOMMAND']['FOOTER'])

                await ctx.reply(embed=embed, mention_author=False)

                return None
        raise errors.CommandDontExists


    @lockcommand.autocomplete('command')
    async def lockcommand_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
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
    await bot.add_cog(Lockcommand(bot))
 