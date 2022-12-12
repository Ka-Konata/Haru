import typing
import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()
categories = {
    "help": ['view', 'command', 'module']
}


class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot


    @commands.hybrid_group(aliases=modulos['bot']['help'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def help(self, ctx):
        '''A list of all modules and commands'''
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


    @help.command(aliases=modulos['bot']['view'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def view(self, ctx):
        '''A list of all modules and commands'''
        await ctx.invoke(self.bot.get_command('help'))


    @help.command(aliases=modulos['bot']['module'])
    @app_commands.describe(module='Command you want to get help')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
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


    @commands.hybrid_command(aliases=modulos['bot']['haru'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def haru(self, ctx):
        '''Basic informations about Haru'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        embed = discord.Embed(title=lang['COMMAND']['HARU']['TITLE'], description=lang['COMMAND']['HARU']['DESCRIPTION']+settings['bot-invite']+').', color=colors.default)
        embed.set_author(name=lang['COMMAND']['HARU']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.add_field(name=lang['COMMAND']['HARU']['COMMANDS']['NAME'], value=lang['COMMAND']['HARU']['COMMANDS']['VALUE'], inline=False)
        embed.add_field(name=lang['COMMAND']['HARU']['SERVER']['NAME'], value=lang['COMMAND']['HARU']['SERVER']['VALUE']+settings['bot-invite']+').', inline=False)
        embed.add_field(name=lang['COMMAND']['HARU']['SITE']['NAME'], value=lang['COMMAND']['HARU']['SITE']['VALUE']+settings['site']+').', inline=False)
        embed.set_footer(text=lang['COMMAND']['HARU']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


    @commands.hybrid_command(aliases=modulos['bot']['invite'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def invite(self, ctx):
        '''Send the bot invite link'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        
        embed = discord.Embed(description=lang['COMMAND']['INVITE']['DESCRIPTION']+settings['bot-invite']+').', color=colors.default)
        embed.set_author(name=lang['COMMAND']['INVITE']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['INVITE']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


    @commands.hybrid_command(aliases=modulos['bot']['site'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def site(self, ctx):
        '''Send the bot's official website link'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        
        embed = discord.Embed(description=lang['COMMAND']['SITE']['DESCRIPTION']+settings['site']+').', color=colors.default)
        embed.set_author(name=lang['COMMAND']['SITE']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['SITE']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


    @commands.hybrid_command(aliases=modulos['bot']['server'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def server(self, ctx):
        '''Send the bot's official server invite link'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        
        embed = discord.Embed(description=lang['COMMAND']['SERVER']['DESCRIPTION']+settings['server-invite']+').', color=colors.default)
        embed.set_author(name=lang['COMMAND']['SERVER']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['SERVER']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


    @commands.hybrid_command(aliases=modulos['bot']['github'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def github(self, ctx):
        '''Send Haru's repository link on github'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        
        embed = discord.Embed(description=lang['COMMAND']['GITHUB']['DESCRIPTION']+settings['server-invite']+').', color=colors.default)
        embed.set_author(name=lang['COMMAND']['GITHUB']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['GITHUB']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


    @commands.hybrid_command(aliases=modulos['bot']['dev'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def dev(self, ctx):
        '''Informations about the bot development team'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        devs_count = len(settings['developer-list'])
        devs_str = ''
        for dev in settings['developer-list']:
            devs_str += f'{ctx.bot.get_user(dev).mention}\n'

        managers_count = len(settings['manager-list'])
        managers_str = ''
        for manager in settings['manager-list']:
            managers_str += f'{ctx.bot.get_user(manager).mention}\n'

        embed = discord.Embed(description=lang['COMMAND']['DEV']['DESCRIPTION']+str(devs_count + managers_count)+'`.', color=colors.default)
        embed.add_field(name=lang['COMMAND']['DEV']['LIST DEVS']['TITLE'], value=devs_str if devs_str != '' else lang['COMMAND']['DEV']['LIST DEVS']['VALUE'])
        embed.add_field(name=lang['COMMAND']['DEV']['LIST MANAGERS']['TITLE'], value=managers_str if managers_str != '' else lang['COMMAND']['DEV']['LIST MANAGERS']['VALUE'])
        embed.set_author(name=lang['COMMAND']['DEV']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['DEV']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


    @commands.hybrid_command(aliases=modulos['bot']['ping'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def ping(self, ctx):
        '''Used to know if haru is alive team'''

        await ctx.reply(f'`🏓Pong ({round(self.bot.latency * 1000)}ms)`', mention_author=False)


async def setup(bot):
    await bot.add_cog(Bot(bot))
 