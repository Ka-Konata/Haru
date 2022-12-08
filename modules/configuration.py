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
    @commands.check(configs.guild_check)
    async def prefix(self, ctx, new_prefix : str):
        '''Allows you to change the guild prefix'''
        settings = configs.get()
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

        await ctx.send(embed=embed)


    @prefix.error
    async def pretix_error(self, ctx, error):
        if isinstance(error, errors.PrefixVeryBig):
            lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
            embed = errors.get_error_embed(lang, lang['ERROR']['PrefixVeryBig']['TYPE'], lang['ERROR']['PrefixVeryBig']['REASON'])
        else:
            return None
        await ctx.send(embed=embed)

    
    @commands.hybrid_command(aliases=modulos['configuration']['language'])
    @app_commands.describe(language_code='Input the code for the desired language.')
    @commands.check(configs.Authentication.administrator)
    @commands.check(configs.guild_check)
    async def language(self, ctx, language_code : str):
        '''Allows you to change Haru's language'''
        settings = configs.get()
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

        await ctx.send(embed=embed)


    @language.error
    async def language_error(self, ctx, error):
        if isinstance(error, errors.LanguageDontExists):
            lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
            embed = errors.get_error_embed(lang, lang['ERROR']['LanguageDontExists']['TYPE'], reason=lang['ERROR']['LanguageDontExists']['REASON'], tip=lang['ERROR']['LanguageDontExists']['TIP'])
        else:
            return None
        await ctx.send(embed=embed)
        
    
    @language.autocomplete('language_code')
    async def help_autocomplete(self, interaction : discord.Interaction, current : str) -> typing.List[app_commands.Choice[str]]:
        languages = configs.get()['languages']
        choice_list = []
        for language in languages:
            if current.lower() in language and len(choice_list) < 25:
                choice_list.append(app_commands.Choice(name=language, value=language))
        return choice_list


async def setup(bot):
    await bot.add_cog(Configuration(bot))
 