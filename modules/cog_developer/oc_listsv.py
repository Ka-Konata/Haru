import discord
from discord.ext import commands
from scripts import configs, colors

modulos = configs.get_commands()


class OC_Listsv(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['_listsv'])
    @commands.check(configs.Authentication.manager)
    @commands.check(configs.check_guild)
    async def oc_listsv(self, ctx):
        '''Lista todos os servidores liberados'''
        settings = configs.get_configs()

        sv_list = settings['server-list']
        sv_list_str = '```'
        c = 1
        for sv in sv_list:
            sv_list_str += ctx.bot.get_guild(sv).name + f' ({str(sv)})'
            if not c == len(sv_list):
                sv_list_str += ', '
            c += 1
        sv_list_str += '```'

        embed=discord.Embed(color=colors.default)
        embed.add_field(name="Lista de Servidores Liberados:", value=sv_list_str, inline=True)
        embed.set_footer(text=f"Total: {len(sv_list)} servidor(es)")
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(OC_Listsv(bot))
 