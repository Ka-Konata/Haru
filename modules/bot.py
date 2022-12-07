import typing
import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot

    
    @commands.hybrid_command(nsfw=True, aliases=modulos['bot']['help'])
    @app_commands.describe(especify='Input a command or a module.')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.guild_check)
    async def help(self, ctx, especify : str = None):
        '''Uma lista com todos os comandos ou uma explicação de um módulo ou comando específico.'''
        settings = configs.get()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        msg = discord.Embed()
        cmd = False
        for i in modulos.keys():
            for j in modulos[i]:
                if especify in modulos[i] or especify in modulos[i][j]:
                    msg = discord.Embed(title=lang['HELP']['COMMAND']['TITLE']+especify, description=lang['HELP']['COMMAND'][especify]['DESCRIPTION'], color=colors.default)
                    msg.set_author(name=lang['HELP']['COMMAND']['NAME'], icon_url=settings['bot-icon'])
                    msg.set_thumbnail(url=settings['app-icon'])

                    msg.add_field(name=lang['HELP']['COMMAND']['HOW TITLE'], value=lang['HELP']['COMMAND'][especify]['HOW VALUE'], inline=False)
                    msg.add_field(name=lang['HELP']['COMMAND']['EXEMPLE TITLE'], value=lang['HELP']['COMMAND'][especify]['EXEMPLE VALUE'], inline=True)

                    cmd_mod = None
                    for mod in modulos.keys():
                        if especify in modulos[mod]:
                            cmd_mod = mod
                            break
                    aliases = modulos[cmd_mod][especify]
                    aliases_str = ''
                    for aliase in aliases:
                        aliases_str += f'`{aliase}` '

                    msg.add_field(name=lang['HELP']['COMMAND']['ALIASES TITLE'], value=aliases_str, inline=True)
                    msg.set_footer(text=lang['HELP']['COMMAND']['FOOTER'])

                    cmd = True
                    break
        if not cmd:
            if especify == None:
                msg = discord.Embed(title=lang['HELP']['DEFAULT']['TITLE'], description=lang['HELP']['DEFAULT']['DESCRIPTION'], color=colors.default)
                msg.set_author(name=lang['HELP']['DEFAULT']['NAME'], icon_url=settings['bot-icon'])
                msg.set_thumbnail(url=settings['app-icon'])

                bot = str(list(modulos['bot'].keys())).replace('[', '').replace(']', '').replace("'", '')
                msg.add_field(name=lang['HELP']['DEFAULT']['MODULE']['BOT'], value=f'```{bot}```', inline=False)

                configuration = str(list(modulos['configuration'].keys())).replace('[', '').replace(']', '').replace("'", '')
                msg.add_field(name=lang['HELP']['DEFAULT']['MODULE']['CONFIGURATION'], value=f'```{configuration}```', inline=False)
                
                utility = str(list(modulos['utility'].keys())).replace('[', '').replace(']', '').replace("'", '')
                msg.add_field(name=lang['HELP']['DEFAULT']['MODULE']['UTILITY'], value=f'```{utility}```', inline=False)

                fun = str(list(modulos['fun'].keys())).replace('[', '').replace(']', '').replace("'", '')
                msg.add_field(name=lang['HELP']['DEFAULT']['MODULE']['FUN'], value=f'```{fun}```', inline=False)

                interaction = str(list(modulos['interaction'].keys())).replace('[', '').replace(']', '').replace("'", '')
                msg.add_field(name=lang['HELP']['DEFAULT']['MODULE']['INTERACTION'], value=f'```{interaction}```', inline=False)
                msg.set_footer(text=lang['HELP']['DEFAULT']['FOOTER'])
            elif especify in modulos.keys():
                msg = discord.Embed(title=lang['HELP']['MODULE'][especify]['TITLE'], description=lang['HELP']['MODULE'][especify]['DESCRIPTION'], color=colors.default)
                msg.set_thumbnail(url=settings['app-icon'])
                msg.set_author(name=lang['HELP']['MODULE']['NAME'], icon_url=settings['bot-icon'])
                value = str(list(modulos[especify].keys())).replace('[', '').replace(']', '').replace("'", '')
                msg.add_field(name=lang['HELP']['MODULE']['FIELD NAME'], value=f'```{value}```', inline=False)
            else:
                raise errors.CommandOrModuleNotFound

        await ctx.send(embed = msg)


    @help.autocomplete('especify')
    async def help_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for module in modulos.keys():
            if current.lower() in module.lower() and len(choice_list) < 25:
                choice_list.append(app_commands.Choice(name=module, value=module))
            for cmd in modulos[module].keys():
                if current.lower() in cmd.lower() and len(choice_list) < 25:
                    choice_list.append(app_commands.Choice(name=cmd, value=cmd))
        return choice_list

    
    @help.error
    async def help_error(self, ctx, error):
        if isinstance(error, errors.CommandOrModuleNotFound):
            lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
            embed = errors.get_error_embed(lang, 'Não Existe Nenhum Comandulo ou Modulo com Este Nome')
        else:
            return None
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Bot(bot))
 