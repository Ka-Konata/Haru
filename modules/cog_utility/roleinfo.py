import discord
from discord import app_commands
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class Roleinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(aliases=modulos['utility']['roleinfo'])
    @app_commands.describe(role='The role you want to see the informations')
    @commands.check(configs.Authentication.member)
    @commands.check(configs.check_islocked)
    @commands.check(configs.check_guild)
    async def roleinfo(self, ctx, role : discord.Role):
        '''Get informations about a role'''
        settings = configs.get_configs()
        lang = configs.lang[configs.get_guild(ctx.guild.id)['language']]

        name = '**'+lang['COMMAND']['ROLELINFO']['MENTION']+'**: '+str(role.mention)
        id = '**'+lang['COMMAND']['ROLELINFO']['ID']+'**: `'+str(role.id)+'`'
        created = '**'+lang['COMMAND']['ROLELINFO']['CREATED']+'**: `'+role.created_at.strftime('%d/%m/%Y %H:%M:%S')+'`'

        desc = f'{name}\n{id}\n{created}'

        perms_aux   = configs.get_perms_as_dict(role.permissions)
        perms_cnt   = 0
        perms_str   = '```'
        for perm_name in perms_aux.keys():
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

        embed = discord.Embed(color=colors.default)
        embed.add_field(name=lang['COMMAND']['ROLELINFO']['INFO TITLE'], value=desc)
        embed.add_field(name=lang['COMMAND']['ROLELINFO']['PERMS TITLE'], value=perms_str, inline=False)
        embed.set_author(name=lang['COMMAND']['ROLELINFO']['NAME'], icon_url=settings['bot-icon'])
        embed.set_thumbnail(url=settings['app-icon'])
        embed.set_footer(text=lang['COMMAND']['ROLELINFO']['FOOTER'])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Roleinfo(bot))
 