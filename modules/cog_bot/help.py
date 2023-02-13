import typing
import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors
from modules.cog_bot.category_help import view as help_view
from modules.cog_bot.category_help import module as help_module
from modules.cog_bot.category_help import command as help_command

modulos = configs.get_commands()
categories = {
    "help": ['view', 'command', 'module']
}


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot


    @commands.hybrid_group(aliases=modulos['bot']['help'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def help(self, ctx):
        '''A list of all modules and commands'''
        await help_view.Cmd.view(self, ctx)


    @help.command(aliases=modulos['bot']['view'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def view(self, ctx):
        '''A list of all modules and commands'''
        await help_view.Cmd.view(self, ctx)


    @help.command(aliases=modulos['bot']['module'])
    @app_commands.describe(module='Command you want to get help')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def module(self, ctx, module : str):
        '''Get explanation about a specific module'''
        await help_module.Cmd.module(self, ctx, module)


    @module.autocomplete('module')
    async def module_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for module in modulos.keys():
            if current.lower() in module.lower() and len(choice_list) < 25:
                choice_list.append(app_commands.Choice(name=module, value=module))
        return choice_list


    @help.command(aliases=modulos['bot']['command'])
    @app_commands.describe(command='Command you want to get help')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def command(self, ctx, command : str):
        '''Get explanation about a specific command'''
        await help_command.Cmd.command(self, ctx, command)


    @command.autocomplete('command')
    async def command_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
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
    await bot.add_cog(Help(bot))
 