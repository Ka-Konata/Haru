import typing
import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class Configuration(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot

    
    @commands.hybrid_command(aliases=modulos['configuration']['prefix'])
    @app_commands.describe(new_prefix='Input a new prefix.')
    @commands.check(configs.Authentication.administrator)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def prefix(self, ctx, new_prefix : str):
        '''Allows you to change the guild prefix'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        if len(new_prefix) > 2:
            raise errors.PrefixVeryBig

        guild_configs = configs.get_guild(ctx.guild.id, all=True)
        old_prefix    = guild_configs[str(ctx.guild.id)]['prefix']
        guild_configs[str(ctx.guild.id)]['prefix'] = new_prefix
        configs.save(guild_configs, path='storage/guilds.json')

        embed = discord.Embed(description=lang['COMMAND']['PREFIX']['DESCRIPTION'], color=colors.default)
        embed.set_author(name=lang['COMMAND']['PREFIX']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.add_field(name=lang['COMMAND']['PREFIX']['PREFIX NEW'], value='`'+new_prefix+'`', inline=True)
        embed.add_field(name=lang['COMMAND']['PREFIX']['PREFIX OLD'], value='`'+old_prefix+'`', inline=True)
        embed.set_footer(text=lang['COMMAND']['PREFIX']['FOOTER'])

        await ctx.reply(embed=embed)


    @prefix.error
    async def pretix_error(self, ctx, error):
        if isinstance(error, errors.PrefixVeryBig):
            lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
            embed = errors.get_error_embed(lang, lang['ERROR']['PrefixVeryBig']['TYPE'], lang['ERROR']['PrefixVeryBig']['REASON'])
        else:
            return None
        await ctx.reply(embed=embed)

    
    @commands.hybrid_command(aliases=modulos['configuration']['language'])
    @app_commands.describe(language_code='Input the code for the desired language.')
    @commands.check(configs.Authentication.administrator)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def language(self, ctx, language_code : str):
        '''Allows you to change Haru's language'''
        settings = configs.get_configs()
        if not language_code in settings['languages']:
            raise errors.LanguageDontExists 

        lang = configs.lang[language_code]
         
        guild_configs = configs.get_guild(ctx.guild.id, all=True)
        guild_configs[str(ctx.guild.id)]['language'] = language_code
        configs.save(guild_configs, path='storage/guilds.json')

        embed = discord.Embed(description=lang['COMMAND']['LANGUAGE']['DESCRIPTION'], color=colors.default)
        embed.set_author(name=lang['COMMAND']['LANGUAGE']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.add_field(name=lang['COMMAND']['LANGUAGE']['LANGUAGE TITLE'], value=lang['COMMAND']['LANGUAGE']['LANGUAGE VALUE'])
        embed.set_footer(text=lang['COMMAND']['LANGUAGE']['FOOTER'])

        await ctx.reply(embed=embed)


    @language.error
    async def language_error(self, ctx, error):
        if isinstance(error, errors.LanguageDontExists):
            lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
            embed = errors.get_error_embed(lang, lang['ERROR']['LanguageDontExists']['TYPE'], reason=lang['ERROR']['LanguageDontExists']['REASON'], tip=lang['ERROR']['LanguageDontExists']['TIP'])
        else:
            return None
        await ctx.reply(embed=embed)
        
    
    @language.autocomplete('language_code')
    async def help_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        languages = configs.get_configs()['languages']
        choice_list = []
        for language in languages:
            if current.lower() in language and len(choice_list) < 25:
                choice_list.append(app_commands.Choice(name=language, value=language))
        return choice_list

    
    @commands.hybrid_command(aliases=modulos['configuration']['lockcommand'])
    @app_commands.describe(command='A command to be locked.')
    @commands.check(configs.Authentication.administrator)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def lockcommand(self, ctx, command : str):
        '''Blocks the use of a command for everyone'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        for mod in modulos:
            if command in modulos[mod].keys():
                if mod in ['configuration']:
                    print('cannot', mod)
                    raise errors.CannotBeLocked

                guild = configs.get_guild(ctx.guild.id, all=True)
                if not command in guild[str(ctx.guild.id)]['lockedcommands']:
                    guild[str(ctx.guild.id)]['lockedcommands'].append(command)
                    configs.save(guild, 'storage/guilds.json')

                embed = discord.Embed(description=lang['COMMAND']['LOCKCOMMAND']['DESCRIPTION'], color=colors.default)
                embed.set_author(name=lang['COMMAND']['LOCKCOMMAND']['NAME'], icon_url=settings['bot-icon'])
                embed.set_thumbnail(url=settings['app-icon'])
                embed.add_field(name=lang['COMMAND']['LOCKCOMMAND']['TITLE'], value='`'+command+'`', inline=True)
                embed.set_footer(text=lang['COMMAND']['LOCKCOMMAND']['FOOTER'])

                await ctx.reply(embed=embed)

                return None
        raise errors.CommandDontExists


    @lockcommand.autocomplete('command')
    async def lockcommand_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for module in modulos.keys():
            for cmd in modulos[module].keys():
                if current.lower() in cmd.lower() and len(choice_list) < 25:
                    choice_list.append(app_commands.Choice(name=cmd, value=cmd))
        return choice_list

    
    @commands.hybrid_command(aliases=modulos['configuration']['unlockcommand'])
    @app_commands.describe(command='The command to be locked.')
    @commands.check(configs.Authentication.administrator)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def unlockcommand(self, ctx, command : str): #finder
        '''Unlocks the use of a command for everyone'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        for mod in modulos:
            if command in modulos[mod].keys():
                guild = configs.get_guild(ctx.guild.id, all=True)
                if command in guild[str(ctx.guild.id)]['lockedcommands']:
                    guild[str(ctx.guild.id)]['lockedcommands'].remove(command)
                    configs.save(guild, 'storage/guilds.json')

                embed = discord.Embed(description=lang['COMMAND']['UNLOCKCOMMAND']['DESCRIPTION'], color=colors.default)
                embed.set_author(name=lang['COMMAND']['UNLOCKCOMMAND']['NAME'], icon_url=settings['bot-icon'])
                embed.set_thumbnail(url=settings['app-icon'])
                embed.add_field(name=lang['COMMAND']['UNLOCKCOMMAND']['TITLE'], value='`'+command+'`', inline=True)
                embed.set_footer(text=lang['COMMAND']['UNLOCKCOMMAND']['FOOTER'])

                await ctx.reply(embed=embed)

                return None
        raise errors.CommandDontExists


    @unlockcommand.autocomplete('command')
    async def unlockcommand_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for module in modulos.keys():
            for cmd in modulos[module].keys():
                if current.lower() in cmd.lower() and len(choice_list) < 25:
                    choice_list.append(app_commands.Choice(name=cmd, value=cmd))
        return choice_list

    
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

                await ctx.reply(embed=embed)

                return None
        raise errors.ModuleDontExists


    @lockmodule.autocomplete('module')
    async def lockmodule_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for module in modulos.keys():
            if current.lower() in module.lower() and len(choice_list) < 25:
                choice_list.append(app_commands.Choice(name=module, value=module))
        return choice_list


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

                await ctx.reply(embed=embed)

                return None
        raise errors.ModuleDontExists


    @unlockmodule.autocomplete('module')
    async def unlockmodule_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        choice_list = []
        for module in modulos.keys():
            if current.lower() in module.lower() and len(choice_list) < 25:
                choice_list.append(app_commands.Choice(name=module, value=module))
        return choice_list

    
    @commands.hybrid_command(aliases=modulos['configuration']['lockedcommands'])
    @commands.check(configs.Authentication.moderator)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def lockedcommands(self, ctx): #finder
        '''Sends a list of all locked commands on this guild'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        guild = configs.get_guild(ctx.guild.id)

        cmd_list = guild['lockedcommands']

        cmds_str = ''
        for cmd in cmd_list:
            cmds_str = cmds_str+'`'+cmd+'`\t'
        if len(cmd_list) == 0:
            cmds_str = '`'+lang['COMMAND']['LOCKEDCOMMANDS']['NONE']+'`'

        embed = discord.Embed(description=lang['COMMAND']['LOCKEDCOMMANDS']['DESCRIPTION'], color=colors.default)
        embed.set_author(name=lang['COMMAND']['LOCKEDCOMMANDS']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.add_field(name=lang['COMMAND']['LOCKEDCOMMANDS']['TITLE'], value=cmds_str, inline=True)
        embed.set_footer(text=lang['COMMAND']['LOCKEDCOMMANDS']['FOOTER'])

        await ctx.reply(embed=embed)

    
    @commands.hybrid_command(aliases=modulos['configuration']['settings'])
    @commands.check(configs.Authentication.moderator)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def settings(self, ctx): #finder
        '''Send all guild settings'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
        guild = configs.get_guild(ctx.guild.id)

        prefix   = '`'+guild['prefix']+'`'
        language = '`'+guild['language']+' '+lang['COMMAND']['SETTINGS']['LANGUAGE VALUE']+'`'
        lockedcommands = ''
        for cmd in guild['lockedcommands']:
            lockedcommands = lockedcommands+'`'+cmd+'`\t'
        if len(guild['lockedcommands']) == 0:
            lockedcommands = '`'+lang['COMMAND']['SETTINGS']['NONE']+'`'

        embed = discord.Embed(description=lang['COMMAND']['SETTINGS']['DESCRIPTION'], color=colors.default)
        embed.set_author(name=lang['COMMAND']['SETTINGS']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.add_field(name=lang['COMMAND']['SETTINGS']['PREFIX'], value=prefix, inline=True)
        embed.add_field(name=lang['COMMAND']['SETTINGS']['LANGUAGE'], value=language, inline=True)
        embed.add_field(name=lang['COMMAND']['SETTINGS']['LOCKEDCOMMANDS'], value=lockedcommands, inline=False)
        embed.set_footer(text=lang['COMMAND']['SETTINGS']['FOOTER'])

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Configuration(bot))
 