import discord
from scripts import configs, colors


modulos = configs.get_commands()


class Cmd:
    async def view(parent, ctx):
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

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

        await ctx.reply(embed = msg, mention_author=False)
