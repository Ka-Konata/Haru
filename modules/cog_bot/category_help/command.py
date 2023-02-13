import discord
from discord.ext import commands
from scripts import configs, colors


modulos = configs.get_commands()
categories = {
    "help": ['view', 'command', 'module']
}


class Cmd: 
    async def command(self, ctx, command : str):
        '''Get explanation about a specific command'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        command = command.lower()
        cmd = False
        for i in modulos.keys():
            for j in modulos[i]:
                if command in modulos[i] or command in modulos[i][j]:

                    if command in modulos[i][j]:
                        for aux in modulos[i].keys():
                            if command in modulos[i][aux]:
                                command = aux
                                break

                    prefix = None
                    for category in categories.keys():
                        if command in categories[category]:
                            prefix = str(category) + ' '
                    if prefix != None:
                        msg = discord.Embed(title=lang['HELP']['COMMAND']['TITLE']+prefix+command, description=lang['HELP']['COMMAND'][command]['DESCRIPTION'], color=colors.default)
                    else:
                        msg = discord.Embed(title=lang['HELP']['COMMAND']['TITLE']+command, description=lang['HELP']['COMMAND'][command]['DESCRIPTION'], color=colors.default)
                    
                    msg.set_author(name=lang['HELP']['COMMAND']['NAME'], icon_url=settings['bot-icon'])
                    msg.set_thumbnail(url=settings['app-icon'])

                    msg.add_field(name=lang['HELP']['COMMAND']['HOW TITLE'], value=lang['HELP']['COMMAND'][command]['HOW VALUE'], inline=False)
                    msg.add_field(name=lang['HELP']['COMMAND']['EXEMPLE TITLE'], value=lang['HELP']['COMMAND'][command]['EXEMPLE VALUE'], inline=True)

                    cmd_mod = None
                    for mod in modulos.keys():
                        if command in modulos[mod]:
                            cmd_mod = mod
                            break
                    aliases = modulos[cmd_mod][command]
                    aliases_str = ''
                    for aliase in aliases:
                        aliases_str += f'`{aliase}`\t'

                    msg.add_field(name=lang['HELP']['COMMAND']['ALIASES TITLE'], value=aliases_str, inline=True)
                    msg.set_footer(text=lang['HELP']['COMMAND']['FOOTER'])

                    cmd = True
                    break
        if cmd:
            await ctx.reply(embed = msg, mention_author=False)
        else:
            raise commands.errors.CommandNotFound
