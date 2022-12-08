import typing
import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot

    
    @commands.hybrid_command(aliases=modulos['bot']['help'])
    @app_commands.describe(especify='Input a command or module.')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.guild_check)
    async def help(self, ctx, especify : str = None):
        '''A list of all commands or an explanation of a specific module/command.'''
        settings = configs.get()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        msg = discord.Embed()
        cmd = False
        for i in modulos.keys():
            for j in modulos[i]:
                if especify in modulos[i] or especify in modulos[i][j]:

                    if especify in modulos[i][j]:
                        for aux in modulos[i].keys():
                            if especify in modulos[i][aux]:
                                especify = aux
                                break

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
            embed = errors.get_error_embed(lang, lang['ERROR']['CommandOrModuleNotFound']['TYPE'])
        else:
            return None
        await ctx.send(embed=embed)


    @commands.hybrid_command(aliases=modulos['bot']['haru'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.guild_check)
    async def haru(self, ctx):
        '''Basic informations about Haru'''
        settings = configs.get()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        embed = discord.Embed(title=lang['COMMAND']['HARU']['TITLE'], description=lang['COMMAND']['HARU']['DESCRIPTION']+settings['bot-invite']+').', color=colors.default)
        embed.set_author(name=lang['COMMAND']['HARU']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.add_field(name=lang['COMMAND']['HARU']['COMMANDS']['NAME'], value=lang['COMMAND']['HARU']['COMMANDS']['VALUE'], inline=False)
        embed.add_field(name=lang['COMMAND']['HARU']['SERVER']['NAME'], value=lang['COMMAND']['HARU']['SERVER']['VALUE']+settings['bot-invite']+').', inline=False)
        embed.add_field(name=lang['COMMAND']['HARU']['SITE']['NAME'], value=lang['COMMAND']['HARU']['SITE']['VALUE']+settings['site']+').', inline=False)
        embed.set_footer(text=lang['COMMAND']['HARU']['FOOTER'])
        await ctx.send(embed=embed)


    @commands.hybrid_command(aliases=modulos['bot']['invite'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.guild_check)
    async def invite(self, ctx):
        '''Send the bot invite link'''
        settings = configs.get()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        
        embed = discord.Embed(description=lang['COMMAND']['INVITE']['DESCRIPTION']+settings['bot-invite']+').', color=colors.default)
        embed.set_author(name=lang['COMMAND']['INVITE']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['INVITE']['FOOTER'])
        await ctx.send(embed=embed)


    @commands.hybrid_command(aliases=modulos['bot']['site'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.guild_check)
    async def site(self, ctx):
        '''Send the bot's official website link'''
        settings = configs.get()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        
        embed = discord.Embed(description=lang['COMMAND']['SITE']['DESCRIPTION']+settings['site']+').', color=colors.default)
        embed.set_author(name=lang['COMMAND']['SITE']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['SITE']['FOOTER'])
        await ctx.send(embed=embed)


    @commands.hybrid_command(aliases=modulos['bot']['server'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.guild_check)
    async def server(self, ctx):
        '''Send the bot's official server invite link'''
        settings = configs.get()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        
        embed = discord.Embed(description=lang['COMMAND']['SERVER']['DESCRIPTION']+settings['server-invite']+').', color=colors.default)
        embed.set_author(name=lang['COMMAND']['SERVER']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['SERVER']['FOOTER'])
        await ctx.send(embed=embed)


    @commands.hybrid_command(aliases=modulos['bot']['github'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.guild_check)
    async def github(self, ctx):
        '''Send Haru's repository link on github'''
        settings = configs.get()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        
        embed = discord.Embed(description=lang['COMMAND']['GITHUB']['DESCRIPTION']+settings['server-invite']+').', color=colors.default)
        embed.set_author(name=lang['COMMAND']['GITHUB']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['GITHUB']['FOOTER'])
        await ctx.send(embed=embed)


    @commands.hybrid_command(aliases=modulos['bot']['dev'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.guild_check)
    async def dev(self, ctx):
        '''Information about the bot development team'''
        settings = configs.get()
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
        await ctx.send(embed=embed)


    @commands.hybrid_command(aliases=modulos['bot']['ping'])
    @commands.check(configs.Authentication.member)
    @commands.check(configs.guild_check)
    async def ping(self, ctx):
        '''Used to know if haru is alive team'''

        await ctx.send(f'`🏓Pong ({round(self.bot.latency * 1000)}ms)`')


async def setup(bot):
    await bot.add_cog(Bot(bot))
 