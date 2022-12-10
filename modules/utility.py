import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, errors, colors

modulos = configs.get_commands()


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(aliases=modulos['utility']['avatar'])
    @app_commands.describe(user='Whose profile picture is it', local='Do you want the pfp from the server?')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def avatar(self, ctx, user : discord.Member, local : bool = False):
        '''Download someone's profile picture'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        if local: 
            pfp = user.display_avatar
        else:
            pfp = user.avatar

        embed = discord.Embed(description=lang['COMMAND']['AVATAR']['DESC 1']+str(pfp)+lang['COMMAND']['AVATAR']['DESC 2'], color=colors.default)
        embed.set_image(url=pfp.with_size(512))
        embed.set_author(name=lang['COMMAND']['AVATAR']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['AVATAR']['FOOTER'])
        await ctx.reply(embed=embed)


    @commands.hybrid_command(aliases=modulos['utility']['banner'])
    @app_commands.describe(user='Whose banner is it')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def banner(self, ctx, user : discord.Member):
        '''Download someone's banner'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        fuser = await self.bot.fetch_user(user.id)
        if fuser.banner == None:
            embed = discord.Embed(description=lang['COMMAND']['BANNER']['DESC NO BANNER 1']+str(fuser.id)+['COMMAND']['BANNER']['DESC NO BANNER 1'], color=colors.default)
        else:
            embed = discord.Embed(description=lang['COMMAND']['BANNER']['DESC 1']+str(fuser.banner)+lang['COMMAND']['BANNER']['DESC 2'], color=colors.default)
            embed.set_image(url=fuser.banner)
        embed.set_author(name=lang['COMMAND']['BANNER']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['BANNER']['FOOTER'])
        await ctx.reply(embed=embed)


    #@commands.hybrid_command(aliases=modulos['utility']['servericon'])
    #@app_commands.describe(user='Whose banner is it')
    #@commands.check(configs.Authentication.member)
    #@commands.check(configs.check_islocked)
    #@commands.check(configs.check_guild)
    #async def servericon(self, ctx, server : discord.Guild = None):
    #    '''Download someone's banner'''
    #    settings = configs.get_configs()
    #    lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
    #
    #    fuser = await self.bot.fetch_user(user.id)
    #    if fuser.banner == None:
    #        embed = discord.Embed(description=lang['COMMAND']['BANNER']['DESC NO BANNER 1']+str(fuser.id)+['COMMAND']['BANNER']['DESC NO BANNER 1'], color=colors.default)
    #    else:
    #        embed = discord.Embed(description=lang['COMMAND']['BANNER']['DESC 1']+str(fuser.banner)+lang['COMMAND']['BANNER']['DESC 2'], color=colors.default)
    #        embed.set_image(url=fuser.banner)
    #    embed.set_author(name=lang['COMMAND']['BANNER']['NAME'], icon_url=settings['bot-icon'])
    #    embed.set_thumbnail(url=settings['app-icon'])
    #    embed.set_footer(text=lang['COMMAND']['BANNER']['FOOTER'])
    #    await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Utility(bot))
