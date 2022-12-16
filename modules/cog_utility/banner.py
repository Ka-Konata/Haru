import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class Banner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


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
            id = str(fuser.id)
            embed = discord.Embed(description=lang['COMMAND']['BANNER']['DESC NO BANNER 1']+fuser.mention+lang['COMMAND']['BANNER']['DESC NO BANNER 2'], color=colors.default)
        else:
            embed = discord.Embed(description=lang['COMMAND']['BANNER']['DESC 1']+str(fuser.banner)+lang['COMMAND']['BANNER']['DESC 2'], color=colors.default)
            embed.set_image(url=fuser.banner)
            embed.set_thumbnail(url=settings['app-icon'])
            embed.set_author(name=lang['COMMAND']['BANNER']['NAME'], icon_url=settings['bot-icon'])
        embed.set_footer(text=lang['COMMAND']['BANNER']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Banner(bot))
 