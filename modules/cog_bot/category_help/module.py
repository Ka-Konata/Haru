import discord
from scripts import configs, colors, errors


modulos = configs.get_commands()


class Cmd: 
    async def module(self, ctx, module : str):
        '''Get explanation about a specific module'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        module = module.lower()
        if module in modulos.keys():
            msg = discord.Embed(title=lang['HELP']['MODULE'][module]['TITLE'], description=lang['HELP']['MODULE'][module]['DESCRIPTION'], color=colors.default)
            msg.set_thumbnail(url=settings['app-icon'])
            msg.set_author(name=lang['HELP']['MODULE']['NAME'], icon_url=settings['bot-icon'])
            value = str(list(modulos[module].keys())).replace('[', '').replace(']', '').replace("'", '')
            msg.add_field(name=lang['HELP']['MODULE']['FIELD NAME'], value=f'```{value}```', inline=False)
            await ctx.reply(embed = msg, mention_author=False)
        else:
            raise errors.ModuleNotFound
