import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class Servericon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(aliases=modulos['utility']['servericon'])
    @app_commands.describe(server='Guild ID')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def servericon(self, ctx, server : discord.Guild = None):
        '''Downloads a guild's icon'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
    
        if server == None:
            server_icon = ctx.guild.icon
        else:
            server_icon = server.icon
        
        embed = discord.Embed(description=lang['COMMAND']['SERVERICON']['DESC 1']+str(server_icon)+lang['COMMAND']['SERVERICON']['DESC 2'], color=colors.default)
        embed.set_image(url=str(server_icon))
        embed.set_author(name=lang['COMMAND']['SERVERICON']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['SERVERICON']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot): 
    await bot.add_cog(Servericon(bot))
 