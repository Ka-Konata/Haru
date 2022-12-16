import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class Prefix(commands.Cog):
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

        await ctx.reply(embed=embed, mention_author=False)


    @prefix.error
    async def pretix_error(self, ctx, error):
        if isinstance(error, errors.PrefixVeryBig):
            lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
            embed = errors.get_error_embed(lang, lang['ERROR']['PrefixVeryBig']['TYPE'], lang['ERROR']['PrefixVeryBig']['REASON'])
        else:
            return None
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Prefix(bot))
 