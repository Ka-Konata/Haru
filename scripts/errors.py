import discord
from discord.ext import commands
from scripts import colors, configs

class GuildNotAllowed(commands.CommandError):
    pass
class AuthenticationFailure(commands.CommandError):
    pass
class CommandOrModuleNotFound(commands.CommandError):
    pass
class DevModeUnknown(commands.CommandError):
    pass
class PrefixVeryBig(commands.CommandError):
    pass
class LanguageDontExists(commands.CommandError):
    pass
class CommandLocked(commands.CommandError):
    pass
class CommandDontExists(commands.CommandError):
    pass
class ModuleDontExists(commands.CommandError):
    pass
class CannotBeLocked(commands.CommandError):
    pass


local_errors = [DevModeUnknown, CommandOrModuleNotFound, PrefixVeryBig, LanguageDontExists]
global_errors = [GuildNotAllowed, AuthenticationFailure, CommandLocked, CommandDontExists, ModuleDontExists, CannotBeLocked]

def get_error_embed(lang, type, reason = None, tip = None, unknown=False):
    settings = configs.get_configs()

    embed=discord.Embed(color=colors.error) # title='Um erro me impediu de executar o comando...',
    embed.set_author(name=lang['ERROR']['AUTHOR'] if unknown == False else lang['ERROR']['AUTHOR UNKNOWN'], icon_url=settings['bot-icon'])
    #embed.set_thumbnail(url=settings['app_icon'])
    embed.add_field(name=lang['ERROR']['TYPE'], value=f'```{type}```', inline=False)
    if not reason == None:
        embed.add_field(name=lang['ERROR']['REASON'], value=f"```{reason}```", inline=True)
    if not tip == None:
        embed.add_field(name=lang['ERROR']['TIP'], value=f"```{tip}```", inline=True)
    embed.set_footer(text=lang['ERROR']['FOOTER'] if unknown == False else lang['ERROR']['FOOTER UNKNOWN'])
    return embed