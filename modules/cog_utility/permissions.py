import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class Permissions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(aliases=modulos['utility']['permissions'])
    @app_commands.describe(member='The one you want to see the permissions')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def permissions(self, ctx, member : discord.Member = None):
        '''Get someone's permissions'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]
    
        if member == None:
            member = ctx.author

        perms_aux   = configs.get_perms_as_dict(member.guild_permissions)
        perms_cnt   = 0
        perms_str   = '```'
        for perm_name in  perms_aux.keys():
            if perms_aux[perm_name] and perm_name != 'value':
                try:
                    nm        = lang['PERMISSIONS'][perm_name]
                    perms_str = perms_str + f'{nm}, '
                except KeyError:
                    perms_str = perms_str + f'{perm_name}, '
                perms_cnt += 1
        perms_str = perms_str[0:-2] + '```'

        if perms_cnt == 0:
            perms_str = lang['COMMAND']['PERMISSIONS']['NONE']

        embed = discord.Embed(description=lang['COMMAND']['PERMISSIONS']['DESCRIPTION 1']+member.mention+lang['COMMAND']['PERMISSIONS']['DESCRIPTION 2']+member.top_role.mention, color=colors.default)
        embed.add_field(name=lang['COMMAND']['PERMISSIONS']['PERMS TITLE'], value=perms_str)
        embed.set_author(name=lang['COMMAND']['PERMISSIONS']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['PERMISSIONS']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Permissions(bot))
 