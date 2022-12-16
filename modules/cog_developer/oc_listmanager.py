import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class OC_Listmanager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['_listmanager'])
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.check_guild)
    async def oc_listmanager(self, ctx):
        '''Lista todos os usuários com permissão de manager'''
        settings = configs.get_configs()

        mn_list = settings['manager-list']
        mn_list_str = ''
        c = 0
        for mn in mn_list:
            c += 1
            mn_list_str += ctx.bot.get_user(mn).mention
            if not c == len(mn_list):
                mn_list_str += ', '
        if mn_list_str == '':
            mn_list_str = '`nenhum`'

        embed=discord.Embed(color=colors.default)
        embed.add_field(name="Lista de Managers:", value=mn_list_str, inline=True)
        embed.set_footer(text=f"Total: {len(mn_list)} manager(s)")
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(OC_Listmanager(bot))
 