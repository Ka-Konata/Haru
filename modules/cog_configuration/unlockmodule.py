import typing
import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class Unlockmodule(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot


    @commands.hybrid_command(aliases=modulos['configuration']['unlockmodule'])
    @app_commands.describe(module='The module to be unlocked.')
    @commands.check(configs.Authentication.administrator)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def unlockmodule(self, ctx, module : str): #finder
        '''Unlocks the use of a module for everyone'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        for mod in modulos:
            if module == mod:
                guild = configs.get_guild(ctx.guild.id, all=True)
                cmds_str = ''
                for cmd in modulos[mod].keys():
                    cmds_str = cmds_str+'`'+cmd+'`\t'
                    if cmd in guild[str(ctx.guild.id)]['lockedcommands']:
                        guild[str(ctx.guild.id)]['lockedcommands'].remove(cmd)
                configs.save(guild, 'storage/guilds.json')

                embed = discord.Embed(description=lang['COMMAND']['UNLOCKMODULE']['DESCRIPTION'], color=colors.default)
                embed.set_author(name=lang['COMMAND']['UNLOCKMODULE']['NAME'], icon_url=settings['bot-icon'])
                embed.set_thumbnail(url=settings['app-icon'])
                embed.add_field(name=lang['COMMAND']['UNLOCKMODULE']['TITLE'], value=cmds_str, inline=True)
                embed.set_footer(text=lang['COMMAND']['UNLOCKMODULE']['FOOTER'])

                await ctx.reply(embed=embed, mention_author=False)

                return None
        raise errors.ModuleDontExists


    @unlockmodule.autocomplete('module')
    async def unlockmodule_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for module in modulos.keys():
            if current.lower() in module.lower() and len(choice_list) < 25:
                choice_list.append(app_commands.Choice(name=module, value=module))
        return choice_list


async def setup(bot):
    await bot.add_cog(Unlockmodule(bot))
 