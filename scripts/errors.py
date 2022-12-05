import discord
from discord.ext import commands
from scripts import colors, configs

class GuildNotAllowed(commands.CommandError):
    pass
class AuthenticationFailure(commands.CommandError):
    pass

def get_error_embed(type, reason = None):
    settings = configs.get()

    embed=discord.Embed(color=colors.error) # title='Um erro me impediu de executar o comando...',
    embed.set_author(name='Haru - Erro', icon_url=settings['bot_icon'])
    #embed.set_thumbnail(url=settings['app_icon'])
    embed.add_field(name='Tipo: ', value=f'```{type}```', inline=False)
    if not reason == None:
        embed.add_field(name='Motivo:', value=f"```{reason}```", inline=True)
    embed.set_footer(text='Use /help ou h!help para mais informações')
    return embed