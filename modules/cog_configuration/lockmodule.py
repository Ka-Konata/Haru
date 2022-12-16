import typing
import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class Lockmodule(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot

    
    @commands.hybrid_command(aliases=modulos['configuration']['lockmodule'])
    @app_commands.describe(module='A module to be locked.')
    @commands.check(configs.Authentication.administrator)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def lockmodule(self, ctx, module : str):
        '''Blocks the use of a module for everyone'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        if module in ['configuration']:
            print('cannot', mod)
            raise errors.CannotBeLocked

        for mod in modulos:
            if mod == module:
                cmds_str = ''
                guild = configs.get_guild(ctx.guild.id, all=True)
                for cmd in modulos[module].keys():
                    cmds_str = cmds_str+'`'+cmd+'`\t'
                    if not cmd in guild[str(ctx.guild.id)]['lockedcommands']:
                        guild[str(ctx.guild.id)]['lockedcommands'].append(cmd)
                configs.save(guild, 'storage/guilds.json')

                embed = discord.Embed(description=lang['COMMAND']['LOCKMODULE']['DESCRIPTION'], color=colors.default)
                embed.set_author(name=lang['COMMAND']['LOCKMODULE']['NAME'], icon_url=settings['bot-icon'])
                embed.set_thumbnail(url=settings['app-icon'])
                embed.add_field(name=lang['COMMAND']['LOCKMODULE']['TITLE'], value=cmds_str, inline=True)
                embed.set_footer(text=lang['COMMAND']['LOCKMODULE']['FOOTER'])

                await ctx.reply(embed=embed, mention_author=False)

                return None
        raise errors.ModuleDontExists


    @lockmodule.autocomplete('module')
    async def lockmodule_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for module in modulos.keys():
            if current.lower() in module.lower() and len(choice_list) < 25:
                choice_list.append(app_commands.Choice(name=module, value=module))
        return choice_list


async def setup(bot):
    await bot.add_cog(Lockmodule(bot))
 